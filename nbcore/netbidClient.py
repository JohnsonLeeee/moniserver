from netbid import *

class MessageCore160220(MessageCore1121):
    def c2s0101(self, bidnumber, timestamp = None, requestid = None):
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

    
    def c2s0000(self, bidnumber, timestamp = None, requestid = None):
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

    
    def c2s0201(self, bidnumber, bidamount, timestamp = None, requestid = None):
        if timestamp is None:
            timestamp = self.cal_timestamp()
        if requestid is None:
            requestid = self.cal_requestid(bidnumber, timestamp)
        checkcode = encutil.one_time_md5(self.CLIENT_ID + bidamount + self.CLIENT_ID + timestamp + requestid + self.VERSION + bidnumber)
        version = self.VERSION
        raw_text = self.template_c2s0201 % locals()
        enc_text = self.encdec.enc(raw_text)
        if DEBUG:
            print raw_text
        return self.head(len(enc_text), 2, 1) + enc_text

    
    def c2s0202(self, bidnumber, bidamount, imagenumber, imageResponcode = 0, priceCode = '', timestamp = None, requestid = None):
        if timestamp is None:
            timestamp = self.cal_timestamp()
        if requestid is None:
            requestid = self.cal_requestid(bidnumber, timestamp)
        bidamount = str(bidamount)
        if priceCode == '':
            checkcode = encutil.one_time_md5(bidnumber + bidamount + self.VERSnbcore.encutilelf.VERSION + imagenumber + requestid + self.CLIENT_ID + timestamp)
        elif imageResponcode == 1:
            priceCode = eval(priceCode)
        checkcode = encutil.one_time_md5(requestid + self.VERSION + priceCode + timestamp + bidnumber + self.CLIENT_ID + bidamount + imagenumber)
        version = self.VERSION
        raw_text = self.template_c2s0202 % locals()
        enc_text = self.encdec.enc(raw_text)
        if DEBUG:
            print raw_text
        return self.head(len(enc_text), 2, 2) + enc_text