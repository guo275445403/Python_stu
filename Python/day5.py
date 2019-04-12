#!/usr/bin/python  
#-*-coding:utf-8-*-
#userbiubiubiu
import json,requests
class gaode(object):
    def qingqiu(self,page):
        url='https://www.gaode.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum={}&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=11.8&city=410100&geoobj=113.547581%7C34.681186%7C113.897023%7C34.835746&keywords=%E5%A4%A7%E5%AD%A6'.format(page)
        head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}
        aaa=requests.get(url=url,headers=head)
        html=aaa.content.decode('utf-8')
        html=json.loads(html)
        print(html)
        return html
    def guolv(self,abc):
        with open('aa.txt','w+',encoding='utf-8') as f:
            f.write('学校名称,')
            f.write('学校位置,')
            f.write('电话\n')
            for i in range(20):
                a=(abc['data']['poi_list'][i]['name'])
                f.write(a+',')
                b=(abc['data']['poi_list'][i]['address'])
                f.write(b+',')
                c=(abc['data']['poi_list'][i]['areacode'])
                d=(abc['data']['poi_list'][i]['adcode'])
                f.write(c+'-'+d+',\n')
zong=gaode()
abc=zong.qingqiu(0)
zong.guolv(abc)