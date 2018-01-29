# -*- coding: utf-8 -*-
import threading
import socket
import datetime as dt
import random
import time
import struct
import json
import re
import Queue as queue

from nbcore import netbid

from history.historyfactory import HistoryFactory


def today_time(hour, minute, sec):
    today = dt.date.today()
    return dt.datetime(today.year, today.month, today.day, hour, minute, sec)


class TcpServer(object):

    def __init__(self, host, port, config=None, timeout=5000):
        self.is_started = False
        self.host = host
        self.port = port
        self.timeout = timeout
        self.config = config

    def serve(self):
        self.is_started = True

        server_sock = socket.socket()
        server_sock.bind((self.host, self.port))
        server_sock.listen(5)

        print 'TCP Server [listen]', self.host, self.port

        while self.is_started:
            print 'TCP Server [wait new socket]', self.host, self.port
            newsocket, fromaddr = server_sock.accept()
            print 'TCP Server [got new socket]', self.host, self.port

            ctx = Context(self.config)

            writer = Writer(newsocket, ctx)
            reader = Reader(newsocket, ctx)

            reader.start()
            writer.start()
            # newsocket.settimeout(self.timeout)


class Writer(threading.Thread):

    def __init__(self, wsock, context):
        super(Writer, self).__init__()
        self.wsock = wsock
        self.ctx = context

    def run(self):
        self.ctx.wait_init()

        while True:
            messages = self.ctx.replys()
            for m in messages:
                self.wsock.sendall(m)

            time.sleep(1)
            self.ctx.update()

            # do while at least send one reply
            if self.ctx.is_finished:
                break

        self.wsock.close()


class Reader(threading.Thread):

    def __init__(self, rsock, context):
        super(Reader, self).__init__()
        self.rsock = rsock
        self.ctx = context

    def run(self):
        data = self.rsock.recv(1024)
        self.ctx.process(data)
        self.ctx.starting_fishished()

        while not self.ctx.is_finished:
            data = self.rsock.recv(1024)
            self.ctx.process(data)


class Context(object):
    NORMAL = 0
    IMAGECODE_GOT = 1
    IN_QUEUE = 2
    QUEUE_FINISH = 3

    def __init__(self, config=None):
        self.config = config

        self.msg_queue = queue.Queue()
        self.init_event = threading.Event()
        self.is_init = False
        self.is_finished = False
        self.nb = netbid.MessageCoreFactory.create_message_core("0220")
        self.policy_name = "201711"
        self.policy = HistoryFactory().creatHistory(self.policy_name)

        self.state = self.NORMAL
        self.bid_no = 0
        self.cur_no = 0
        self.your_no = 0
        self.lowbidprice = 86300
        self.bidcount = 1
        self.bidamount = 86300
        self.realbidamount = 86300
        self.is_result_pushed = False

        self.timedelta = dt.datetime.now() - self.mock_datetime(11, 29, 10)

    def mock_datetime(self, hour, minute, second):
        mock_year = self.policy.auction_date.year
        mock_month = self.policy.auction_date.month
        mock_day = self.policy.auction_date.day
        return dt.datetime(mock_year, mock_month, mock_day, hour, minute, second)

    def getMocktime(self):
        #print(type(hour), type(minute), type(second))
        return dt.datetime.now() - self.timedelta

    def wait_init(self):
        self.init_event.wait()

    def starting_fishished(self):
        self.init_event.set()

    def process(self, clientdata):
        #print 'got',clientdata
        if len(clientdata) == 0:
            return

        if "policy-file-request" in clientdata:
            self.msg_queue.put(
                '<cross-domain-policy><allow-access-from domain="*" to-ports="*" /></cross-domain-policy>')
            self.is_finished = True
            return

        messages = self.nb.dec_client_data(clientdata)
        for msg in messages:
            #print msg
            pmethod = getattr(self, 'reply%d_%d' % (msg.period1, msg.period2))
            r = pmethod(msg)
            if r:
                self.msg_queue.put(r)
                reply = self.nb.dec_server_data(r)

    #                print 'debug reply',reply

    def replys(self):
        replys = []
        while not self.msg_queue.empty():
            replys.append(self.msg_queue.get())
            self.msg_queue.task_done()



        # 需要添加的功能
        # 1，11：30：00后页面改变为G
        # 2，中标信息出来后，弹框告知，并页面改变为D
        mock_time = self.getMocktime()
        if self.mock_datetime(11, 00, 00) <= mock_time < self.mock_datetime(11, 30, 00):
            replys.append(self.s2c0301(stage='B'))
        elif self.mock_datetime(11, 30, 00) <= mock_time < self.mock_datetime(11, 30, 10):
            replys.append(self.s2c0301(stage='G'))
        elif self.mock_datetime(11, 30, 10) <= mock_time < self.mock_datetime(11, 40, 00):
            replys.append(self.s2c0301(stage='D'))
        elif self.mock_datetime(10, 30, 00) <= mock_time < self.mock_datetime(11, 00, 00):
            replys.append(self.s2c0301(stage='A'))
        elif self.mock_datetime(8, 30, 00) <= mock_time < self.mock_datetime(10, 30, 00):
            replys.append(self.s2c0301(stage='F'))

        return replys

    def update(self):
        #         print 'cur_no:%d, bid_no:%d, your_no:%d'%(self.cur_no,self.bid_no,self.your_no)
        mock_time = self.getMocktime()
        self.lowbidprice = self.policy.getLowPrice(mock_time)

        self.cur_no += random.randint(50, 100)

        # 6 新增代码，大于11，30，45， 拍牌结束
        if mock_time > self.mock_datetime(11, 30, 45):
            self.is_finished = True

        # 6 新增代码，大于11，30，07，给出出价结果;
        # print(mock_time, self.realbidamount, self.lowbidprice)
        if mock_time > self.mock_datetime(11, 30, 07) and not self.is_result_pushed:
            if self.realbidamount >= self.lowbidprice:

                r = self.nb.s2c0203("4004", self.bidamount, self.bidnumber,
                                    (dt.datetime.now() - self.timedelta),
                                    "恭喜你，中标了！30s后将自动重新模拟".format(
                                        realbidamount=self.realbidamount, lowbidprice=self.lowbidprice),
                                    str(self.bidcount),
                                    mock_time,
                                    self.requestid)
            else:

                r = self.nb.s2c0203("4004", self.bidamount, self.bidnumber,
                                    (dt.datetime.now() - self.timedelta),
                                    "很遗憾，您没中标。30s后将自动重新模拟".format(
                                        bidamount=self.realbidamount, lowbidprice=self.lowbidprice),
                                    str(self.bidcount),
                                    mock_time, self.requestid)

            self.msg_queue.put(r)
            self.is_result_pushed = True
        """
        if random.randint(0,3) == 0:
            self.lowbidprice += 100
        """

        if self.state == self.IN_QUEUE:
            if self.cur_no >= self.your_no:
                self.state = self.QUEUE_FINISH

        if self.state == self.QUEUE_FINISH:

            # 检测是否拍卖结束

            if mock_time > self.mock_datetime(11, 30, 0):
                r = self.nb.s2c0203("0", self.bidamount, self.bidnumber,
                                    (dt.datetime.now() - self.timedelta).strftime("%Y-%m-%d %H:%M:%S"),
                                    "拍卖已结束", str(self.bidcount), mock_time,
                                    self.requestid)

            # 检测修改次数
            elif self.bidcount >= 3:
                r = self.nb.s2c0203("4004", self.bidamount, self.bidnumber,
                                    (dt.datetime.now() - self.timedelta).strftime("%Y-%m-%d %H:%M:%S"),
                                    "超过修改次数", str(self.bidcount), mock_time,
                                    self.requestid)

            # 检测价格区间
            elif int(self.bidamount) > self.lowbidprice + 300 or int(self.bidamount) < self.lowbidprice - 300:

                r = self.nb.s2c0203("4015", self.bidamount, self.bidnumber,
                                    (dt.datetime.now() - self.timedelta).strftime("%Y-%m-%d %H:%M:%S"),
                                    "您的出价不在目前数据库接受处理价格%d-%d元区间范围内，请重新出价！" % (
                                        self.lowbidprice - 300, self.lowbidprice + 300),
                                    str(self.bidcount), mock_time, self.requestid)
            else:
                self.bidcount += 1
                self.realbidamount = int(self.bidamount)
                r = self.nb.s2c0203("0", self.bidamount, self.bidnumber,
                                    (dt.datetime.now() - self.timedelta).strftime("%Y-%m-%d %H:%M:%S"),
                                    "出价有效", str(self.bidcount), mock_time,
                                    self.requestid)

            self.msg_queue.put(r)
            self.state = self.NORMAL

    def reply1_1(self, msg):
        # print 'reply 1-1', msg
        responsecode = 0
        responsemsg = "建立成功"

        bidamount = 100
        bidnumber = msg.getprop('bidnumber')

        bidcount = 1
        stype = 1
        requestid = msg.getprop('requestid')
        dealtime = self.mock_datetime(10, 30, 01)
        # print(type(dealtime))

        # 7添加功能：根据传回的bidnumber值，确定所属历史月份的队列

        #self.bidnumber = bidnumber
        #self.policy_name = str(bidnumber)[:6]
        #self.policy = HistoryFactory().creatHistory(self.policy_name)
        #self.mockdate = dt.datetime(self.bidnumber[:4], self.bidnumber[4:6], self.bidnumber[6:])
        #print("bidnumber", self.bidnumber, str(bidnumber)[:6])


        return self.nb.s2c0101(responsecode, responsemsg,
                               bidamount, bidnumber, bidcount, stype, requestid, dealtime)

    def reply0_0(self, msg):
        #         print 'reply 0-0'

        return None

    def reply2_1(self, msg):
        self.state = self.IMAGECODE_GOT
        requestid = msg.getprop('requestid')
        img = self.policy.getRandImageCode()
        self.correct_imgnum = img[0]
        return self.nb.s2c0201("0", "Success", img[2], img[1], requestid)

    def reply2_2(self, msg):
        mock_time = self.getMocktime()
        self.bid_no = self.cur_no
        if mock_time > self.mock_datetime(11, 29, 50):
            self.your_no = self.cur_no + random.randint(0, 500)
        else:
            self.your_no = self.cur_no + random.randint(0, 30)

        requestid = msg.getprop('requestid')
        bidnumber = msg.getprop('bidnumber')
        bidamount = msg.getprop('bidamount')
        client_imgnum = msg.getprop('imagenumber')

        self.requestid = requestid
        self.bidnumber = bidnumber
        self.bidamount = int(bidamount)

        # 检测验证码是否正确
        if client_imgnum != self.correct_imgnum:
            self.state = self.NORMAL
            return self.nb.s2c0203("4004", self.bidamount, self.bidnumber,
                                   mock_time.strftime("%Y-%m-%d %H:%M:%S"),
                                   "验证码不正确", str(self.bidcount), mock_time,
                                   self.requestid)

        elif client_imgnum == self.correct_imgnum:
            self.state = self.IN_QUEUE
            # print(self.your_no,self.bid_no,self.cur_no)
            return self.nb.s2c0202("0", "成功", bidamount, bidnumber,
                                   "出价入列，您处于第%d位，%d，%d" % (self.your_no, self.your_no, self.bid_no), "0", requestid,
                                   "0001-01-01 00:00:00")

    #这里的消息，要想清楚，什么参数需要simserver里传递，什么参数是可选的传递，什么参数直接在netbid里获取就行。
    def s2c0301(self, stage):
        mock_time = self.getMocktime()
        #这里的字典的键不能随意改动，只可改其参数
        if stage == "A":
            time0 = mock_time.strftime("%Y%m%d%H%M%S")
            stage1 = "A"
            auctionType2 = "0"  # 0代表个人，1代表单位
            auctionDate3 = self.policy.auction_date.strftime("%Y%m%d")
            quota4 = self.policy.cards
            warningPrice5 = str(self.policy.warning_price)
            priceLowerLimit6 = "100"
            startTime7 = "1030"
            updateTime8 = "1100"
            endTime9 = "1130"
            systemTime10 = mock_time.strftime("%H%M%S")
            numberOfBidUsers11 = str(self.policy.bid_people)
            basePrice12 = str(self.lowbidprice)
            # 这里还需要改变basepricetime，先不管
            basePriceTime13 = self.policy.getBasePriceTime(mock_time)           #basePriceTime13 = "20150622110229"
            tradeSn14 = str(self.cur_no)
            queueLength15 = str(self.your_no - self.cur_no)

            kwargs = locals()
            kwargs.pop("self")
            kwargs.pop("stage")
            #print(kwargs)

            return self.nb.s2c0301(kwargs, "A")

        elif stage == "B":
            time0 = mock_time.strftime("%Y%m%d%H%M%S")
            stage1 = "B"
            auctionType2 = "0"  # 0代表个人，1代表单位
            auctionDate3 = self.policy.auction_date.strftime("%Y%m%d")
            quota4 = self.policy.cards
            numberOfBidUsers5 = str(self.policy.bid_people)
            priceLowerLimit6 = "100"
            startTime7 = "1030"
            updateTime8 = "1100"
            endTime9 = "1130"
            systemTime10 = mock_time.strftime("%H%M%S")
            basePrice11 = str(self.lowbidprice)
            basePriceTime12 = self.policy.getBasePriceTime(mock_time)
            var12013 = str(self.lowbidprice - 300)
            var12114 = str(self.lowbidprice + 300)
            tradeSn15 = str(self.cur_no)
            queueLength16 = str(self.your_no - self.cur_no)

            kwargs = locals()
            kwargs.pop("self")
            kwargs.pop("stage")
            #print(kwargs)

            return self.nb.s2c0301(kwargs, "B")

        # E,H消息暂不知作用
        elif stage == "C" or stage == 'E' or stage == 'H':
            time0 = mock_time.strftime("%Y%m%d%H%M%S")
            stage1 = "C"
            content2 = "没有正在举行的拍卖会，请注意拍卖公告！查询请到WWW.ALLTOBID.COM"

            kwargs = locals()
            kwargs.pop("self")
            kwargs.pop("stage")
            #print(kwargs)

            return self.nb.s2c0301(kwargs, "C")

        elif stage == 'D':
            time0 = mock_time.strftime("%Y%m%d%H%M%S")
            stage1 = "D"
            content2 = ("""
{auctionDate}上海市个人非营业性客车额度投标拍卖会结果公布
参加拍卖人数：{numberOfBidUsers}
最低成交价：{lowbidprice}
最低成交价的截止时间：{basepricetime}
平均成交价：{averageprice}
请拍卖成交的买受人在XX月XX日～YY日(9:00-16:00)到下列服务点办理成交付款手续。
1.长宁区淞虹路938号（福缘湾九华商业广场地下1层A2）
2.共和新路3550号（百联汽车广场）
3.东江湾路444号（虹口足球场4区113）
4.新镇路288号（闵行体育馆架空层B2区）
5.新村路1500号1层107（家乐福上海万里店内）
6.浦东成山路800号（云顶国际商业广场A座101）
注：福州路108号（公司本部）不办理成交付款结算手续
另：我公司网站已开通网上支付结算，大家可登录查询。
                    """)
            tradeSn3 = str(self.cur_no)  # tradeSn15 = str(cur_pos)
            queueLength4 = str(self.your_no - self.cur_no)

            kwargs = locals()
            kwargs.pop("self")
            kwargs.pop("stage")
            #print(kwargs)

            return self.nb.s2c0301(kwargs, "D")
        elif stage == "G":
            time0 = mock_time.strftime("%Y%m%d%H%M%S")
            stage1 = "G"
            auctionType2 = "0"
            auctionDate3 = self.policy.auction_date.strftime("%Y%m%d")
            content4 = """稍后发布拍卖会结果，请等待！

拍卖会结果也可通过本公司网站、微信公众号进行查询，网址：www.alltobid.com，微信公众号：shanghaiguopai
            """
            tradeSn5 = str(self.cur_no)  # tradeSn15 = str(cur_pos)
            queueLength6 = str(self.your_no - self.cur_no)

            kwargs = locals()
            kwargs.pop("self")
            kwargs.pop("stage")
            #print(kwargs)

            return self.nb.s2c0301(kwargs, "G")

        elif stage == 'F':
            time0 = mock_time.strftime("%Y%m%d%H%M%S")
            stage1 = "F"
            auctionType2 = "0"
            auctionDate3 = self.policy.auction_date.strftime("%Y%m%d")
            startTime4 = '1030'
            endTime5 = '1130'
            systemTime6 = mock_time.strftime("%H%M%S")

            kwargs = locals()
            kwargs.pop("self")
            kwargs.pop("stage")
            #print(kwargs)

            return self.nb.s2c0301(kwargs, "F")


HOST = ''  # Symbolic name meaning all available interfaces
PORT = 8300  # Arbitrary non-privileged port


def main():
    server1 = TcpServer(HOST, PORT)
    server1.serve()


if __name__ == "__main__": main()
