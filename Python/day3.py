#!/usr/bin/python  
#-*-coding:utf-8-*-
#userbiubiubiu

# class xiaoai():
#     def __bofang(self):
#         print('haha')
#
#     def diange(self):
#         self.__guanji()
#         print('dudu')
#
#     def __guanji(self):
#         self.__bofang()
#         print('biubiu')
# class new_xiaoai():
#     def __laji(self):
#         print('laji')
#
# class newnew_xiaoai(xiaoai,new_xiaoai):
#     def __init__(self,x):
#         self.name=x
#     def aaa(self):
#         print('{}又长高了'.format(self.name))
#     def bbb(self):
#         print('{}66666'.format(self.name))
# aa=newnew_xiaoai('小朱')
# aa.aaa()
# aa.bbb()
#
# import re,requests,xlwt,xlrd
# class qiushi(object):
#     def fangwen(self,a):
#         head = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}
#         url='https://www.qiushibaike.com/textnew/page/{}/?s=5167701'.format(a)
#         qingqiu=requests.get(url,headers=head)
#         html=qingqiu.text
#         return html
#     def guolv(self,html):
#         abc=[]
#         a=re.findall(r'<div class="content">(.*?)</span>',html,re.S)
#         for i in a:
#             i=i.replace('<span>','').replace('<br/>','').strip()
#             abc.append(i)
#         return abc
#     def baocun(self,qwe):
#         with open('b.txt','a',encoding='utf-8')as f:
#             for i in qwe:
#                 f.write(i+'\n')
#
# qiu=qiushi()
# aa=qiu.fangwen(1)
# qwe=qiu.guolv(aa)
# qiu.baocun(qwe)
# with open('b.txt','r',encoding='utf-8') as f:
#     aa=f.readlines()
# f1=xlwt.Workbook()
# sheet=f1.add_sheet('糗事')
# for i in range(len(aa)):
#     sheet.write(i,0,aa[i])
# f1.save('6666.xls')

# import re,requests,xlwt
# mingcheng1=[]
# daoyan1=[]
# miaosu1=[]
# pingjia1=[]
# class doubai(object):
#     def xiangying(self,a):
#         head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}
#         url='https://movie.douban.com/top250?start={}&filter='.format(a)
#         aaa=requests.get(url,headers=head)
#         html=aaa.text
#         return html
#     def guolv(self,html):
#         # zonggong=re.findall(r'<div class="info">(.*?)</li>',html,re.S)
#         mingcheng=re.findall(r'<img width="100" alt="(.*?)" src=',html)
#         for i in mingcheng:
#             mingcheng1.append(i)
#         daoyan=re.findall(r'导演: (.*?)&nbsp;&nbsp;&nbsp;主演',html)
#         for j in daoyan:
#             daoyan1.append(j)
#         miaosu=re.findall(r'<span class="inq">(.*?)</span>',html)
#         for k in miaosu:
#             miaosu1.append(k)
#         pingjia=re.findall(r'<span>(.*?)评价</span>',html)
#         for l in pingjia:
#             pingjia1.append(l)
#         # print(mingcheng1,daoyan1,miaosu1,pingjia1)
#         return mingcheng1,daoyan1,miaosu1,pingjia1
#     def baocun(self,a,b,c,d):
#         with open('c.txt','w+',encoding='utf-8')as f:
#             for i in range(len(b)):
#                 f.write(a[i]+',')
#                 f.write(b[i]+',')
#                 f.write(c[i]+',')
#                 f.write(d[i]+'\n')
# aa=doubai()
# for i in range(0,26,25):
#     bb=aa.xiangying(i)
#     a,b,c,d=aa.guolv(bb)
#     aa.baocun(a,b,c,d)
# with open('c.txt','r',encoding='utf-8')as f:
#     a=f.readlines()
# f=xlwt.Workbook('666.xls')
# sheet=f.add_sheet('dianying')
# sheet.write(0,0,'名称')
# sheet.write(0,1,'导演')
# sheet.write(0,2,'影评')
# sheet.write(0,3,'评价人数')
# for i,j in enumerate(a):
#     j=j.split(',')
#     for k in range(len(j)):
#         sheet.write(i+1,k,j[k])
# f.save('666.xls')
# import pymysql,xlrd
# conn=pymysql.connect(host='192.168.0.118',port=3306,user='root',password='123456',charset='utf8')
# abc=conn.cursor()
# f=xlrd.open_workbook('666.xls')
# sheet=f.sheets()[0]
# a=sheet.row_values()
# for i in range(a):
#         if a != 'exit' and a!='shuru':
#             abc.execute(a)
#             print(abc.fetchall())
#         elif a == 'shuru':
#             print(aaa)
#             for j in range(len(aaa)):
#                 if j==0:
#                     abc.execute('create table dianying ({} char(255),{} char(255),{} char(255))'.format(aaa[j][0],aaa[j][1],aaa[j][2],aaa[j][3]))
#                 else:
#                     abc.execute('insert into dianying values("{}","{}","{}","{}")'.format(aaa[j][0],aaa[j][1],aaa[j][2],aaa[j][3]))
#                     print(abc.fetchall())
#         elif a=='exit':
#             break
#     except:
#         continue
# conn.close()
