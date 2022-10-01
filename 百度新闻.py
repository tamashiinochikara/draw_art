"""
======================
@author:沈志超
@time:2022/9/29:11:52
=====================
"""
import requests
headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50'}
url = "https://www.baidu.com/s?tn=news&rtt=1&bsst=1&cl=2&wd=%阿里巴巴"
res = requests.get(url,headers).text
print(res)