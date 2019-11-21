# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 15:15
# @Author  : Wang Bingyin
# @Email   : xxxxxxx@163.com
# @File    : request.py
# @Software: PyCharm

import json
import requests

class Request:
    def __init__(self, method, url, data=None, json=None, cookies=None, headers=None):
        try:
            if method == 'GET':
                self.res = requests.get(url=url, params=data, cookies=cookies, headers=headers)
            elif method == 'POST':
                self.res = requests.post(url=url, data=data, json=json, cookies=cookies, headers=headers)
            else:
                self.res = requests.request(method=method, url=url, data=data, cookies=cookies, headers=headers)
        except Exception as e:
            raise e

    def get_code(self):
        return self.res.status_code

    def get_text(self):
        return self.res.text

    def get_json(self):
        return self.res.json()

    def get_cookies(self, key=None):
        if key:
            return self.res.cookies
        else:
            return self.res.cookies[key]

if __name__ == '__main__':
    url = 'http://wap.dev.gomegj.com/login/yf/lg'
    data = {"account":"CU0D73hqiuOQ0lgYs5MoW8bIZIz5v5F6er/UI+jCzKo35/chm67cnxo1uFv5/CK/IqodLTphh08a3ukOhxbHY+0lwksfz3aRGdv1tZNcP1c/4SlKjYKzp/Bm8Hz59NQpApGSI7Ugk5PFE3a/3PVfByRShBKdGIITuePZV+SkASAyB853KT1/xPo7VZjfcPquyYgmsOJqTsmrbtmXbLOUo0RahFDyZTFGp1J/nayxX5J73ludK5hQAnibqSK7uFs9CNml2EOb4EaWBan/A5YQticLthQDNuOQAEahJ3cNbiaUMCTQpkfgFnHiNxFtpA7+qVs73+ns8KOw7mcCaVCA4w==",
	"pwd":"hO5RXsRpc7hJ7FycDikzNiutBkuM8tOxO1EyfKRmSaN067/nGe0zRMug7EnE5y3Hsf6+BoJiubBO8I5yYPKntlFKuW5lLjJ4oZXGGwZ7s8Qj8+PTPxvwjs5CWeK1Hu8khpnGCx4lywiF2+IFfOSDaMTlE8W+PBTlbTgSFbm6+zTbS8hR07Q4n5ISSye44o9Hvg/SFzc6hMdZn8WQSmhT0LMgCEUjeVInjNs35/g6X0EfUIWqrZk/GGdkwRzDluB/JSNeArxJVWN/P5lr+AkZL27xotWQuHJMsFUsYvQJ3qrbY2JU8laIkXN7wJuJWuw0FsSIfxy4uw3OpGlnQckZ6g==",
	"clickTime":4}
 #    data = {"account":"QX23iesejquAlS4TzQR9SpxGZoTROAcLabupvaSfr5J13+XjcRkfv9nHCWSDeJx6xGDMndVy+EM7kQWGwjmtP+UKWybEGj5tyCXLiQxr43BfD9RsTQ2HSVGi2yxJzvpGWBEtlJyEuR+2tbE6SlQ9cogbrEqShRjzeH83SsDX0REAeM64QKQJi/3AqgwV1xqTGh1TNiL1PLaynZRAZ/FH4VDyBtgX0Ioy21JzsXyCBd3Rz7sCwUItksmrT9D6M7QHj28TPmGXd+avkPnDFqPERortiswGzOiPd6EErLriQAf6LOZFJPwU8PG7gxPsUmZhAEKt4GjdVsZrBZ7qQQpMuA==",
 # "pwd":"gds1Hljjq5gzGABuq/36aebAe6Hoqrgf9H0qtlpm5/HaD502B8J2LNgqp7iFgTKtv8dyCQ+Z3hQAtOm8/GlW1zveVbsefEFJwVywHdMUBGbpBo+95rm/rTT0M4B3ZHtCvjBI12nhKNI2P8/gxKcxU3TN4DTKCSmShIMmlWNRxyMBUJ8cGLcjpZZfr2Ns8KYnCGXIgru3jpGgqcne5qypGEsRg3ualb8aE2QVo+lHL9olR3oYaHMiPm0QUxLaNLK8SzKRVFQ5fCIz4NKspBSCpo8qXW2kSf7idLh/xKgkybDar8yecaJYblWL5EtQ9So7IOegh/1r25sKa6x4Wg7Vmw==",
 # "clickTime":1}
    res = Request("POST", url, json=data)
    # print(res.get_json())
    cookies = res.get_cookies('body')
    # print("======",cookies)
    url2 = 'http://wap.dev.gomegj.com/recycle/yf/partInActivity'
    data2 = {"orderSource": 4, "categoryId": "12", "cityCode": "110105"}
    res2 = Request("GET", url2, data=data2, cookies=cookies)
    print(res2.get_text())