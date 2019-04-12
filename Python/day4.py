#!/usr/bin/python  
#-*-coding:utf-8-*-
#userbiubiubiu

# import json
# a={'name':123}
# b=json.dumps(a)
# print(b)
# abc=json.loads(b)
# print(abc)
import requests,re,json
xuexiao=[]
class gaode(object):
    def qingqiu(self,page):
        head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}
        url='https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=90&cityId=538&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&=0&at=6d103953ad584104b7341a69fe4a5475&rt=6e7a0de0083742e4806e05740fe70c2e&_v=0.36859449&userCode=696300212&x-zp-page-request-id=b00b2f98a5c54d328d8a1132f60d23e7-1550653288848-23394'.format(page)
        res=requests.get(url=url,headers=head)
        html=res.content.decode('utf-8')
        a=json.loads(html)
        return a
    def guolv(self,html):
        with open('b.txt','w+',encoding='utf-8') as f:
            for i in range(90):
                a=(html['data']['results'][i]['company']['name'])
                f.write(a+',')
                aa=(html['data']['results'][i]['jobTag']['searchTag'])
                f.write(aa+',')
                aaa = (html['data']['results'][i]['city']['display'])
                f.write(aaa+',')
                aaaa=(html['data']['results'][i]['salary'])
                f.write(aaaa+'\n')
a=gaode()
for i in range(3):
    abc=a.qingqiu(i)
    a.guolv(abc)