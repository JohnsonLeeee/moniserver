# -*- coding: utf-8 -*-
import base64 as b64
import hashlib as hl
import struct  
import math

def one_time_md5(s):
    m = hl.md5()
    m.update(s)
    return m.hexdigest()
    
class EncDec(object):
    
    def __init__(self,config):
        self.tea = XXTEA(config['s1'],config['s2'],config['s3'],config['s4'])
        self.key = config['key']
                
    def enc(self,raw_text):
        s1 = b64.b64encode(raw_text)
        s2 = self.tea.encrypt(s1, self.key)
        return b64.b64encode(s2)
        
    
    def dec(self,enc_text):
        s1 = b64.b64decode(enc_text)
        s2 = self.tea.decrypt(s1, self.key)
        return b64.b64decode(s2)
    
class XXTEA(object):
    #this is for 6-22 netbid
    
    #622 5 2 3 4
    #1024 4 2 3 5
    _DELTA = 0x9E3779B9
    def __init__(self, s1,s2,s3,s4):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
    
    def _long2str(self,v, w):  
        n = (len(v) - 1) << 2  
        if w:  
            m = v[-1]  
            if (m < n - 3) or (m > n): return ''  
            n = m  
        s = struct.pack('<%iL' % len(v), *v)  
        return s[0:n] if w else s  
      
    def _str2long(self,s, w):  
        n = len(s)  
        m = (4 - (n & 3) & 3) + n  
        s = s.ljust(m, "\0")  
        v = list(struct.unpack('<%iL' % (m >> 2), s))  
        if w: v.append(n)  
        return v  
      
    def encrypt(self,str, key):  
        if str == '': return str  
        v = self._str2long(str, True)  
        k = self._str2long(key.ljust(16, "\0"), False)  
        n = len(v) - 1  
        z = v[n]  
        y = v[0]  
        sum = 0  
        q = 6 + 52 // (n + 1)  
        while q > 0:  
            sum = (sum + XXTEA._DELTA) & 0xffffffff  
            e = sum >> 2 & 3  
            for p in xrange(n):  
                y = v[p + 1]  
                v[p] = (v[p] + ((z >> self.s1 ^ y << self.s2) + (y >> self.s3 ^ z << self.s4) ^ (sum ^ y) + (k[p & 3 ^ e] ^ z))) & 0xffffffff  
                z = v[p]  
            y = v[0]  
            v[n] = (v[n] + ((z >> self.s1 ^ y << self.s2) + (y >> self.s3 ^ z << self.s4) ^ (sum ^ y) + (k[n & 3 ^ e] ^ z))) & 0xffffffff  
            z = v[n]  
            q -= 1  
        return self._long2str(v, False)  
      
    def decrypt(self,str, key):  
        if str == '': return str  
        v = self._str2long(str, False)  
        k = self._str2long(key.ljust(16, "\0"), False)  
        n = len(v) - 1  
        z = v[n]  
        y = v[0]  
        q = 6 + 52 // (n + 1)  
        sum = (q * XXTEA._DELTA) & 0xffffffff  
        while (sum != 0):  
            e = sum >> 2 & 3  
            for p in xrange(n, 0, -1):  
                z = v[p - 1]  
                v[p] = (v[p] - ((z >> self.s1 ^ y << self.s2) + (y >> self.s3 ^ z << self.s4) ^ (sum ^ y) + (k[p & 3 ^ e] ^ z))) & 0xffffffff  
                y = v[p]  
            z = v[n]  
            v[0] = (v[0] - ((z >> self.s1 ^ y << self.s2) + (y >> self.s3 ^ z << self.s4) ^ (sum ^ y) + (k[0 & 3 ^ e] ^ z))) & 0xffffffff  
            y = v[0]  
            sum = (sum - XXTEA._DELTA) & 0xffffffff  
        return self._long2str(v, True)  


def hex2str(hex_str):
    s = []
    for i in range(0,len(hex_str),2):
        h = hex_str[i:i+2]
        s.append(chr(int(h,16)))
        
    return "".join(s)
        

def test():
    data = "pkPb0qJmRLvDmtlxX2reFzLyZd+6+qgQQJptbVj5EBktizufIjfzw8ADU7/EGmkglk3thkZ31OPbBqeNYaaTu/82FG1Lo+ScSnyYQZBDa986BmQWzOwW99RbjvpFhDD6XgQmPpItsFtJ1Xq9g45Ip5CnVQP6UwrzmOgyeBraCW48S7W0KAMvhW1aIVx+fWxUXn13855+gu6xo5F0GP535w0aIjIe4f8s15Rl7veJaNcBl8cKOWko3Tn7aCAu08uoH933n7/dllHNaMONwr8jcmv1AkjLgZjw"
    d2 = "cR0YVyElBxBjHrUchiVDEA+kafCU4YkqLEvhifwWMuJtqPsdtswLQwmzZzwTfuMPv6s5LOY3Qui2/qgF3nI+87L9NpO9TMjcO17CTzSbNN+8nRBShimNQZRmPrYrSq44hjoIY33pI0b3OS155u5nmDz8Xyj73hJ7YIeB9PnGUNOO+xmi4HC3dmL/RCbxYsbD2nHmKRXNeGB7MFGXUOtHKhocGvlpyF+u2Boc14jyMCnyFMoq"
    print one_time_md5("test")
    print ord(str("你")[0]),ord(str("你")[1]),ord(str("你")[2])
    
    tea = XXTEA()
    a = tea.encrypt('test', 'abc')
    print tea.decrypt(a, 'abc')
    
    ed = EncDec("shcarbid")
    print ed.dec(d2)

def test2():
    t = "000000ce0301000000c432303135303632323230303234332c422c32303135e5b9b436e69c883232e697a5e4b88ae6b5b7e5b882e4b8aae4babae99d9ee890a5e4b89ae680a7e5aea2e8bda6e9a29de5baa6e6a8a1e68b9fe68a95e6a087e68b8de58d96e4bc9a2c353030302c37363836352c31393a33302c32303a33302c31393a33302c32303a30302c32303a30302c32303a33302c32303a30323a34322c37353430302c323031352d30362d32322032303a30313a32392c37353130302c37353730302c3130373138382c30"
    print hex2str(t[20:])
    
    ed = EncDec("shcarbid")
    
    t2 = "00012a00000000012049702b504533792f684b31652f6437376b45526c6576563474355778596c587a38534e716b6b734e58596d39414963623439416b46426a343444714267515231337270373030534e7a4552354a48774d684c31776f38697962725347594d376c4e4c432f4e364a477a366f524a596f52627650726b35435931485076444864554f6770577574365a6f7147742b51364356345650316c6631764f66425a49442f765264476e6836576d333248676e6f70417773627a734441743236456d6d6739313771516e365838324e5548423578575546777354516e6136643443724451556532727a317450787033334d3934334773746a73537752665a53426d365234384838634a54326839446578686d6c30464b6a6d2b41732f506c583646764b6f74"
    h2 = "Ip+PE3y/hK1e/d77kERlevV4t5WxYlXz8SNqkksNXYm9AIcb49AkFBj44DqBgQR13rp700SNzER5JHwMhL1wo8iybrSGYM7lNLC/N6JGz6oRJYoRbvPrk5CY1HPvDHdUOgpWut6ZoqGt+Q6CV4VP1lf1vOfBZID/vRdGnh6Wm32HgnopAwsbzsDAt26Emmg917qQn6X82NUHB5xWUFwsTQna6d4CrDQUe2rz1tPxp33M943GstjsSwRfZSBm6R48H8cJT2h9Dexhml0FKjm+As/PlX6FvKot"
    
    print ed.dec(h2)
    
    h3 = "IPtz5zuci14+wYVZGdczfXpaFwTvBn1iWIvdpweewZ4FIPSqrIi3nexrLAxvAjDChFREJjMsOaVhN1iVnnH2UqIbF1W41aajl8FP3Rs49lQq3SyttUjCxV0+wkNlD0fHALoTs+/yvkCFIVTugr55fxZTtUeDqYfhu+SY7T9U5xTsF5grgtt7SsrZvZxOWmztRD0XtCfhqzQVzx/LFg5uaaW8/GEVHHgNVX++jtI1FVEvi9sTkFs6UPeUi/TfD1srB8G73BZ9tri56L/DWeH9CNcnf63IILF0"
    
    print ed.dec(h3)
    
def test3():
    #622 5 2 3 4
    #1024 4 2 3 5
    t = "0000012a00000000012050725a364c52366c33582b5a413430594b3836424c6f493473396b364b664b386446655366354b623061334371626d4937774d334471416f714b4a6d3478336353734d4a434d7751716d76597576566261665137396f415556516c415a6c396469434b38537130595736346e597238354c6561513064366842342b732f6f784e6b3532353530786f4f4b435a37486c594f314c65486c7466657a66687356324b794a37307a2f47782b3454685470714663586753747859734d48717545654254454c7244434e4669536b4c6169494633645357434b5153564d6b47357472783770394a5845685a58326367436e686955714f526555626c56635a347062454c657674344d75756e496b66442b31736a67426e364138543548556b53556b7a2f67"
    h = hex2str(t[20:])
    print h
    config = {'s1':4,'s2':2,'s3':3,'s4':5,'key':'gp[p&m)'[2:2+5]}
    enc = EncDec(config)
    print enc.dec(h)
    
def test4():
    
    t = "2cb05da56c116002b4955ab108004500015a413e400040069df30a000006de49721d11d6206c9a6c315aaa08525f50184380421e0000000001320201000001284d6a396250535877746d374438744f49624f2b785564636f61523967384a752f3465595a49645439385a633333494e644f72655662562f3978455950654d763349644b625078517748516f6d4f6c475a5933565768544f39767359326b41626a6c66677a544c565739636f657437725150614867547a48306d747470792b59627965596c794a46624571566c70304b37367a6e7a7874445a31456e586a754a614e51346a7a632b4b4f64397361505a76454d75716a694c48676746436b5671315252786678496373437543534b45553969554146696a337634746f2b6c5975344f7a537041516f347565504b4f7a68565a54616d4f317863342f68494f37674b36665a723035684e72717343537363616753524933696568687561354f566e5135736d6656773d3d"
    h = hex2str(t[4*16*2:])
    print h
    config = {'s1':4,'s2':2,'s3':3,'s4':5,'key':'gp[p&m)'[2:2+5]}
    enc = EncDec(config)
    print enc.dec(h)
    
    t2 = "6002b4955ab12cb05da56c1108004500022a45af4000770661b2de49721d0a000006206c11d6aa08525f9a6c328c5018fbeeeff40000000002020201000001f8346b483255374b527068715a673078434b4a66726e4b373548764c337634363854385a55797a77687967355133306249694f4c747a324c2b386e543467344754723266566e774c6c727861646c6a75314651447276367973756b34772b7050546d4445794947682f65394f44575031374f715345536c2b4151434c2f6f473839344655524637625469314e366c5254786b525157446e6731573538794555617a6835745357466e2f4670512b6d46446f4e316574774a4779744c437036674c35424177713233307930596c635070634d505555636c614d757a7831632b6a424f48536c372f3557493353484c544d33476a6c315a414371527a766a45613333454a7458496d6c654c53482f625634645639665666484a4934423870702b6b395033334b4f5544717a4a723776736e584a555a676d51546c743555794d654d4654382b4733656d4436777867396958526a6a4c586e473343392b426a4f74313976624f5554437a6f307836646a59696d6d3877665569684c74442b5467665a44617972315669733164537535675857667a6570363548466d347a796c5972534a724d62336e5878486843456c53527966746a6c724d4d386e52645255575044546a666a4e4b396941496a676979524a35596f412b4f797561502f4b4850347644546374775466756c75367377374f6864574b68554c69773d3d"
    h2 = hex2str(t2[4*16*2:])
    print enc.dec(h2)
    
    t3 = "2cb05da56c116002b4955ab108004500017a4297400040069c7a0a000006de49721d11d6206c9a6c33b6aa085d7250183e8e259e000000000152020200000148484c6555434e494e324b374d33462b4546386e727066795778784a4556672f354d487635347a65422b44536156544b64367a79616d536e4a2b317a4f627944663257577047536874537947544f382b792b784c4f61456b6a51626b55514e464c714f77354139492f565770496855504f51544b442f555a5a4b577866436e686e325634364b734a586936546d7a4e396330786d34336677414d726f386e496b427a37675366386c446b434270636834594c464471624e557341774a79307a4e6a50656b484772766838725444707130776d32516756473055596a31716f436b554256416b6c4e4952784b716863394b79763349444c4d32443538784b2f4d61306a70384e616f424d734e627941735a6b4969657677744c6a44364133346964427737723158704b745563534764324368474e3247643352356f43496e684c56497761375442773d3d"
    h3 = hex2str(t3[4*16*2:])
    print enc.dec(h3)
    
    t4 = "6002b4955ab12cb05da56c110800450002be3174400077067559de49721d0a000006206c11d6aa085d729a6c35085018f972ee0000000000029602020000028c4a4c5274674d514d507354313735615176676a6d646d6763684e326841526574464b63453552544854316e594d545a314977654678672f4a4b6a617275347a372b6569734f7855706e726c37556f47657068727234662f347179676c707044324e636e4e3553644c564559633936487a41444152597376597842313733466b68444e2b726431444f6f4e397367654b323664452b574d4d6b456e75507356336c486c756e38504b534941636d7670684e6857496a37517a5473656a495a3975536d644e495275616d523843664c546338526d517a48724e347144676e44566973595a6348544b42645a4d6d2f496e4164516c4b594d6950742f5357337759485761625a7a2b44734854355a4d39442b5779324b504c49346c455133552b5845496367746f574a474d3873445454636e69386739466e7a714b6639504b6e4e4550704949694a5670323464754473444257766c794477624151566e707a507430566d754d554c30796e4c41744569427772675876677830682b6f61476f495242367a72306d64575a597a3442416d4e4d4f446148553879745353597a7749335a5454416d554d426e7439443970386c73477466547564514f6c3445367477696a3174586c38547339796a676b326a4472622f515859783543456a37744932524c7331554b52616c5a742b724e53667861794d6e4a336f416669326c6f69497634376a444b72504c303931764c5074427a74617170693850514e32794a793765653662722f3361577a536a2f5153354771725631486459745a766f78446d674b35657256317466416a586a764b795a6879576f4d76486e4b5a43356863684441515575466c65624b2b415a7471565a44477a424d6141412f77425363674965534d4f682f71705864744f7364633d"
    
    print dtotal(t4)
    
    t = "6002b4955ab12cb05da56c110800450000fb1dc8400077068ac8de49721d0a000006206c11d6aa085c9f9a6c33b65018fac4c81a0000000000d30301000000c932312c31e5b882e8bda62c302c31332c3132312d3138343030313030e4b8aae9a29d3739313a30313a3930313a34303731322ce69c88e4babae5baa6373930332c31333a30303238302c35393232e99d9ee68a9536353a30313a30352c2d39302c3031353034e890a5e6a087332c332c31302c3432323a303420303531e697a5e4b89ae68b8d2c3130313a30312c3034352c3520322c35e4b88ae680a7e58d9631302c30302c31383120303836203442e5b9b4e6b5b7e5aea2e4bc9a3730313a30313a3535312c3535"
    decoded =  demix_msg(hex2str(t[4*16*2:]).decode('utf-8'))
    print decoded
    decoded = "20151106175636,B,0,2015年10月24日上海市个人非营业性客车额度投标拍卖会,7763,170995,100,10:30,11:30,10:30,11:00,11:00,11:30,17:56:36,82800,2015-06-22 20:01:29,82500,83100,281,0"
    decoded = decoded.decode('utf-8')
    decoded2 =  remix_msg(decoded)
    print decoded2

    
    
def remix_msg(msg,cols=8):
    msg_len = len(msg)
    remain = msg_len % cols
    if remain != 0:
        msg_len += cols - remain
        msg += " "*(cols-remain)
    
    buff = [" "]*msg_len
    
    rows = msg_len / cols
    for idx,m in enumerate(msg):
        row = idx // cols
        col = idx % cols
        buff[col * rows + row] = msg[idx]
    
    return "".join(buff)

def demix_msg(mixed_msg,rows = 8):
    #把长度切分为8个元素一行，然后行列交换
    
    msg_len = len(mixed_msg)
    
    reaming_len = msg_len % rows
    if  reaming_len!= 0:
        msg_len = msg_len + rows - reaming_len;
    
    buff = [None]*msg_len
    cols = msg_len / rows;
    row = 0;
    
    
    while row < rows:
        col = 0;
        while col < cols:
            if row * cols + col < len(mixed_msg):
                #core exchange
                buff[col * rows + row] = mixed_msg[row * cols + col]
            else:
                #超出部分填入空格
                buff[row + rows * col] = " "
          
            col+=1
        row+=1
    
    while buff[msg_len - 1] == " ":
        msg_len-=1
       
    outputStr = ""
    _loc6_ = 0;
    
    while _loc6_ < msg_len:
        outputStr = outputStr + buff[_loc6_]
        _loc6_+=1
       
    return outputStr;

def dtotal(hex_str):
    config = {'s1':4,'s2':2,'s3':3,'s4':5,'key':'gp[p&m)'[2:2+5]}
    enc = EncDec(config)
    h = hex2str(hex_str[4*16*2:])
    return enc.dec(h)

def test5():
    print one_time_md5('0001111222334455567789aachiiiiilmnpuuuyz')
    
if __name__ == "__main__":test4()