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

"""
已复制到historydata.historyRandom
IMAGES = [
["7695","输入下面带星的四位数字","http://51moni-sh.oss-cn-shanghai.aliyuncs.com/base1.png?id=cf920e81-4a73-4e69-beea-bdcd3929abcb&i=2b4ca06b3f1790e1a232dba065ffda3f"],
["1187","输入下面不带星的四位数字","http://51moni-sh.oss-cn-shanghai.aliyuncs.com/base2.png?id=cf920e81-4a73-4e69-beea-bdcd3929abcb&i=2b4ca06b3f1790e1a232dba065ffda3f"],
["2249","输入苹果行的四位数字校验码","http://51moni-sh.oss-cn-shanghai.aliyuncs.com/yzm1710/b1172~a2249.png"],
["1683","输入香蕉行的四位数字校验码","http://51moni-sh.oss-cn-shanghai.aliyuncs.com/yzm1710/b1683~a3369.png?id=cf920e81-4a73-4e69-beea-bdcd3929abcb&i=2b4ca06b3f1790e1a232dba065ffda3f"],
["3369","输入苹果行的四位数字校验码","http://51moni-sh.oss-cn-shanghai.aliyuncs.com/yzm1710/b1683~a3369.png?id=cf920e81-4a73-4e69-beea-bdcd3929abcb&i=2b4ca06b3f1790e1a232dba065ffda3f"],
["1698","输入香蕉行的四位数字校验码","http://51moni-sh.oss-cn-shanghai.aliyuncs.com/yzm1710/b1698~a1293.png?id=cf920e81-4a73-4e69-beea-bdcd3929abcb&i=2b4ca06b3f1790e1a232dba065ffda3f"],
["1293","输入苹果行的四位数字校验码","http://51moni-sh.oss-cn-shanghai.aliyuncs.com/yzm1710/b1698~a1293.png?id=cf920e81-4a73-4e69-beea-bdcd3929abcb&i=2b4ca06b3f1790e1a232dba065ffda3f"],
["2072","输入香蕉行的四位数字校验码","http://51moni-sh.oss-cn-shanghai.aliyuncs.com/yzm1710/b2072~a6647.png?id=cf920e81-4a73-4e69-beea-bdcd3929abcb&i=2b4ca06b3f1790e1a232dba065ffda3f"],
["6647","输入苹果行的四位数字校验码","http://51moni-sh.oss-cn-shanghai.aliyuncs.com/yzm1710/b2072~a6647.png?id=cf920e81-4a73-4e69-beea-bdcd3929abcb&i=2b4ca06b3f1790e1a232dba065ffda3f"],
["3389","输入香蕉行的四位数字校验码","http://51moni-sh.oss-cn-shanghai.aliyuncs.com/yzm1710/b3389~a3968.png?id=cf920e81-4a73-4e69-beea-bdcd3929abcb&i=2b4ca06b3f1790e1a232dba065ffda3f"],
["3968","输入苹果行的四位数字校验码","http://51moni-sh.oss-cn-shanghai.aliyuncs.com/yzm1710/b3389~a3968.png?id=cf920e81-4a73-4e69-beea-bdcd3929abcb&i=2b4ca06b3f1790e1a232dba065ffda3f"],
["4845","输入香蕉行的四位数字校验码","http://51moni-sh.oss-cn-shanghai.aliyuncs.com/yzm1710/b4845~a6136.png?id=cf920e81-4a73-4e69-beea-bdcd3929abcb&i=2b4ca06b3f1790e1a232dba065ffda3f"],
["6136","输入苹果行的四位数字校验码","http://51moni-sh.oss-cn-shanghai.aliyuncs.com/yzm1710/b4845~a6136.png?id=cf920e81-4a73-4e69-beea-bdcd3929abcb&i=2b4ca06b3f1790e1a232dba065ffda3f"],
["4936","输入香蕉行的四位数字校验码","http://51moni-sh.oss-cn-shanghai.aliyuncs.com/yzm1710/b4936~a8850.png?id=cf920e81-4a73-4e69-beea-bdcd3929abcb&i=2b4ca06b3f1790e1a232dba065ffda3f"],
["8850","输入苹果行的四位数字校验码","http://51moni-sh.oss-cn-shanghai.aliyuncs.com/yzm1710/b4936~a8850.png?id=cf920e81-4a73-4e69-beea-bdcd3929abcb&i=2b4ca06b3f1790e1a232dba065ffda3f"],
["7213","输入香蕉行的四位数字校验码","http://51moni-sh.oss-cn-shanghai.aliyuncs.com/yzm1710/b7213~a1015.png?id=cf920e81-4a73-4e69-beea-bdcd3929abcb&i=2b4ca06b3f1790e1a232dba065ffda3f"],
["1015","输入苹果行的四位数字校验码","http://51moni-sh.oss-cn-shanghai.aliyuncs.com/yzm1710/b7213~a1015.png?id=cf920e81-4a73-4e69-beea-bdcd3929abcb&i=2b4ca06b3f1790e1a232dba065ffda3f"],
["7650","输入香蕉行的四位数字校验码","http://51moni-sh.oss-cn-shanghai.aliyuncs.com/yzm1710/b7650~a2972.png?id=cf920e81-4a73-4e69-beea-bdcd3929abcb&i=2b4ca06b3f1790e1a232dba065ffda3f"],
["2972","输入苹果行的四位数字校验码","http://51moni-sh.oss-cn-shanghai.aliyuncs.com/yzm1710/b7650~a2972.png?id=cf920e81-4a73-4e69-beea-bdcd3929abcb&i=2b4ca06b3f1790e1a232dba065ffda3f"],

    ]
"""


##IMAGES = [
##    ["0048","请输入第一行图像校验码","http://liuziyu.oss-cn-hangzhou.aliyuncs.com/yzm5/b9749-a9373.png?ep=7788"],]

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
        self.policy_name = "201707"
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

        self.timedelta = dt.datetime.now() - today_time(11, 29, 00)

    def getMocktime(self):
        return dt.datetime.now() - self.timedelta

    def wait_init(self):
        self.init_event.wait()

    def starting_fishished(self):
        self.init_event.set()

    def process(self, clientdata):
        # type: (object) -> object

        #        print 'got',clientdata
        if len(clientdata) == 0:
            return

        if "policy-file-request" in clientdata:
            self.msg_queue.put(
                '<cross-domain-policy><allow-access-from domain="*" to-ports="*" /></cross-domain-policy>')
            self.is_finished = True
            return

        messages = self.nb.dec_client_data(clientdata)
        for msg in messages:
            #             print msg
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

        mock_time = self.getMocktime()

        #需要添加的功能
        #1，11：30：00后页面改变为G
        #2，中标信息出来后，弹框告知，并页面改变为D
        if today_time(11,00,00) <= mock_time < today_time(11,30,00):
            replys.append(self.nb.s2c0301(self.lowbidprice, self.cur_no, cur_time=mock_time, stage='B'))
        elif today_time(11,30,00) <= mock_time < today_time(11,30,10):
            replys.append(self.nb.s2c0301(self.lowbidprice, self.cur_no, cur_time=mock_time, stage='G'))
        elif today_time(11, 30, 10) <= mock_time < today_time(11, 40, 00):
            replys.append(self.nb.s2c0301(self.lowbidprice, self.cur_no, cur_time=mock_time, stage='D'))
        elif today_time(10, 30, 00) <= mock_time < today_time(11, 00, 00):
            replys.append(self.nb.s2c0301(self.lowbidprice, self.cur_no, cur_time=mock_time, stage='A'))

        return replys

    def update(self):
        #         print 'cur_no:%d, bid_no:%d, your_no:%d'%(self.cur_no,self.bid_no,self.your_no)
        mock_time = self.getMocktime()
        self.lowbidprice = self.policy.getLowPrice(mock_time)

        self.cur_no += random.randint(50, 100)

        # 6 新增代码，大于11，30，30， 拍牌结束
        if mock_time > today_time(11, 30, 30):
            self.is_finished = True

        # 6 新增代码，大于11，30，07，给出出价结果;
        #print(mock_time, self.realbidamount, self.lowbidprice)
        if mock_time > today_time(11, 30, 07) and not self.is_result_pushed:
            if self.realbidamount >= self.lowbidprice:

                r = self.nb.s2c0203("4004", self.bidamount, self.bidnumber,
                                    (dt.datetime.now() - self.timedelta),
                                    "恭喜你，中标了！您的出价金额为{realbidamount},最低中标价为{lowbidprice},30s后将自动重新模拟".format(
                                    realbidamount=self.realbidamount,lowbidprice=self.lowbidprice),
                                    str(self.bidcount),
                                    mock_time,
                                    self.requestid)
            else:

                r = self.nb.s2c0203("4004", self.bidamount, self.bidnumber,
                                    (dt.datetime.now() - self.timedelta),
                                    "很遗憾，您没中标，您的出价金额为{bidamount},最低中标价为{lowbidprice},30s后将自动重新模拟".format(
                                            bidamount=self.realbidamount,lowbidprice=self.lowbidprice),
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

            if mock_time > today_time(11, 30, 0):
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
        #print 'reply 1-1', msg
        responsecode = 0
        responsemsg = "建立成功"

        bidamount = 100
        bidnumber = msg.getprop('bidnumber')

        bidcount = 1
        stype = 1
        requestid = msg.getprop('requestid')
        dealtime = today_time(10, 30, 01)
        print(type(dealtime))

        #7添加功能：根据传回的bidnumber值，确定所属历史月份的队列
        self.bidnumber = bidnumber
        self.policy_name = str(bidnumber)[:6]
        self.policy = HistoryFactory().creatHistory(self.policy_name)
        print("bidnumber", self.bidnumber, str(bidnumber)[:6])

        return self.nb.s2c0101(responsecode, responsemsg,
                               bidamount, bidnumber, bidcount, stype, requestid,dealtime)

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
        if mock_time > today_time(11, 29, 50):
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
            #print(self.your_no,self.bid_no,self.cur_no)
            return self.nb.s2c0202("0", "成功", bidamount, bidnumber,
                               "出价入列，您处于第%d位，%d，%d" % (self.your_no, self.your_no, self.bid_no), "0", requestid,
                               "0001-01-01 00:00:00")





HOST = ''  # Symbolic name meaning all available interfaces
PORT = 8300  # Arbitrary non-privileged port


def main():
    server1 = TcpServer(HOST, PORT)
    server1.serve()


if __name__ == "__main__": main()
