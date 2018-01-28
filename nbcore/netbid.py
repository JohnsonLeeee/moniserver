# -*- coding: utf-8 -*-
import struct
import datetime as dt
import re
import encutil
import json
import traceback as tb

DEBUG = False
today = dt.date.today()


def parse_time_str(time_str):
    try:
        temp = dt.datetime.strptime(time_str, '%H:%M:%S')
        return dt.datetime(today.year, today.month, today.day, temp.hour, temp.minute, temp.second)
    except:
        return dt.datetime.now()


def time2str(t):
    return t.strftime("%Y%m%d%H%M%S")


def daytime(datetimeobj):
    return datetimeobj.strftime("%H:%M:%S")


def hex2str(hex_str):
    s = []
    for i in range(0, len(hex_str), 2):
        h = hex_str[i:i + 2]
        s.append(chr(int(h, 16)))

    return "".join(s)


def findprop(propname, jsonstr):
    m = re.search(r'%s:"(.+?)"' % propname, jsonstr)
    return m.group(1)


class ClientMessage(object):

    def __init__(self, heading, body):
        self.heading = heading
        self.body = body
        self.period1 = heading[1]
        self.period2 = heading[2]
        self.period = '%d-%d' % (heading[1], heading[2])

    def getprop(self, prop):
        return findprop(prop, self.body)

    def __str__(self):
        return '%s [%s]' % (self.period, self.body)

    def __repr__(self):
        return self.__str__()


class ServerMessage(object):

    def __init__(self, heading, body):
        self.heading = heading
        self._body = body
        self.period1 = heading[1]
        self.period2 = heading[2]
        self.period = '%d-%d' % (heading[1], heading[2])
        self.json_body = json.loads(body)

    def body(self):
        return self.json_body

    def __str__(self):
        return '%s [%s]' % (self.period, self._body)

    def __repr__(self):
        return self.__str__()


class ServerSecMessage(object):

    def __init__(self, heading, body):
        self.heading = heading
        self._body = body
        self.period1 = heading[1]
        self.period2 = heading[2]
        self.period = '%d-%d' % (heading[1], heading[2])
        elems = body.split(',')
        if elems[1] == 'A':
            self._server_time = parse_time_str(elems[11])
            self._server_price = int(elems[13])
            self._server_pos = int(elems[15])
        else:
            self._server_time = parse_time_str(elems[13])
            self._server_price = int(elems[14])
            self._server_pos = int(elems[18])

    def server_pos(self):
        return self._server_pos

    def server_time(self):
        return self._server_time

    def server_price(self):
        return self._server_price

    def __str__(self):
        return '%s [%s]' % (self.period, self._body)

    def __repr__(self):
        return self.__str__()


class MessageCoreFactory(object):

    @staticmethod
    def create_message_core(version):
        if version == '622':
            config = {'s1': 5, 's2': 2, 's3': 3, 's4': 4, 'key': 'shcarbid'}
            return MessageCore622(config)

        if version == '1024':
            config = {'s1': 4, 's2': 2, 's3': 3, 's4': 5, 'key': 'gp#h$n%'[2:7]}
            return MessageCore1024(config)
        if version == '1121':
            config = {'s1': 4, 's2': 2, 's3': 3, 's4': 5, 'key': 'gp#h$n%'[2:7]}
            return MessageCore1024(config)

        if version == '1219':
            config = {'s1': 4, 's2': 2, 's3': 3, 's4': 5, 'key': 'gp*g(0&'[2:2 + 5]}
            return MessageCore1024(config)

        if version == '0220':
            config = {'s1': 4, 's2': 2, 's3': 3, 's4': 6, 'key': 'ji!@p!a'[2:2 + 5], 'msg_decode_len': 7}
            return MessageCore1024(config)


class MessageCore622(object):
    template_c2s0000 = '{requestid:"%(requestid)s",timestamp:"%(timestamp)s",bidnumber:"%(bidnumber)s",' \
                       'checkcode:"%(checkcode)s",version:%(version)s,' \
                       'request:{timespan:%(timespan)s}}'

    template_s2c0101 = '{"response":{"responsecode":%(responsecode)s,"responsemsg":"%(responsemsg)s",' \
                       '"data":{"informationtemplate":"",' \
                                '"results":[{"bidamount":"%(bidamount)d","bidnumber":"%(bidnumber)s",' \
                                '"bidtime":"%(bidtime)s","msg":"%(msg)s","bidcount":%(bidcount)d,"type":%(type)d,"' \
                                'requestid":"%(lastrequestid)s","code":0,"dealtime":"%(dealtime)s"}]}},' \
                       '"requestid":"%(requestid)s","servertime":"%(servertime)s"}'

    template_s2c0201 = '{"response":{"responsecode":%(responsecode)s,"responsemsg":"%(responsemsg)s",' \
                       '"data":{"imageurl":"%(imageurl)s","prompt":"%(prompt)s"}},' \
                       '"requestid":"%(requestid)s","servertime":"%(servertime)s"}'

    template_s2c0202 = '{"response":{"responsecode":%(responsecode)s,"responsemsg":"%(responsemsg)s",' \
                       '"data":{"bidamount":"%(bidamount)s","bidnumber":"%(bidnumber)s",' \
                                '"bidtime":"%(bidtime)s","msg":"%(msg)s","bidcount":%(bidcount)s,' \
                                '"type":%(stype)s,"requestid":"%(requestid)s","code":%(code)s,"dealtime":"%(dealtime)s"}},' \
                       '"requestid":"%(requestid)s","servertime":"%(servertime)s"}'

    template_s2c0203 = '{"response":{"responsecode":%(responsecode)s,"responsemsg":"",' \
                       '"data":{"bidamount":"%(bidamount)s","bidnumber":"%(bidnumber)s",' \
                                '"bidtime":"%(bidtime)s","msg":"%(msg)s","bidcount":%(bidcount)s,' \
                                '"type":%(stype)s,"requestid":"%(requestid)s","code":%(code)s,"dealtime":"%(dealtime)s"}},' \
                       '"requestid":"%(requestid)s","servertime":"%(servertime)s"}'
    # this is for 6-22
    CLIENT_ID = "4d3d87126d5446248c44ff0f33cc75b3"
    VERSION = "1.0"
    KEY = "shcarbid"
    TIMESPAN = "0"

    def __init__(self, config):
        self.encdec = encutil.EncDec(config)
        self.msg_decode_len = config.get('msg_decode_len', 5)

    def head(self, msg_length, stage1, stage2):
        return struct.pack('>lBBl', msg_length + 10, stage1, stage2, msg_length)

    def unhead(self, heading):
        return struct.unpack('>lBBl', heading)

    def dec_client_data(self, data):
        messages = []
        datalen = len(data)
        startidx = 0
        while startidx < datalen:
            heading = self.unhead(data[startidx:startidx + 10])
            enc_body = data[startidx + 10:startidx + heading[0]]
            if heading[1] == 3:
                body = encutil.demix_msg(enc_body.decode('utf-8')).encode('utf-8')
            else:
                body = self.encdec.dec(enc_body)
            print heading, body
            messages.append(ClientMessage(heading, body))
            startidx += heading[0]

        return messages

    def dec_server_data(self, data):
        messages = []
        datalen = len(data)
        startidx = 0
        while startidx < datalen:
            heading = self.unhead(data[startidx:startidx + 10])
            enc_body = data[startidx + 10:startidx + heading[0]]
            if heading[1] == 3:
                body = encutil.demix_msg(enc_body.decode('utf-8')).encode('utf-8')
                messages.append(ServerSecMessage(heading, body))
            else:
                body = self.encdec.dec(enc_body)
                messages.append(ServerMessage(heading, body))
            startidx += heading[0]
        return messages

    def cal_timestamp(self, delta=None):
        n = dt.datetime.now()
        if delta:
            n = n - delta

        return "%d%d%d%d" % (n.hour, n.minute, n.second, n.microsecond)

    def c2s0000(self, bidnumber):
        timestamp = self.cal_timestamp()
        requestid = bidnumber + "." + timestamp
        checkcode = encutil.one_time_md5(
            bidnumber + self.CLIENT_ID + requestid + self.TIMESPAN + timestamp + self.VERSION)
        raw_text = self.template_c2s0000 % {
            'requestid': requestid,
            'timestamp': timestamp,
            'bidnumber': bidnumber,
            'checkcode': checkcode,
            'version': self.VERSION,
            'timespan': self.TIMESPAN,
        }

        enc_text = self.encdec.enc(raw_text)
        return self.head(len(enc_text), 0, 0) + enc_text

    def s2c0000(self):
        enc_text = "test"
        return self.head(len(enc_text), 0, 0) + enc_text

    def c2s0101(self, bidnumber):
        self.cal_timestamp()

    def s2c0101(self, responsecode, responsemsg,
                bidamount, bidnumber, bidcount, stype, requestid):
        lastrequestid = bidnumber + "." + self.cal_timestamp(dt.timedelta(seconds=30))

        bidtime = (dt.datetime.now() - dt.timedelta(seconds=30)).strftime('%Y-%m-%d %H:%M:%S')
        msg = '出价有效'
        bidcount = 1
        dealtime = bidtime
        servertime = time2str(dt.datetime.now())

        raw_text = self.template_s2c0101 % {
            'responsecode': responsecode,
            'responsemsg': responsemsg,
            'bidamount': bidamount,
            'bidnumber': bidnumber,
            'bidtime': bidtime,
            'msg': msg,
            'bidcount': bidcount,
            'type': stype,
            'lastrequestid': lastrequestid,
            'dealtime': dealtime,
            'requestid': requestid,
            'servertime': servertime
        }

        enc_text = self.encdec.enc(raw_text)
        return self.head(len(enc_text), 1, 1) + enc_text

    def c2s0201(self, bidnumber, bidamount):
        # get image code
        pass

    def s2c0201(self, responsecode, responsemsg,
                imageurl, prompt, requestid):
        # response imagecode
        servertime = time2str(dt.datetime.now())
        raw_text = self.template_s2c0201 % {
            'responsecode': responsecode,
            'responsemsg': responsemsg,
            'imageurl': imageurl,
            'prompt': prompt,
            'requestid': requestid,
            'servertime': servertime,
        }

        enc_text = self.encdec.enc(raw_text)
        return self.head(len(enc_text), 2, 1) + enc_text

    def c2s0202(self, bidnumber, bidamount, imagenumber):
        # commit imagecode
        self.cal_timestamp()

        """
        template_s2c0202 = '{"response":{"responsecode":%(responsecode)s,"responsemsg":"%(responsemsg)s",' \
                   '"data":{"bidamount":"%(bidamount)s","bidnumber":"%(bidnumber)s",' \
                            '"bidtime":"%(bidtime)s","msg":"%(msg)s","bidcount":%(bidcount)s,' \
                            '"type":%(stype)s,"requestid":"%(requestid)s","code":%(code)s,"dealtime":"%(dealtime)s"}},' \
                   '"requestid":"%(requestid)s","servertime":"%(servertime)s"}'
        """

    def s2c0202(self, responsecode, responsemsg, bidamount, bidnumber, msg, bidcount, requestid, dealtime, stype="1",
                code="0"):
        # in queue message
        servertime = time2str(dt.datetime.now())
        bidtime = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        raw_text = self.template_s2c0202 % locals()
        enc_text = self.encdec.enc(raw_text)
        return self.head(len(enc_text), 2, 2) + enc_text

    """
    template_s2c0203 = '{"response":{"responsecode":%(responsecode)s,"responsemsg":"",' \
                   '"data":{"bidamount":"%(bidamount)s","bidnumber":"%(bidnumber)s",' \
                            '"bidtime":"%(bidtime)s","msg":"%(msg)s","bidcount":%(bidcount)s,' \
                            '"type":%(stype)s,"requestid":"%(requestid)s","code":%(code)s,"dealtime":"%(dealtime)s"}},' \
                   '"requestid":"%(requestid)s","servertime":"%(servertime)s"}'
    """

    def s2c0203(self, responsecode,
                bidamount, bidnumber, bidtime, msg, bidcount, dealtime, requestid, stype="1", code="0"):
        servertime = time2str(dt.datetime.now())
        raw_text = self.template_s2c0203 % locals()
        enc_text = self.encdec.enc(raw_text)
        return self.head(len(enc_text), 2, 3) + enc_text

    def s2c0301(self, lowbidprice, cur_pos, stage='B'):
        if stage == 'A':
            """
            0    20150622195754,
            1    A,
            2    2015年6月22日上海市个人非营业性客车额度模拟投标拍卖会,
            3    5000,
            4    75200,
            5    19:30,
            6    20:30,
            7    19:30,
            8    20:00,
            9    20:00,
            10    20:30,
            11    19:57:53,
            12    75508,
            13    75200,
            14    2015-06-22 19:38:31,
            15    93342,
            16    0
            """
            time0 = dt.datetime.now().strftime("%Y%m%d%H%M%S")
            stage1 = "A"
            name2 = "2015年6月22日上海市个人非营业性客车额度模拟投标拍卖会"
            count3 = "5000"
            startprice4 = "75200"
            bidstart5 = "19:30"
            bidend6 = "20:30"
            stageAstart7 = "19:30"
            stageAend8 = "20:00"
            stageBstart9 = "20:00"
            stageBend10 = "20:30"
            servertime11 = daytime(dt.datetime.now())
            people12 = "75508"
            lowbidprice13 = str(lowbidprice)
            lowbidpricetime14 = "2015-06-22 19:38:31"
            cur_pos15 = str(cur_pos)
            unused16 = "0"
            enc_text = "%(time0)s,%(stage1)s,%(name2)s,%(count3)s,%(startprice4)s,%(bidstart5)s,%(bidend6)s,%(stageAstart7)s,%(stageAend8)s,%(stageBstart9)s,%(stageBend10)s,%(servertime11)s,%(people12)s,%(lowbidprice13)s,%(lowbidpricetime14)s,%(cur_pos15)s,%(unused16)s" % locals()
        else:
            """
            0 20150622200243
            1 B
            2 2015年6月22日上海市个人非营业性客车额度模拟投标拍卖会
            3 5000
            4 76865
            5 19:30
            6 20:30
            7 19:30
            8 20:00
            9 20:00
            10 20:30
            11 20:02:42
            12 75400
            13 2015-06-22 20:01:29
            14 75100
            15 75700
            16 107188
            17 0
            """
            time0 = dt.datetime.now().strftime("%Y%m%d%H%M%S")
            stage1 = "B"
            name2 = "结束了"
            count3 = "5000"
            people4 = "75200"
            bidstart5 = "19:30"
            bidend6 = "20:30"
            stageAstart7 = "19:30"
            stageAend8 = "20:00"
            stageBstart9 = "20:00"
            stageBend10 = "20:30"
            servertime11 = daytime(dt.datetime.now())
            lowbidprice12 = str(lowbidprice)
            lowbidpricetime13 = "2015-06-22 20:01:29"
            lowlimit14 = str(lowbidprice - 300)
            uplimit15 = str(lowbidprice + 300)
            cur_pos16 = str(cur_pos)
            unusedd17 = "0"
            enc_text = "%(time0)s,%(stage1)s,%(name2)s,%(count3)s,%(people4)s,%(bidstart5)s,%(bidend6)s,%(stageAstart7)s,%(stageAend8)s,%(stageBstart9)s,%(stageBend10)s,%(servertime11)s,%(lowbidprice12)s,%(lowbidpricetime13)s,%(lowlimit14)s,%(uplimit15)s,%(cur_pos16)s,%(unusedd17)s" % locals()

        return self.head(len(enc_text), 3, 1) + enc_text

    def s2c0302(self):
        self.cal_timestamp()


class MessageCore1024(MessageCore622):
    CLIENT_ID = 'c7e87d4b71544fe4804d5532f192b111'
    template_c2s0000 = '{requestid:"%(requestid)s",timestamp:"%(timestamp)s",bidnumber:"%(bidnumber)s",checkcode:"%(checkcode)s",version:"%(version)s",request:{timespan:"%(timespan)s"}}'
    template_c2s0101 = '{requestid:"%(requestid)s",timestamp:"%(timestamp)s",bidnumber:"%(bidnumber)s",checkcode:"%(checkcode)s",version:"%(version)s"}}'
    template_c2s0201 = '{requestid:"%(requestid)s",timestamp:"%(timestamp)s",bidnumber:"%(bidnumber)s",checkcode:"%(checkcode)s",version:"%(version)s",request:{bidamount:%(bidamount)s}}'
    template_c2s0202 = '{requestid:"%(requestid)s",timestamp:"%(timestamp)s",bidnumber:"%(bidnumber)s",checkcode:"%(checkcode)s",version:"%(version)s",request:{bidamount:"%(bidamount)s",imagenumber:"%(imagenumber)s"}}'

    def cal_requestid(self, bidnumber, timestamp):
        return bidnumber + '.f' + timestamp

    def c2s0101(self, bidnumber, timestamp=None, requestid=None):
        if timestamp is None:
            timestamp = self.cal_timestamp()
        if requestid is None:
            requestid = self.cal_requestid(bidnumber, timestamp)
        checkcode = encutil.one_time_md5(self.CLIENT_ID + timestamp + bidnumber + requestid + self.VERSION)
        version = self.VERSION
        timespan = '0'
        raw_text = self.template_c2s0101 % locals()
        enc_text = self.encdec.enc(raw_text)
        if DEBUG:
            print raw_text
        return self.head(len(enc_text), 1, 1) + enc_text

    def c2s0000(self, bidnumber, timestamp=None, requestid=None):
        if timestamp is None:
            timestamp = self.cal_timestamp()
        if requestid is None:
            requestid = self.cal_requestid(bidnumber, timestamp)
        checkcode = encutil.one_time_md5(bidnumber + self.CLIENT_ID + requestid + timestamp + self.VERSION)
        version = self.VERSION
        timespan = '0'
        raw_text = self.template_c2s0000 % locals()
        enc_text = self.encdec.enc(raw_text)
        if DEBUG:
            print raw_text
        return self.head(len(enc_text), 0, 0) + enc_text

    def c2s0201(self, bidnumber, bidamount, timestamp=None, requestid=None):
        if timestamp is None:
            timestamp = self.cal_timestamp()
        if requestid is None:
            requestid = self.cal_requestid(bidnumber, timestamp)
        checkcode = encutil.one_time_md5(
            self.CLIENT_ID + bidamount + self.CLIENT_ID + timestamp + requestid + self.VERSION + bidnumber)
        version = self.VERSION
        raw_text = self.template_c2s0201 % locals()
        enc_text = self.encdec.enc(raw_text)
        if DEBUG:
            print raw_text
        return self.head(len(enc_text), 2, 1) + enc_text

    def c2s0202(self, bidnumber, bidamount, imagenumber, imageResponcode=0, priceCode='', timestamp=None,
                requestid=None):
        if timestamp is None:
            timestamp = self.cal_timestamp()
        if requestid is None:
            requestid = self.cal_requestid(bidnumber, timestamp)
        bidamount = str(bidamount)
        if priceCode == '':
            checkcode = encutil.one_time_md5(
                bidnumber + bidamount + self.VERSnbcore.encutilelf.VERSION + imagenumber + requestid + self.CLIENT_ID + timestamp)
        elif imageResponcode == 1:
            priceCode = eval(priceCode)
        checkcode = encutil.one_time_md5(
            requestid + self.VERSION + priceCode + timestamp + bidnumber + self.CLIENT_ID + bidamount + imagenumber)
        version = self.VERSION
        raw_text = self.template_c2s0202 % locals()
        enc_text = self.encdec.enc(raw_text)
        if DEBUG:
            print raw_text
        return self.head(len(enc_text), 2, 2) + enc_text

    def s2c0101(self, responsecode, responsemsg,bidamount,
                bidnumber, bidcount, stype, requestid, dealtime):

        lastrequestid = bidnumber + "." + self.cal_timestamp(dt.timedelta(seconds=30))

        bidtime = (dt.datetime.now() - dt.timedelta(seconds=30)).strftime('%Y-%m-%d %H:%M:%S')
        msg = '出价有效'
        bidcount = 1
        servertime = time2str(dt.datetime.now())

        raw_text = self.template_s2c0101 % {
            'responsecode': responsecode,
            'responsemsg': responsemsg,
            'bidamount': bidamount,
            'bidnumber': bidnumber,
            'bidtime': bidtime,
            'msg': msg,
            'bidcount': bidcount,
            'type': stype,
            'lastrequestid': lastrequestid,
            'dealtime': dealtime,
            'requestid': requestid,
            'servertime': servertime
        }

        enc_text = self.encdec.enc(raw_text)
        return self.head(len(enc_text), 1, 1) + enc_text

    """
     template_s2c0203 = '{"response":{"responsecode":%(responsecode)s,"responsemsg":"",' \
                    '"data":{"bidamount":"%(bidamount)s","bidnumber":"%(bidnumber)s",' \
                             '"bidtime":"%(bidtime)s","msg":"%(msg)s","bidcount":%(bidcount)s,' \
                             '"type":%(stype)s,"requestid":"%(requestid)s","code":%(code)s,"dealtime":"%(dealtime)s"}},' \
                    '"requestid":"%(requestid)s","servertime":"%(servertime)s"}'
     """
    def s2c0203(self, responsecode,
                bidamount, bidnumber, bidtime, msg, bidcount, dealtime, requestid, stype="1", code="0"):
        servertime = time2str(dt.datetime.now())
        #测试用
        #print(type(dealtime), dealtime)
        #把后microseconds的后三位截断
        dealtime = str(dealtime)[:-3]

        raw_text = self.template_s2c0203 % locals()
        #print("2-3消息：", raw_text)
        enc_text = self.encdec.enc(raw_text)
        return self.head(len(enc_text), 2, 3) + enc_text




    def s2c0301(self, lowbidprice, cur_pos, stage='B', cur_time=None):
        if cur_time is None:
            cur_time = dt.datetime.now()

        if stage == 'A':
            """
            0    20150622195754,
            1    A,
            2    2015年6月22日上海市个人非营业性客车额度模拟投标拍卖会,
            3    5000,
            4    75200,
            5    19:30,
            6    20:30,
            7    19:30,
            8    20:00,
            9    20:00,
            10    20:30,
            11    19:57:53,
            12    75508,
            13    75200,
            14    2015-06-22 19:38:31,
            15    93342,
            16    0
            """
            """
            time0 = cur_time.strftime("%Y%m%d%H%M%S")
            stage1 = "A"
            name2 = "2015年6月22日上海市个人非营业性客车额度模拟投标拍卖会"
            count3 = "5000"
            startprice4 = "75200"
            bidstart5 = "19:30"
            bidend6 = "20:30"
            stageAstart7 = "19:30"
            stageAend8 = "20:00"
            stageBstart9 = "20:00"
            stageBend10 = "20:30"
            servertime11 = daytime(cur_time)
            people12 = "75508"
            lowbidprice13 = str(lowbidprice)
            lowbidpricetime14 = "2015-06-22 19:38:31"
            cur_pos15 = str(cur_pos)
            unused16 = "0"
            enc_text = "%(time0)s,%(stage1)s,%(name2)s,%(count3)s,%(startprice4)s,%(bidstart5)s,%(bidend6)s,%(stageAstart7)s,%(stageAend8)s,%(stageBstart9)s,%(stageBend10)s,%(servertime11)s,%(people12)s,%(lowbidprice13)s,%(lowbidpricetime14)s,%(cur_pos15)s,%(unused16)s" % locals()
            """
            time0 = cur_time.strftime("%Y%m%d%H%M%S")
            stage1 = "A"
            auctionType2 = "0"
            auctionDate3 = "20180121"
            quota4 = "7763"
            warningPrice5 = "11300"
            priceLowerLimit6 = "100"
            startTime7 = "1030"
            updateTime8 = "1100"
            endTime9 = "1130"
            systemTime10 = cur_time.strftime("%H%M%S")
            numberOfBidUsers11 = "1233433"
            basePrice12 = str(lowbidprice)
            basePriceTime13 = "20150622110229"
            tradeSn14 = str(0)
            queueLength15 = "0"
            enc_text = "%(time0)s,%(stage1)s,%(auctionType2)s,%(auctionDate3)s,%(quota4)s,%(warningPrice5)s,%(priceLowerLimit6)s,%(startTime7)s,%(updateTime8)s,%(endTime9)s,%(systemTime10)s,%(numberOfBidUsers11)s,%(basePrice12)s,%(basePriceTime13)s,%(tradeSn14)s,%(queueLength15)s" % locals()
            # print "liuziyu ~~~~", enc_text


        elif stage == 'B':
            """
            0 20150622200243
            1 B
            2 2015年6月22日上海市个人非营业性客车额度模拟投标拍卖会
            3 5000
            4 76865
            5 19:30
            6 20:30
            7 19:30
            8 20:00
            9 20:00
            10 20:30
            11 20:02:42
            12 75400
            13 2015-06-22 20:01:29
            14 75100
            15 75700
            16 107188
            17 0
            
            0 20151024112955,
            1 B,
            2 0,
            3 2015年10月24日上海市个人非营业性客车额度投标拍卖会,
            4 7763,
            5 170995,
            6 100,
            7 10:30,
            8 11:30,
            9 10:30,
            10 11:00,
            11 11:00,
            12 11:30,
            13 11:29:54,
            14 85100,
            15 2015-10-24 11:29:50,
            16 84800,
            17 85400,
            18 456507,
            19 0

            
            """
            ##            time0 = cur_time.strftime("%Y%m%d%H%M%S")
            ##            stage1 = "B"
            ##            unknow2 = "0"
            ##            name3 = "2017年1月14日上海市个人非营业性客车额度投标拍卖会"
            ##            count4 = "7763"
            ##            people5 = "170995"
            ##            unknow6 = "100"
            ##            bidstart7 = "10:30"
            ##            bidend8 = "11:30"
            ##            stageAstart9 = "10:30"
            ##            stageAend10 = "11:00"
            ##            stageBstart11 = "11:00"
            ##            stageBend12 = "11:30"
            ##            servertime13 = daytime(cur_time)
            ##            lowbidprice14 = str(lowbidprice)
            ##            lowbidpricetime15 = "2015-06-22 20:01:29"
            ##            lowlimit16 = str(lowbidprice-300)
            ##            uplimit17 = str(lowbidprice+300)
            ##            cur_pos18 = str(cur_pos)
            ##            unusedd19 = "0"

            time0 = cur_time.strftime("%Y%m%d%H%M%S")
            stage1 = "B"
            unknow2 = "0"
            aucttionDate3 = "20180121"
            quota4 = "7763"
            numberOfBidUsers5 = "170995"
            priceLowerLimit6 = "100"
            startTime7 = "1030"
            updateTime8 = "1100"
            endTime9 = "1130"
            systemTime10 = cur_time.strftime("%H%M%S")
            basePrice11 = str(lowbidprice)
            basePriceTime12 = "20150622110229"
            var12013 = str(lowbidprice - 300)
            var12114 = str(lowbidprice + 300)
            tradeSn15 = str(cur_pos)
            queueLength16 = "0"

            ##            enc_text = "%(time0)s,%(stage1)s,%(unknow2)s,%(name3)s,%(count4)s,%(people5)s,%(unknow6)s,%(bidstart7)s,%(bidend8)s,%(stageAstart9)s,%(stageAend10)s,%(stageBstart11)s,%(stageBend12)s,%(servertime13)s,%(lowbidprice14)s,%(lowbidpricetime15)s,%(lowlimit16)s,%(uplimit17)s,%(cur_pos18)s,%(unusedd19)s"%locals()

            enc_text = "%(time0)s,%(stage1)s,%(unknow2)s,%(aucttionDate3)s,%(quota4)s,%(numberOfBidUsers5)s,%(priceLowerLimit6)s,%(startTime7)s,%(updateTime8)s,%(endTime9)s,%(systemTime10)s,%(basePrice11)s,%(basePriceTime12)s,%(var12013)s,%(var12114)s,%(tradeSn15)s,%(queueLength16)s" % locals()
            #print "liuziyu ~~~~", enc_text

        #7李帅新加代码
        #E,H消息暂时不知何用，是拍牌前的界面
        elif stage == 'C' or stage == 'E' or stage == 'H':
            time0 = cur_time.strftime("%Y%m%d%H%M%S")
            stage1 = "C"
            content2 = "没有正在举行的拍卖会，请注意拍卖公告！查询请到WWW.ALLTOBID.COM"
            enc_text = "%(time0)s,%(stage1)s,%(content2)s," % locals()

        elif stage == 'D':
            time0 = cur_time.strftime("%Y%m%d%H%M%S")
            stage1 = "D"
            content2 = ("""
2017年11月18日上海市个人非营业性客车额度投标拍卖会结果公布
参加拍卖人数：226911
最低成交价：93100
最低成交价的截止时间：11:29:59 第1025位
平均成交价：93130
请拍卖成交的买受人在11月19日～25日(9:00-16:00)到下列服务点办理成交付款手续。
1.长宁区淞虹路938号（福缘湾九华商业广场地下1层A2）
2.共和新路3550号（百联汽车广场）
3.东江湾路444号（虹口足球场4区113）
4.新镇路288号（闵行体育馆架空层B2区）
5.新村路1500号1层107（家乐福上海万里店内）
6.浦东成山路800号（云顶国际商业广场A座101）
注：福州路108号（公司本部）不办理成交付款结算手续
另：我公司网站已开通网上支付结算，大家可登录查询。
            
            """)
            tradeSn3 = str(cur_pos)     #tradeSn15 = str(cur_pos)
            queueLength4 = "0"
            enc_text = ("%(time0)s,%(stage1)s,%(content2)s,%(tradeSn3)s,%(queueLength4)s") % locals()
            #print "stage == D", enc_text

        elif stage == 'F':
            time0 = cur_time.strftime("%Y%m%d%H%M%S")
            stage1 = "F"
            auctionType2 = "0"
            auctionDate3 = "20180121"
            startTime4 = '1030'
            endTime5 = '1130'
            systemTime6 = cur_time.strftime("%H%M%S")

            enc_text = ("%(time0)s,%(stage1)s,%(auctionType2)s,%(auctionDate3)s,%(startTime4)s,"
                        "%(endTime5)s,%(systemTime6)s") % locals()
            #print "stage == D", enc_text


        elif stage == 'G':
            time0 = cur_time.strftime("%Y%m%d%H%M%S")
            stage1 = "G"
            auctionType2 = "0"
            auctionDate3 = "20180121"
            content4 = """稍后发布拍卖会结果，请等待！

拍卖会结果也可通过本公司网站、微信公众号进行查询，网址：www.alltobid.com，微信公众号：shanghaiguopai
"""
            tradeSn5 = str(cur_pos)  #tradeSn15 = str(cur_pos)
            queueLength6 = "0"
            enc_text = ("%(time0)s,%(stage1)s,%(auctionType2)s,%(auctionDate3)s,%(content4)s,"
                        "%(tradeSn5)s,%(queueLength6)s") % locals()
            #print "stage == G", enc_text



        enc_text = enc_text.decode('utf-8')
        mixed_text = encutil.remix_msg(enc_text, self.msg_decode_len)
        #         print len(mixed_text),mixed_text
        #         print len(enc_nbcore.encutilnc_text

        mixed_text = mixed_text.encode('utf-8')
        return self.head(len(mixed_text), 3, 1) + mixed_text


class MessageCore1121(MessageCore1024):
    pass


def test():
    print ord("abc"[0])
    print len(str(u"abc"))
    mc = MessageCore622()

    print mc.s2c0101(0, '建立成功', 100, '12345678', 1, 1, '12345678.193925477')[10:]


def test2():
    global DEBUG
    DEBUG = True
    mc = MessageCoreFactory.create_message_core('1121')
    mc.c2s0101('12345678', timestamp='151312311', requestid='12345678.f151312311')
    print '{requestid:"12345678.f151312311",timestamp:"151312311",bidnumber:"12345678",checkcode:"cde52b1e38d8ababfad2d9f3beb75f85",version:"1.0"}'
    mc.c2s0000('12345678', timestamp='151322371', requestid='12345678.f151322371')
    print '{requestid:"12345678.f151322371",timestamp:"151322371",bidnumber:"12345678",checkcode:"7a62cac0c9719f859dff866526c6b0c8",version:"1.0",request:{timespan:"0"}}'
    mc.c2s0201('12345678', '84100', timestamp='15141222', requestid='12345678.f15141222')
    print '{requestid:"12345678.f15141222",timestamp:"15141222",bidnumber:"12345678",checkcode:"4f92ec2eaa494191f23641a1a60e2273",version:"1.0",request:{bidamount:84100}}'
    mc.c2s0202('12345678', '84100', '1234', imageResponcode=0, priceCode='9b9', timestamp='15144759',
               requestid='12345678.f15144759')
    print '{requestid:"12345678.f15144759",timestamp:"15144759",bidnumber:"12345678",checkcode:"7821546a99b7974a7b0750e38d8ea233",version:"1.0",request:{bidamount:"84100",imagenumber:"1234"}}'


if __name__ == "__main__": test2()
