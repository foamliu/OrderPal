# /usr/bin/env python
# coding=utf8

import hashlib
import http.client
import json
import random
import urllib

appid = '20190723000320385'  # 你的appid
secretKey = 'wtdLNIvQLI8jCkL5a25l'  # 你的密钥
m1 = hashlib.md5()
theurl = '/api/trans/vip/translate'


def translate(q):
    # q = 'apple'
    fromLang = 'auto'
    toLang = 'zh'
    salt = random.randint(32768, 65536)

    sign = appid + q + str(salt) + secretKey
    m1.update(bytes(sign, 'utf-8'))
    sign = m1.hexdigest()
    myurl = theurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        # print(response.status)
        content = response.read().decode('utf-8')
        ret = json.loads(content)
        # print(ret)
        # print(ret['from'])
        # print(ret['to'])
        # print(ret['trans_result'][0]['src'])
        # print(ret['trans_result'][0]['dst'])
        response.read()
        return ret['trans_result'][0]['dst']
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print(translate('apple'))
