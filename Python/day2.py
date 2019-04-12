#!/usr/bin/python
#-*- coding:utf-8 - * -
#user:biubiubiu
# a='1q e 1{} Aaqrts1a1a1  '
# f=a.format('1qe1') 
# print(type(a))
# print(f)
# # abc.popitem()

# abc={'name':['小明','小红'],
#      'age':11,
#      'sex':'aaa男'}
# bc={'name':['小明','小红'],
#      'age':11111,
#      'sex':'男'}
# print(abc.items())
# print(abc)
# abc=[12,23,22,34,45,56]
# bc=[1,8,688]
# abc.extend(bc)
# print(abc)
# a=3
# a/=1
# print(a)
# for i in range(3):
#     a=input('请输入成绩：')
#     a=int(a)
#     if a >90 and a<=100:
#     	print('优秀')
#     elif a>80 and a<=90:
# 	    print('良好')
#     elif a>70 and a<=80:
#       print('中等')
#     elif a >60 and a<=70:
# 	    print('及格')
#     elif a>0 and a<=60:
#         print('渣渣')
#     elif  a>100 :
#         print('输入错误，重新输入：')


# a=input('输入:')
# if a.startswith('a'):
# 	 if a.endswith('c'):
# 	    print('hello wrold')
# 	 else:
# 	    print('hello')
# elif a.endswith('c'):
# 	print('world')
# else:
# 	print('123')
# a={1:2,"name":111}
# for i in a.keys():
# 	for j in a.values():
# 	 print(i,j)

# b=0
# for i in range(0,101):
# 	b=i+b
# 	i+=1
# print(b)

# a=0
# for i in range(1,100,2):
# 	a=a+i-(i-1)
# print(a)

# a=0
# for i in range(1,100):
# 	if i%2==0:
# 		a-=i
# 	else:
# 		a+=i
# print(a)

# a=0
# b=0
# for i in range(1,100,2):
# 	a=a+i
# for j in range(0,100,2):
# 	b=b+j
# c=a-b
# print(c)

# a=0
# b=0
# for i in range(1,100):
# 	if i%2==1:
# 		a=a+i
# 	else:
# 		b=b+i
# c=a-b
# print(c)

# a=['asdc','saawd','Asda','asdac']
# for i in a:
# 	if( i[0]=='a' or i[0]=='A')and i[-1]=='c':
# 		print(i)

import random
# a=random.randint(1,10) #从1到10中随机选择一个数字给a
# b=random.randint(1,13)
# for i in range(3):
# 	a = int(input('请输入内容:'))
# 	if a>b:
# 		print('数字过大')
# 	elif a<b:
# 	    print('数字过小')
# 	elif a == b:
# 		print('输入正确')
# 		break
# 	if i==2:
# 		print('赔钱')
# print(2-i)
#
#  判断三角形
# abc=[]
# for i in range(3):
# 	a=int(input('请输入数字:'))
# 	abc.append(a)
# abc.sort()
# if abc[0]+abc[1]>abc[2]:
# 	  if abc[0]**2+abc[1]**2>abc[-1]**2:
# 		  print("锐角三角形")
# 	  elif abc[0]**2+abc[1]**2==abc[-1]**2:
# 	      print('直角三角形')
# 	  else:
# 	      print('钝角三角形')
# else:
# 	print('构不成三角形')


#  求100-1000以内的水仙花数字
# for i in range(100,1000):
# 	a=i//100
# 	b=i//10%10
# 	c=i%10
# 	if a**3+b**3+c**3==i:
# 		print(i)
# 	else:
# 		continue


# 质数之和
# def zhishu(b,c):
#     a=0
#     for i in range(b,c):
#         for j in range(2,i+1):
#             if i%j==0:
#                 break
#         if i==j:
#             a=a + i
#     print(a)
# zhishu(20,30)

# 判断是不是回文字符串
# a=input('请输入字符串:')
# b=len(a)//2
# for i in range(0,b+1):
# 	if a[i]!=a[-i-1]:
# 		print('不是回文字符串')
# 		break
# else:
# 	print('是回文字符串')


# 获取列表里的元素
# a=['电脑','手机','计算机','iphone']
# for i,j in enumerate(a):
# 	print(i+1,j)
# while True:
# 		b =int(input('请输入购买的商品号：'))
# 		if b=='exit':
# 			break
# 		elif type(a)!=int and  b>i:
# 			print('输入有误,请从新输入：')
# 			continue
# 		else:
# 			print(a[int(b)-1])
# print(i,j)


# 冒泡法排序
# a=input('请输入数字')
# a=a.split(',')
# for i in range(len(a)):
#     for j in range(len(a)-1):
#         if int(a[j]) > int(a[j+1]):
#              a[j],a[j+1]=a[j+1],a[j]
# print(a)


# 99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(j,i,j*i),end='\t')
#     print()


# 无限循环
# class Infinit:
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         return None
# for i in Infinit():
#     print("Python的无限循环!")

# a=0
# b=0
# while b < 100:
#     b = b + 1
#     a=a+b
# print(a)



# 求平均成绩
# while True:
#     b=input('!!!')
#     if b[0]=='-':
#          break
#     else:
#         a = b.split(',')
#         sum=0
#     for i in a:
#         sum+=int(i)
#     print('平均数：',sum/len(a))
#     for j in a:
#             if int(j)<=sum/len(a):
#                 print('低于平局值分数',j)

#
# a=input('输入数组:')
# a=a.split(',')
# print(a)
# b=int(input("请输入数字"))
# for i in range(len(a)-1):
#     if int(a[i])+int(a[i+1])==b:
#         print(a[i],a[i+1])




# if __name__== '__main__':
#     print('asd')
#     input('sadad11')

# from xlutils.copy import copy
# import  xlrd
# f=xlrd.open_workbook('666.xls')
# new_f=copy(f)
# sheet=new_f.get_sheet(0)
# for i in range(10):
#     for j in range(10):
#         sheet.write(i,j,'啊啊啊哈')
# new_f.save('666.xls')

# print(222)
# print(f.sheet_names())
# sheet=f.sheet_by_name('excel学习')
# print(sheet.nrows)
# print(sheet.row_values(1))
# print(sheet.col_values(4))
# print(sheet.cell(1,4).value)


# 把两个文件的内容导入到Excel表中
# zongneirong=[]
# with open('a.txt','r+',encoding='utf-8') as f1:
#     a1=f1.readlines()
# with open('b.txt','r',encoding='utf-8') as f2:
#     a2=f2.readlines()
# zongneirong=a1+a2
# import xlwt
# f3=xlwt.Workbook('666.xls')
# sheet = f3.add_sheet('excel学习')
# for i,j in enumerate(zongneirong):
#     j=j.strip().split(',')
#     for k in range(len(j)):
#         sheet.write(i,k,j[k])
# f3.save('666.xls')




# import os
# os.chdir('E:\\Python')
# a=os.makedirs(r'asdds\asd')
# os.removedirs(r'asdds\asd')
# abc=os.popen('ipconfig/all')
# print(abc.read())
# a=os.path.splitext('day1.py')
# for i in os.listdir():
#     if os.path.splitext(i)[1]=='.py':
#         print(i)



# import xlutils,xlwt,xlrd
# f=xlwt.Workbook()
# sheet=f.add_sheet('666')
# sheet.write(0,0,'sad')
# f.save('aa.xls')
# f=xlrd.open_workbook('aa.xls')
# a=f.sheets()[0]
# print(a.cell(0,0))

# import xlrd
# from xlutils.copy import copy
# f=xlrd.open_workbook('aa.xls')
# new_f=copy(f)
# sheet=new_f.get_sheet(0)
# sheet.write(0,2,'河南')
# new_f.save('aa.xls')

# import re
# a='sA1231024al1023sfa1ass1321ssfl'
# c=re.findall('a.*?2',a,re.I)
# print(c)

# import os,re
# a=os.listdir(r'E:\Python')
# for i in a:
#     if os.path.splitext(i)[-1]=='.py':
#         print(i)

# import requests,re
# class qiushi_splider(object):
#     def qingqiu(self,page):
#         url='https://www.qiushibaike.com/text/page/{}/'.format(page)
#         #发送请求
#         head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}
#         xiangying=requests.get(url,headers=head)
#         # with open('a.html','w',encoding='utf-8') as f:
#         #     f.write(xiangying.text)
#         #读取响应 1.text 2.content
#         html=xiangying.content.decode('utf-8')
#         return html
#     def guolv(self,html):
#         #将正则表达式编译
#         shuju=[]
#         patt=re.compile(r'<div class="content">(.*?)</span>',re.S)
#         #将编译后的条件到字符串中查找
#         items=patt.findall(html)
#         for i in items:
#             i=i.replace('<span>','').replace('<br/>','').strip()
#             shuju.append(i)
#             print(i)
#         return shuju
#     def baocun(self,qwe):
#         with open('a.txt','a',encoding='utf-8') as f:
#             for i in qwe:
#                 f.write(i+'\n')
# qiu=qiushi_splider()
# for i in range(1,5):
#     html=qiu.qingqiu(page=i)
#     qwe=qiu.guolv(html)
#     qiu.baocun(qwe)

# 爬虫图片
import re,requests,os
#
# class qiushi(object):
#     a=0
#     def qingqiu(self, page):
#         url='http://www.budejie.com/{}'.format(page)
#         #发送请求
#         head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}
#         xiangying=requests.get(url,headers=head)
#         with open('a.html','w',encoding='utf-8') as f:
#             f.write(xiangying.text)
#         #读取响应 1.text 2.content
#         html=xiangying.content.decode('utf-8')
#         return html
#     def guolv(self,html):
#         shuju = []
#         patt=re.compile(r'<img src="(.*?)"')
#         items=patt.findall(html)
#         for i in items:
#             # patt1=re.compile(r'<img src="(.*?)"')
#             # items1=patt1.findall(i)
#             shuju.append(i)
#         return shuju
#
#     def save(self,qwe):
# #         图片是二进制,请求图片网站来获取图pain的yuanma
#         aaa=[]
#         aaaa=[]
#         for s in qwe:
#             a=os.path.splitext(s)
#             aaaa.append(a[0])
#             aaa.append(a[1])
#         print(aaa)
#
#         for j,i in enumerate(aaaa):
#             print(j)
#             res=requests.get(i)
#             ht=res.content #(读取的是二进制)
#             with open(r'E:\图片\{}{}'.format(self.a,aaa[j]),'wb')as f:
#                 f.write(ht)
#             self.a+=1
# aa=qiushi()
# for i in range(1,2):
#     aaa=aa.qingqiu(i)
#     a=aa.guolv(aaa)
#     aa.save(a)
# a=os.listdir(r'E:\图片')
# a=len(a)
# os.chdir(r'E:\图片')
# for i in range(a):
#     os.remove('{}.jpg'.format(i))

import xlrd,xlwt,xlutils
# f=xlrd.open_workbook('666.xls')
# sheet=f.sheets()[0]
# row=sheet.nrows
# with open('a.txt','w+',encoding='utf-8') as f:
#     for i in range(row):
#         a=sheet.row_values(i)
#         for j in a:
#             if  j!=a[-1]:
#                 f.write(j+',')
#             else:
#                 f.write(j+'\n')

# with open('a.txt','r+',encoding='utf-8') as f:
#     a=f.readlines()
# f=xlwt.Workbook()
# sheet=f.add_sheet('电影')
# for i,j in enumerate(a):
#     j=j.strip().split(',')
#     for k in range(len(j)):
#         sheet.write(i,k,j[k])
# f.save('1.xls')

# import pymysql,xlrd
# conn=pymysql.connect(host='192.168.0.118',user='root',port=3306,charset='utf8',password='123456')
# fubiao=conn.cursor()
# fubiao.execute('use zuoye1;')
# with open('b.txt','r+',encoding='utf-8') as f:
#     a=f.readlines()
# for i,j in enumerate(a):
#     j=j.strip().split(',')
#     if i==0:
#         fubiao.execute('create table biao3({} char(255),{} char(255),{} char(255));'.format(j[0],j[1],j[2]))
#     else:
#         fubiao.execute('insert into biao3 values("{}","{}","{}");'.format(j[0],j[1],j[2]))
#         conn.commit()
# conn.close()

#!/usr/bin/python
#-*-coding:utf-8 -*-
# b=100
# a=[str(i) for i in range(10)] +[chr(j) for j in range(97,103)]
# print(a)
# c=[]
# while True:
#     aa=b%16
#     b=b//16
#     c.append(a[aa])
#     if b==0:
#         break
# c.reverse()
# cc=''.join(c)
# # print(bb)
# print(cc)

# a='516113'
# a=a[::-1]
# c=0
# for i in range(len(a)):
#     for j in range(10):
#         if str(j)==a[i]:
#             c+=j*10**i
# print(c)

# a='asdfdsaa'
# b=len(a)//2
# for i in range(b):
#     if a[i]!=a[-i-1]:
#         break
# else:
#     print(2)
#
# def zhishu(x=100):
#     aa=[str(i) for i in range(10)]+[chr(j) for j in range(97,103)]
#     a=[]
#     while True:
#         x,y=divmod(x,16)
#         a.append(aa[y])
#         if x==0:
#             break
#     a.reverse()
#     b=''.join(a)
#     print(b)
# zhishu()
import time
# a=2019-10-4
# ab=time.localtime(a)
# print(ab)
from selenium import webdriver
from time import sleep

def setup():
    global dr
    dr = webdriver.Chrome()
    dr.get('https://www.qzone.qq.com')
    sleep(2)

def tearDown():
    dr.quit()
setup()
tearDown()