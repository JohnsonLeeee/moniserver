# -*- coding: utf-8 -*-
import datetime
import random


class History201712 :
    auction_date = datetime.datetime(2017, 12, 16)
    bid_people = 228148
    title = "2017年12月16日"
    cards = 12147
    warning_price = 91700
    IMAGE_CODES = [
                        
                        ["2041","输入香蕉行的四位数字校验码","yzm1712/a0143~b2041.png"],
                        ["0143","输入苹果行的四位数字校验码","yzm1712/a0143~b2041.png"],
                        ["9156","输入香蕉行的四位数字校验码","yzm1712/a1725~b9156.png"],
                        ["1725","输入苹果行的四位数字校验码","yzm1712/a1725~b9156.png"],
                        ["4187","输入香蕉行的四位数字校验码","yzm1712/a2325~b4187.png"],
                        ["2325","输入苹果行的四位数字校验码","yzm1712/a2325~b4187.png"],
                        ["7839","输入香蕉行的四位数字校验码","yzm1712/a8064~b7839.png"],
                        ["8064","输入苹果行的四位数字校验码","yzm1712/a8064~b7839.png"],
                        ["1174","输入香蕉行的四位数字校验码","yzm1712/b1174~a6972.png"],
                        ["6972","输入苹果行的四位数字校验码","yzm1712/b1174~a6972.png"],
                        ["1292","输入香蕉行的四位数字校验码","yzm1712/b1292~a2046.png"],
                        ["2046","输入苹果行的四位数字校验码","yzm1712/b1292~a2046.png"],
                        ["1358","输入香蕉行的四位数字校验码","yzm1712/b1358~a2414.png"],
                        ["2414","输入苹果行的四位数字校验码","yzm1712/b1358~a2414.png"],
                        ["1685","输入香蕉行的四位数字校验码","yzm1712/b1685~a6560.png"],
                        ["6560","输入苹果行的四位数字校验码","yzm1712/b1685~a6560.png"],
                        ["2699","输入香蕉行的四位数字校验码","yzm1712/b2699~a2138.png"],
                        ["2138","输入苹果行的四位数字校验码","yzm1712/b2699~a2138.png"],
                        ["3647","输入香蕉行的四位数字校验码","yzm1712/b3647~a7858.png"],
                        ["7858","输入苹果行的四位数字校验码","yzm1712/b3647~a7858.png"],
                        ["3700","输入香蕉行的四位数字校验码","yzm1712/b3700~a0611.png"],
                        ["0611","输入苹果行的四位数字校验码","yzm1712/b3700~a0611.png"],
                        ["3853","输入香蕉行的四位数字校验码","yzm1712/b3853~a1240.png"],
                        ["1240","输入苹果行的四位数字校验码","yzm1712/b3853~a1240.png"],
                        ["4061","输入香蕉行的四位数字校验码","yzm1712/b4061~a2078.png"],
                        ["2078","输入苹果行的四位数字校验码","yzm1712/b4061~a2078.png"],
                        ["7685","输入香蕉行的四位数字校验码","yzm1712/b7685~a7796.png"],
                        ["7796","输入苹果行的四位数字校验码","yzm1712/b7685~a7796.png"],
                        ["0011","输入画圈的四位数字","yzm1712/c0011.png"],
                        ["1656","输入画圈的四位数字","yzm1712/c1656.png"],
                        ["1660","输入画圈的四位数字","yzm1712/c1660.png"],
                        ["1957","输入画圈的四位数字","yzm1712/c1957.png"],
                        ["3651","输入画圈的四位数字","yzm1712/c3651.png"],
                        ["4883","输入画圈的四位数字","yzm1712/c4883.png"],
                        ["5901","输入画圈的四位数字","yzm1712/c5901.png"],
                        ["6214","输入画圈的四位数字","yzm1712/c6214.png"],
                        ["6475","输入画圈的四位数字","yzm1712/c6475.png"],
                        ["9675","输入画圈的四位数字","yzm1712/c9675.png"],
                        ["1184","输入西瓜行的四位数字校验码","yzm1712/w1184~s1020.png"],
                        ["1020","输入草莓行的四位数字校验码","yzm1712/w1184~s1020.png"],
                        ["1878","输入西瓜行的四位数字校验码","yzm1712/w1878~s1933.png"],
                        ["1933","输入草莓行的四位数字校验码","yzm1712/w1878~s1933.png"],
                        ["4894","输入西瓜行的四位数字校验码","yzm1712/w4894~s8649.png"],
                        ["8649","输入草莓行的四位数字校验码","yzm1712/w4894~s8649.png"],
                        ["7614","输入西瓜行的四位数字校验码","yzm1712/w7614~s1222.png"],
                        ["1222","输入草莓行的四位数字校验码","yzm1712/w7614~s1222.png"],
                        ["7717","输入西瓜行的四位数字校验码","yzm1712/w7717~s2558.png"],
                        ["2558","输入草莓行的四位数字校验码","yzm1712/w7717~s2558.png"],
                        ["7854","输入西瓜行的四位数字校验码","yzm1712/w7854~s2086.png"],
                        ["2086","输入草莓行的四位数字校验码","yzm1712/w7854~s2086.png"],

                        ["0036","请输入第1到第4位图像校验码","yzm1712/003617.png"],
                        ["0361","请输入第2到第5位图像校验码","yzm1712/003617.png"],
                        ["3617","请输入第3到第6位图像校验码","yzm1712/003617.png"],
                        ["0212","请输入第1到第4位图像校验码","yzm1712/021235.png"],
                        ["2123","请输入第2到第5位图像校验码","yzm1712/021235.png"],
                        ["1235","请输入第3到第6位图像校验码","yzm1712/021235.png"],
                        ["0366","请输入第1到第4位图像校验码","yzm1712/036648.png"],
                        ["3664","请输入第2到第5位图像校验码","yzm1712/036648.png"],
                        ["6648","请输入第3到第6位图像校验码","yzm1712/036648.png"],
                        ["0377","请输入第1到第4位图像校验码","yzm1712/037743.png"],
                        ["3774","请输入第2到第5位图像校验码","yzm1712/037743.png"],
                        ["7743","请输入第3到第6位图像校验码","yzm1712/037743.png"],
                        ["0603","请输红色数字图像校验码","yzm1712/0603.png"],
                        ["0977","请输入第1到第4位图像校验码","yzm1712/097739.png"],
                        ["9773","请输入第2到第5位图像校验码","yzm1712/097739.png"],
                        ["7739","请输入第3到第6位图像校验码","yzm1712/097739.png"],
                        ["1004","请输入第1到第4位图像校验码","yzm1712/100479.png"],
                        ["0047","请输入第2到第5位图像校验码","yzm1712/100479.png"],
                        ["0479","请输入第3到第6位图像校验码","yzm1712/100479.png"],
                        ["1086","请输红色数字图像校验码","yzm1712/1086.png"],
                        ["1087","请输入第1到第4位图像校验码","yzm1712/108791.png"],
                        ["0879","请输入第2到第5位图像校验码","yzm1712/108791.png"],
                        ["8791","请输入第3到第6位图像校验码","yzm1712/108791.png"],
                        ["1089","请输入第1到第4位图像校验码","yzm1712/108941.png"],
                        ["0894","请输入第2到第5位图像校验码","yzm1712/108941.png"],
                        ["8941","请输入第3到第6位图像校验码","yzm1712/108941.png"],
                        ["1096","请输入第1到第4位图像校验码","yzm1712/109609.png"],
                        ["0960","请输入第2到第5位图像校验码","yzm1712/109609.png"],
                        ["9609","请输入第3到第6位图像校验码","yzm1712/109609.png"],
                        ["1134","请输红色数字图像校验码","yzm1712/1134.png"],
                        ["1185","请输入第1到第4位图像校验码","yzm1712/118581.png"],
                        ["1858","请输入第2到第5位图像校验码","yzm1712/118581.png"],
                        ["8581","请输入第3到第6位图像校验码","yzm1712/118581.png"],
                        ["1207","请输入第1到第4位图像校验码","yzm1712/120749.png"],
                        ["2074","请输入第2到第5位图像校验码","yzm1712/120749.png"],
                        ["0749","请输入第3到第6位图像校验码","yzm1712/120749.png"],
                        ["1214","请输入第1到第4位图像校验码","yzm1712/121449.png"],
                        ["2144","请输入第2到第5位图像校验码","yzm1712/121449.png"],
                        ["1449","请输入第3到第6位图像校验码","yzm1712/121449.png"],
                        ["1243","请输入第1到第4位图像校验码","yzm1712/124327.png"],
                        ["2432","请输入第2到第5位图像校验码","yzm1712/124327.png"],
                        ["4327","请输入第3到第6位图像校验码","yzm1712/124327.png"],
                        ["1329","请输入第1到第4位图像校验码","yzm1712/132949.png"],
                        ["3294","请输入第2到第5位图像校验码","yzm1712/132949.png"],
                        ["2949","请输入第3到第6位图像校验码","yzm1712/132949.png"],
                        ["1332","请输入第1到第4位图像校验码","yzm1712/133243.png"],
                        ["3324","请输入第2到第5位图像校验码","yzm1712/133243.png"],
                        ["3243","请输入第3到第6位图像校验码","yzm1712/133243.png"],
                        ["1362","请输入第1到第4位图像校验码","yzm1712/136200.png"],
                        ["3620","请输入第2到第5位图像校验码","yzm1712/136200.png"],
                        ["6200","请输入第3到第6位图像校验码","yzm1712/136200.png"],
                        ["1368","请输红色数字图像校验码","yzm1712/1368.png"],
                        ["1380","请输入第1到第4位图像校验码","yzm1712/138092.png"],
                        ["3809","请输入第2到第5位图像校验码","yzm1712/138092.png"],
                        ["8092","请输入第3到第6位图像校验码","yzm1712/138092.png"],
                        ["1395","请输入第1到第4位图像校验码","yzm1712/139549.png"],
                        ["3954","请输入第2到第5位图像校验码","yzm1712/139549.png"],
                        ["9549","请输入第3到第6位图像校验码","yzm1712/139549.png"],
                        ["1401","请输入第1到第4位图像校验码","yzm1712/140193.png"],
                        ["4019","请输入第2到第5位图像校验码","yzm1712/140193.png"],
                        ["0193","请输入第3到第6位图像校验码","yzm1712/140193.png"],
                        ["1411","请输入第1到第4位图像校验码","yzm1712/141151.png"],
                        ["4115","请输入第2到第5位图像校验码","yzm1712/141151.png"],
                        ["1151","请输入第3到第6位图像校验码","yzm1712/141151.png"],
                        ["1450","请输入第1到第4位图像校验码","yzm1712/145088.png"],
                        ["4508","请输入第2到第5位图像校验码","yzm1712/145088.png"],
                        ["5088","请输入第3到第6位图像校验码","yzm1712/145088.png"],
                        ["1466","请输入第1到第4位图像校验码","yzm1712/146681.png"],
                        ["4668","请输入第2到第5位图像校验码","yzm1712/146681.png"],
                        ["6681","请输入第3到第6位图像校验码","yzm1712/146681.png"],
                        ["1479","请输红色数字图像校验码","yzm1712/1479.png"],
                        ["1499","请输红色数字图像校验码","yzm1712/1499.png"],
                        ["1594","请输红色数字图像校验码","yzm1712/1594.png"],
                        ["1598","请输入第1到第4位图像校验码","yzm1712/159895.png"],
                        ["5989","请输入第2到第5位图像校验码","yzm1712/159895.png"],
                        ["9895","请输入第3到第6位图像校验码","yzm1712/159895.png"],
                        ["1611","请输入第1到第4位图像校验码","yzm1712/161181.png"],
                        ["6118","请输入第2到第5位图像校验码","yzm1712/161181.png"],
                        ["1181","请输入第3到第6位图像校验码","yzm1712/161181.png"],
                        ["1612","请输入第1到第4位图像校验码","yzm1712/161226.png"],
                        ["6122","请输入第2到第5位图像校验码","yzm1712/161226.png"],
                        ["1226","请输入第3到第6位图像校验码","yzm1712/161226.png"],
                        ["1634","请输红色数字图像校验码","yzm1712/1634.png"],
                        ["1680","请输入第1到第4位图像校验码","yzm1712/168024.png"],
                        ["6802","请输入第2到第5位图像校验码","yzm1712/168024.png"],
                        ["8024","请输入第3到第6位图像校验码","yzm1712/168024.png"],
                        ["1700","请输入第1到第4位图像校验码","yzm1712/170069.png"],
                        ["7006","请输入第2到第5位图像校验码","yzm1712/170069.png"],
                        ["0069","请输入第3到第6位图像校验码","yzm1712/170069.png"],
                        ["1828","请输入第1到第4位图像校验码","yzm1712/182830.png"],
                        ["8283","请输入第2到第5位图像校验码","yzm1712/182830.png"],
                        ["2830","请输入第3到第6位图像校验码","yzm1712/182830.png"],
                        ["1858","请输入第1到第4位图像校验码","yzm1712/185864.png"],
                        ["8586","请输入第2到第5位图像校验码","yzm1712/185864.png"],
                        ["5864","请输入第3到第6位图像校验码","yzm1712/185864.png"],
                        ["1858","请输入第1到第4位图像校验码","yzm1712/185891.png"],
                        ["8589","请输入第2到第5位图像校验码","yzm1712/185891.png"],
                        ["5891","请输入第3到第6位图像校验码","yzm1712/185891.png"],
                        ["1863","请输入第1到第4位图像校验码","yzm1712/186311.png"],
                        ["8631","请输入第2到第5位图像校验码","yzm1712/186311.png"],
                        ["6311","请输入第3到第6位图像校验码","yzm1712/186311.png"],
                        ["1939","请输入第1到第4位图像校验码","yzm1712/193906.png"],
                        ["9390","请输入第2到第5位图像校验码","yzm1712/193906.png"],
                        ["3906","请输入第3到第6位图像校验码","yzm1712/193906.png"],
                        ["1965","请输入第1到第4位图像校验码","yzm1712/196502.png"],
                        ["9650","请输入第2到第5位图像校验码","yzm1712/196502.png"],
                        ["6502","请输入第3到第6位图像校验码","yzm1712/196502.png"],
                        ["2003","请输入第1到第4位图像校验码","yzm1712/200370.png"],
                        ["0037","请输入第2到第5位图像校验码","yzm1712/200370.png"],
                        ["0370","请输入第3到第6位图像校验码","yzm1712/200370.png"],
                        ["2014","请输入第1到第4位图像校验码","yzm1712/201404.png"],
                        ["0140","请输入第2到第5位图像校验码","yzm1712/201404.png"],
                        ["1404","请输入第3到第6位图像校验码","yzm1712/201404.png"],
                        ["2015","请输入第1到第4位图像校验码","yzm1712/201521.png"],
                        ["0152","请输入第2到第5位图像校验码","yzm1712/201521.png"],
                        ["1521","请输入第3到第6位图像校验码","yzm1712/201521.png"],
                        ["2016","请输入第1到第4位图像校验码","yzm1712/201681.png"],
                        ["0168","请输入第2到第5位图像校验码","yzm1712/201681.png"],
                        ["1681","请输入第3到第6位图像校验码","yzm1712/201681.png"],
                        ["2139","请输红色数字图像校验码","yzm1712/2139.png"],
                        ["2201","请输红色数字图像校验码","yzm1712/2201.png"],
                        ["2322","请输红色数字图像校验码","yzm1712/2322.png"],
                        ["2555","请输入第1到第4位图像校验码","yzm1712/255572.png"],
                        ["5557","请输入第2到第5位图像校验码","yzm1712/255572.png"],
                        ["5572","请输入第3到第6位图像校验码","yzm1712/255572.png"],
                        ["2649","请输红色数字图像校验码","yzm1712/2649.png"],
                        ["2766","请输入第1到第4位图像校验码","yzm1712/276605.png"],
                        ["7660","请输入第2到第5位图像校验码","yzm1712/276605.png"],
                        ["6605","请输入第3到第6位图像校验码","yzm1712/276605.png"],
                        ["2817","请输红色数字图像校验码","yzm1712/2817.png"],
                        ["2895","请输入第1到第4位图像校验码","yzm1712/289545.png"],
                        ["8954","请输入第2到第5位图像校验码","yzm1712/289545.png"],
                        ["9545","请输入第3到第6位图像校验码","yzm1712/289545.png"],
                        ["3105","请输红色数字图像校验码","yzm1712/3105.png"],
                        ["3141","请输入第1到第4位图像校验码","yzm1712/314108.png"],
                        ["1410","请输入第2到第5位图像校验码","yzm1712/314108.png"],
                        ["4108","请输入第3到第6位图像校验码","yzm1712/314108.png"],
                        ["3304","请输入第1到第4位图像校验码","yzm1712/330422.png"],
                        ["3042","请输入第2到第5位图像校验码","yzm1712/330422.png"],
                        ["0422","请输入第3到第6位图像校验码","yzm1712/330422.png"],
                        ["3908","请输红色数字图像校验码","yzm1712/3908.png"],
                        ["3958","请输入第1到第4位图像校验码","yzm1712/395820.png"],
                        ["9582","请输入第2到第5位图像校验码","yzm1712/395820.png"],
                        ["5820","请输入第3到第6位图像校验码","yzm1712/395820.png"],
                        ["4319","请输入第1到第4位图像校验码","yzm1712/431980.png"],
                        ["3198","请输入第2到第5位图像校验码","yzm1712/431980.png"],
                        ["1980","请输入第3到第6位图像校验码","yzm1712/431980.png"],
                        ["4404","请输入第1到第4位图像校验码","yzm1712/440484.png"],
                        ["4048","请输入第2到第5位图像校验码","yzm1712/440484.png"],
                        ["0484","请输入第3到第6位图像校验码","yzm1712/440484.png"],
                        ["4519","请输入第1到第4位图像校验码","yzm1712/451946.png"],
                        ["5194","请输入第2到第5位图像校验码","yzm1712/451946.png"],
                        ["1946","请输入第3到第6位图像校验码","yzm1712/451946.png"],
                        ["4564","请输入第1到第4位图像校验码","yzm1712/456444.png"],
                        ["5644","请输入第2到第5位图像校验码","yzm1712/456444.png"],
                        ["6444","请输入第3到第6位图像校验码","yzm1712/456444.png"],
                        ["4694","请输红色数字图像校验码","yzm1712/4694.png"],
                        ["4750","请输入第1到第4位图像校验码","yzm1712/475066.png"],
                        ["7506","请输入第2到第5位图像校验码","yzm1712/475066.png"],
                        ["5066","请输入第3到第6位图像校验码","yzm1712/475066.png"],
                        ["4824","请输红色数字图像校验码","yzm1712/4824.png"],
                        ["4838","请输红色数字图像校验码","yzm1712/4838.png"],
                        ["5200","请输红色数字图像校验码","yzm1712/5200.png"],
                        ["5205","请输入第1到第4位图像校验码","yzm1712/520512.png"],
                        ["2051","请输入第2到第5位图像校验码","yzm1712/520512.png"],
                        ["0512","请输入第3到第6位图像校验码","yzm1712/520512.png"],
                        ["5288","请输入第1到第4位图像校验码","yzm1712/528801.png"],
                        ["2880","请输入第2到第5位图像校验码","yzm1712/528801.png"],
                        ["8801","请输入第3到第6位图像校验码","yzm1712/528801.png"],
                        ["5357","请输入第1到第4位图像校验码","yzm1712/535756.png"],
                        ["3575","请输入第2到第5位图像校验码","yzm1712/535756.png"],
                        ["5756","请输入第3到第6位图像校验码","yzm1712/535756.png"],
                        ["5448","请输入第1到第4位图像校验码","yzm1712/544824.png"],
                        ["4482","请输入第2到第5位图像校验码","yzm1712/544824.png"],
                        ["4824","请输入第3到第6位图像校验码","yzm1712/544824.png"],
                        ["5464","请输红色数字图像校验码","yzm1712/5464.png"],
                        ["5544","请输入第1到第4位图像校验码","yzm1712/554414.png"],
                        ["5441","请输入第2到第5位图像校验码","yzm1712/554414.png"],
                        ["4414","请输入第3到第6位图像校验码","yzm1712/554414.png"],
                        ["6096","请输入第1到第4位图像校验码","yzm1712/609696.png"],
                        ["0969","请输入第2到第5位图像校验码","yzm1712/609696.png"],
                        ["9696","请输入第3到第6位图像校验码","yzm1712/609696.png"],
                        ["6313","请输入第1到第4位图像校验码","yzm1712/631304.png"],
                        ["3130","请输入第2到第5位图像校验码","yzm1712/631304.png"],
                        ["1304","请输入第3到第6位图像校验码","yzm1712/631304.png"],
                        ["6428","请输红色数字图像校验码","yzm1712/6428.png"],
                        ["6468","请输红色数字图像校验码","yzm1712/6468.png"],
                        ["6473","请输入第1到第4位图像校验码","yzm1712/647314.png"],
                        ["4731","请输入第2到第5位图像校验码","yzm1712/647314.png"],
                        ["7314","请输入第3到第6位图像校验码","yzm1712/647314.png"],
                        ["6574","请输红色数字图像校验码","yzm1712/6574.png"],
                        ["6622","请输入第1到第4位图像校验码","yzm1712/662233.png"],
                        ["6223","请输入第2到第5位图像校验码","yzm1712/662233.png"],
                        ["2233","请输入第3到第6位图像校验码","yzm1712/662233.png"],
                        ["6943","请输入第1到第4位图像校验码","yzm1712/694382.png"],
                        ["9438","请输入第2到第5位图像校验码","yzm1712/694382.png"],
                        ["4382","请输入第3到第6位图像校验码","yzm1712/694382.png"],
                        ["6978","请输入第1到第4位图像校验码","yzm1712/697820.png"],
                        ["9782","请输入第2到第5位图像校验码","yzm1712/697820.png"],
                        ["7820","请输入第3到第6位图像校验码","yzm1712/697820.png"],
                        ["7057","请输入第1到第4位图像校验码","yzm1712/705779.png"],
                        ["0577","请输入第2到第5位图像校验码","yzm1712/705779.png"],
                        ["5779","请输入第3到第6位图像校验码","yzm1712/705779.png"],
                        ["7186","请输入第1到第4位图像校验码","yzm1712/718699.png"],
                        ["1869","请输入第2到第5位图像校验码","yzm1712/718699.png"],
                        ["8699","请输入第3到第6位图像校验码","yzm1712/718699.png"],
                        ["7273","请输入第1到第4位图像校验码","yzm1712/727333.png"],
                        ["2733","请输入第2到第5位图像校验码","yzm1712/727333.png"],
                        ["7333","请输入第3到第6位图像校验码","yzm1712/727333.png"],
                        ["7624","请输入第1到第4位图像校验码","yzm1712/762414.png"],
                        ["6241","请输入第2到第5位图像校验码","yzm1712/762414.png"],
                        ["2414","请输入第3到第6位图像校验码","yzm1712/762414.png"],
                        ["7682","请输入第1到第4位图像校验码","yzm1712/768204.png"],
                        ["6820","请输入第2到第5位图像校验码","yzm1712/768204.png"],
                        ["8204","请输入第3到第6位图像校验码","yzm1712/768204.png"],
                        ["7972","请输红色数字图像校验码","yzm1712/7972.png"],
                        ["7989","请输入第1到第4位图像校验码","yzm1712/798902.png"],
                        ["9890","请输入第2到第5位图像校验码","yzm1712/798902.png"],
                        ["8902","请输入第3到第6位图像校验码","yzm1712/798902.png"],
                        ["8018","请输红色数字图像校验码","yzm1712/8018.png"],
                        ["8407","请输红色数字图像校验码","yzm1712/8407.png"],
                        ["8574","请输入第1到第4位图像校验码","yzm1712/857435.png"],
                        ["5743","请输入第2到第5位图像校验码","yzm1712/857435.png"],
                        ["7435","请输入第3到第6位图像校验码","yzm1712/857435.png"],
                        ["8586","请输入第1到第4位图像校验码","yzm1712/858689.png"],
                        ["5868","请输入第2到第5位图像校验码","yzm1712/858689.png"],
                        ["8689","请输入第3到第6位图像校验码","yzm1712/858689.png"],
                        ["8651","请输入第1到第4位图像校验码","yzm1712/865156.png"],
                        ["6515","请输入第2到第5位图像校验码","yzm1712/865156.png"],
                        ["5156","请输入第3到第6位图像校验码","yzm1712/865156.png"],
                        ["8808","请输红色数字图像校验码","yzm1712/8808.png"],
                        ["8883","请输入第1到第4位图像校验码","yzm1712/888334.png"],
                        ["8833","请输入第2到第5位图像校验码","yzm1712/888334.png"],
                        ["8334","请输入第3到第6位图像校验码","yzm1712/888334.png"],
                        ["8902","请输入第1到第4位图像校验码","yzm1712/890273.png"],
                        ["9027","请输入第2到第5位图像校验码","yzm1712/890273.png"],
                        ["0273","请输入第3到第6位图像校验码","yzm1712/890273.png"],
                        ["8989","请输入第1到第4位图像校验码","yzm1712/898905.png"],
                        ["9890","请输入第2到第5位图像校验码","yzm1712/898905.png"],
                        ["8905","请输入第3到第6位图像校验码","yzm1712/898905.png"],
                        ["9147","请输入第1到第4位图像校验码","yzm1712/914768.png"],
                        ["1476","请输入第2到第5位图像校验码","yzm1712/914768.png"],
                        ["4768","请输入第3到第6位图像校验码","yzm1712/914768.png"],
                        ["9538","请输红色数字图像校验码","yzm1712/9538.png"],

                ]
    TIME_HISTORY =[
                    ["11:29:59",92600,"2017-12-16 11:29:43"],
                    ["11:29:58",92600,"2017-12-16 11:29:54"],
                    ["11:29:57",92500,"2017-12-16 11:29:34"],
                    ["11:29:56",92400,"2017-12-16 11:29:28"],
                    ["11:29:55",92300,"2017-12-16 11:28:35"],
                    ["11:29:54",92300,"2017-12-16 11:28:49"],
                    ["11:29:53",92300,"2017-12-16 11:28:52"],
                    ["11:29:52",92300,"2017-12-16 11:28:54"],
                    ["11:29:51",92300,"2017-12-16 11:28:56"],
                    ["11:29:50",92300,"2017-12-16 11:28:57"],
                    ["11:29:49",92300,"2017-12-16 11:29:00"],
                    ["11:29:48",92300,"2017-12-16 11:29:03"],
                    ["11:29:47",92300,"2017-12-16 11:29:05"],
                    ["11:29:46",92300,"2017-12-16 11:29:07"],
                    ["11:29:45",92300,"2017-12-16 11:29:08"],
                    ["11:29:44",92300,"2017-12-16 11:29:09"],
                    ["11:29:43",92300,"2017-12-16 11:29:10"],
                    ["11:29:42",92300,"2017-12-16 11:29:11"],
                    ["11:29:41",92300,"2017-12-16 11:29:12"],
                    ["11:29:40",92300,"2017-12-16 11:29:14"],
                    ["11:29:39",92300,"2017-12-16 11:29:16"],
                    ["11:29:38",92300,"2017-12-16 11:29:18"],
                    ["11:29:37",92300,"2017-12-16 11:29:19"],
                    ["11:29:36",92300,"2017-12-16 11:29:21"],
                    ["11:29:35",92300,"2017-12-16 11:29:24"],
                    ["11:29:34",92300,"2017-12-16 11:29:26"],
                    ["11:29:33",92300,"2017-12-16 11:29:28"],
                    ["11:29:32",92300,"2017-12-16 11:29:31"],
                    ["11:29:31",92200,"2017-12-16 11:28:35"],
                    ["11:29:30",92200,"2017-12-16 11:28:38"],
                    ["11:29:29",92200,"2017-12-16 11:28:57"],
                    ["11:29:28",92100,"2017-12-16 11:28:09"],
                    ["11:29:27",92100,"2017-12-16 11:28:22"],
                    ["11:29:26",92100,"2017-12-16 11:28:28"],
                    ["11:29:25",92100,"2017-12-16 11:29:12"],
                    ["11:29:24",92000,"2017-12-16 11:00:19"],
                    ["11:29:23",92000,"2017-12-16 11:00:44"],
                    ["11:29:22",92000,"2017-12-16 11:01:20"],
                    ["11:29:21",92000,"2017-12-16 11:02:08"],
                    ["11:29:20",92000,"2017-12-16 11:04:01"],
                    ["11:29:19",92000,"2017-12-16 11:06:32"],
                    ["11:29:18",92000,"2017-12-16 11:09:20"],
                    ["11:29:17",92000,"2017-12-16 11:13:07"],
                    ["11:29:16",92000,"2017-12-16 11:16:13"],
                    ["11:29:15",92000,"2017-12-16 11:18:02"],
                    ["11:29:14",92000,"2017-12-16 11:20:08"],
                    ["11:29:13",92000,"2017-12-16 11:21:05"],
                    ["11:29:12",92000,"2017-12-16 11:22:15"],
                    ["11:29:11",92000,"2017-12-16 11:23:19"],
                    ["11:29:10",92000,"2017-12-16 11:24:26"],
                    ["11:29:09",92000,"2017-12-16 11:25:11"],
                    ["11:29:08",92000,"2017-12-16 11:25:35"],
                    ["11:29:07",92000,"2017-12-16 11:25:58"],
                    ["11:29:06",92000,"2017-12-16 11:26:17"],
                    ["11:29:05",92000,"2017-12-16 11:26:30"],
                    ["11:29:04",92000,"2017-12-16 11:26:36"],
                    ["11:29:03",92000,"2017-12-16 11:26:41"],
                    ["11:29:02",92000,"2017-12-16 11:26:45"],
                    ["11:29:01",92000,"2017-12-16 11:26:51"],
                    ["11:29:00",92000,"2017-12-16 11:26:56"],
                    ]
    #把timehistory转变为字典
    TIME_HISTORY_DICT = {}
    for each in TIME_HISTORY:
        TIME_HISTORY_DICT[each[0]] = each[1:]
    #print(TIME_HISTORY_DICT)

    #验证码图片地址加前缀
    for i in range(len(IMAGE_CODES)):
        IMAGE_CODES[i][2] ="http://51moni-sh.oss-cn-shanghai.aliyuncs.com/" + IMAGE_CODES[i][2]


    def getLowPrice(self, mock_time):
        mock_time = '{hour:02d}:{minute:02d}:{second:02d}'.format(
            hour=mock_time.hour, minute=mock_time.minute, second=mock_time.second)
        data = self.TIME_HISTORY_DICT.get(mock_time, self.TIME_HISTORY_DICT["11:29:59"])
        return data[0]

    def getBasePriceTime(self, mock_time):
        mock_time = '{hour:02d}:{minute:02d}:{second:02d}'.format(
            hour=mock_time.hour, minute=mock_time.minute, second=mock_time.second)
        data = self.TIME_HISTORY_DICT.get(mock_time, self.TIME_HISTORY_DICT["11:29:59"])
        basepricetime = filter(str.isdigit, data[1])
        return basepricetime

    def getRandImageCode(self):
        return self.IMAGE_CODES[random.randint(0, len(self.IMAGE_CODES) - 1)]


if __name__ == "__main__":
    policy = History201712()
    print(policy.getBasePriceTime(datetime.datetime(2012,12,12,11,29,59)))
    































    
        
