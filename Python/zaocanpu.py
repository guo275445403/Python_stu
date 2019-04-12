#!/usr/bin/python  
#-*-coding:utf-8-*-
#userbiubiubiu
import requests,re,os
class zaocanpu(object):
    a = 0
    head = {
        'User-Agent': 'Mozilla / 5.0(WindowsNT10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 72.0.3626.96Safari / 537.36',
    }
    def qingqiu(self,page):
        url='https://www.doutula.com/article/list/?page={}'.format(page)
        head={
            'User-Agent': 'Mozilla / 5.0(WindowsNT10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 72.0.3626.96Safari / 537.36',
            }
        res=requests.get(url,headers=head)
        html=res.content.decode('utf-8')
        return html
    def guolv(self,html):
        neirong = []
        mingzi = []
        patt=re.compile(r'<a href="(.*?)" class="list-group-item ')
        itmes=patt.findall(html)
        neirong.append(itmes)
        patt1=re.findall(r'<div class="random_title">(.*?)<div class="date">',html)
        mingzi.append(patt1)
        return neirong,mingzi
    def qingqiu1(self,neirong,mingzi):
        for i in range(10):
            url=neirong[0][i]
            res=requests.get(url,headers=self.head)
            html=res.content.decode('utf-8')
            itmes=re.findall(r"this.src='(.*?)'",html)
            os.makedirs(r'E:\图片\{}'.format(mingzi[0][i]))
            os.chdir(r'E:\图片\{}'.format(mingzi[0][i]))
            for s in range(len(itmes)):
                abcd=os.path.splitext(itmes[1])
                abcde=abcd[1]
                for j,k in enumerate(itmes):
                    res = requests.get(k)
                    ht = res.content
                    with open(r'{}{}'.format(j,abcde),'wb')as f:
                        f.write(ht)
                    self.a += 1
abc=zaocanpu()
for i in range(1,3):
    aa=abc.qingqiu(i)
    a,b=abc.guolv(aa)
    abc.qingqiu1(a,b)

