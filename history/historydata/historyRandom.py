# -*- coding: utf-8 -*-
import time
import random
from history201712 import History201712


class HistoryRandom(History201712):
    bid_people = random.randint(200000, 300000)
    title = "随机模拟"
    cards = random.randint(8000, 15000)
    IMAGE_CODES = [
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
                    ["2972","输入苹果行的四位数字校验码","http://51moni-sh.oss-cn-shanghai.aliyuncs.com/yzm1710/b7650~a2972.png?id=cf920e81-4a73-4e69-beea-bdcd3929abcb&i=2b4ca06b3f1790e1a232dba065ffda3f"]
                  ]

    def __init__(self):
        self.lowbidprice = 86300

    def getLowPrice(self, mock_time):
        if mock_time.hour == 11 and mock_time.minute == 29:
            if random.randint(0, 3) == 0:
                self.lowbidprice += 100
        return self.lowbidprice
        
