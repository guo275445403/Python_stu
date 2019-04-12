#!/usr/bin/python
#-*-coding:utf-8-*-
#userbiubiubiu
# aa=int(input('请问你带了多少钱:'))
# a=['电脑:188元','手机:288元','计算机:388元','iphone:18元']
# l=188,288,388,18
# sum=0
# for i,j in enumerate(a):
# 	print(i+1,j)
# while True:
# 		b =int(input('请输入购买的商品号并加入购物车'))
# 		if b==1 :
# 			sum=sum+188
# 		elif b == 6:
# 			break
# 		elif b==2 :
# 			sum=sum+288
# 		elif b==3:
# 			sum=sum+388
# 		elif b==4:
# 			sum=sum+18
# 		elif b==0 and aa>sum:
# 			print('恭喜您购买成功，本次消费共:',sum)
# 		elif b==5:
# 			print('您的余额为:',aa-sum)
# 		elif b==0 and sum>aa:
# 			print('您的余额已不足，请您及时充值!')
# 		elif b==7:
# 				print('删除你不想购买的商品就输入商品号')
# 				c=int(input('输入你要删除的商品号:'))
# 				if c==1:
# 					sum=sum-188
# 				elif c==2:
# 					sum=sum-288
# 				elif c==3:
# 					sum=sum-388
# 				elif c==4:
# 					sum=sum-18
# 		elif b==8:
# 			aaa=input('充值请输入y，不充值请输入n:')
# 			if aaa=='y':
# 				aaaa=int(input('请输入充值金额:'))
# 				print('充值成功')
# 				aa=aa+aaaa
# 			elif aaa=='n':
# 				print('不充值')
# 		print()
# 		print('请输入你要的操作，0确认购买商品5查看余额6退出本次购物7删除购物车商品8进入充值模式:')
# print('祝您购物愉快,您还剩余:',aa-sum)



# aa=int(input('请问你带了多少钱:'))
# a=[['电脑',188],['手机',288],['计算机',388],['iphone',18]]
# sum=0
# abc=[]
# for i,j in enumerate(a):
# 	print(i+1,j)
# while True:
# 	b=int(input('请输入商品号:'))
# 	abc.append(b)
# 	abc.sort()
# 	for i in range(0,b+1):
# 		sum=sum+int(a[i])


# a=input('请输入字符串,以逗号隔开:')
# b=a.split(',')
# print(b)
# c=[]
# for i in b:
# 	if i not in c:
# 		c.append(i)
# 	else:
# 		continue
# c.sort()
# print(c)
#


# 质数之和
# sum=0
# for i in range(2,100):
# 	for j in range(2,i+1):
 # 		if i%j==0:
# 			break
# 	if i==j:
# 		sum+=i
# print(sum)


# a=input('输入字符串:')
# b=a.split(',')
# c=[]
# for i in b:
# 	if i not in c:
# 		c.append(i)
# 	else:
# 		continue
# print(c)



# 选出最大和第二大的数
# a=[12,5,25,3,54]
# b=a.copy()
# b=list(set(b))
# b.sort()
# print(b)
# for i in a:
# 	if i==b[-1] or i==b[-2]:
# 		print(i)

# # 阶乘之和
# sum=0
# a=int(input('输入数字'))
# i=1
# for j in range(1,a+1):
# 	i=i*j
# 	sum+=i
# print(sum)

# 1000以内的因数之和等于本身的数
# for i in range(1,1000):
# 	sum = 0
# 	for j in range(1,i):
# 		if i%j==0:
# 			sum=sum+j
# 	if i==sum:
# 		print(i)


# 不使用int使字符串变整数
# a=input("shurushuzi")
# a=a[::-1]
# sum=0
# for i in range(len(a)):
#     for j in range(10):
#         if str(j)==a[i]:
#             sum+=j*10**i
# print(sum)


# 一个有顺序的列表，随机加入一个数，加入的数在正确的位置
# a=[2,5,8,10,16]
# b=int(input('添加一个数：'))
# for j in range(0,len(a)):
#     if b>a[j] and  b<a[j+1]:
#         a.insert(j+1,b)
# if b>=a[-1]:
#     a.append(b)
# elif b<=a[0]:
#     a.insert(0,b)
# print(a)


# 输入四个数组成三个数字
# a=input('输入4个数字:')
# a=a.split(',')
# for i in range(len(a)):
#     for j in range(len(a)):
#         for k in range(len(a)):
#             if a[i]!=a[j] and a[i]!=a[k] and a[j]!=a[k]:
#                 print(a[i]+a[j]+a[k])

# 十进制转十六进制
# def 十六进制(a):
#     aa=[str(i) for i in range(10)]+[chr(j) for j in range(97,103) ]
#     c=[]
#     while True:
#         a,b=divmod(a,16)
#         c.append(aa[b])
#         if a==0:
#             break
#     c.reverse()
#     d=''
#     for i in range(len(c)):
#         d+=c[i]
#     print(d)
#     return d
# 十六进制(100)

# f=open(r'E:\Python\a.txt','r',encoding='utf-8')
# a=f.readlines()
# f.close()
# for i in a:
#     if '#' not in i or '\n' not in i:
#         a.remove(i)
# print(len(a))


#在文件中打印99乘法表
# d=open(r'E:\Python\a.txt','a',encoding='utf-8')
# for i in range(1,10):
#     for j in range(1,i+1):
#         d.write('{}*{}={}\t'.format(j,i,i*j))
#     d.write('\n')
# d.close()

#
# def jiujiu():
#     for i in range(1,10):
#         for j in range(1,i+1):
#             print('{}*{}={}'.format(j,i,j*i),end='\t')
#         print()


# def aaa(a=100):
#     sum=0
#     for i in range(2,a):
#         for j in range(2,i+1):
#             if i%j==0:
#                 break
#         if i==j:
#             sum+=i
#     print(sum)
# aaa()



# a=open(r'E:\python\a.txt','r+',encoding='utf-8')
# b=a.readlines()
# a.close()
# for i in range(9,15):
#     c=b[i]
#     print(c)

# a=input('输入数组:')
# c=a.split(',')
# print(c)
# b=int(input("请输入数字"))
# for i in range(len(c)-1):
#     if int(c[i])+int(c[i+1])==b:
#         print(c[i],c[i+1])



# 把文件中的内容导入到excel表格中
# import xlwt
# with open('c.txt','r', encoding='utf-8') as aaa:
# 	b=aaa.readlines()
# f =xlwt.Workbook(encoding='utf - 8')
# sheet = f.add_sheet('excel学习')
# for i,j in enumerate(b):
# 	j=j.strip().split(',')
# 	for k in range(len(j)):
# 		sheet.write(i,k,j[k])
# f.save('666.xls')


# excel导入文件
# import xlrd
# f=xlrd.open_workbook('666.xls')
# sheet=f.sheets()[0]
# with open('c.txt','w',encoding='utf-8') as f1:
#     for i in range(sheet.nrows):
#         a=sheet.row_values(i)
#         print(a)
#         for j in a:
#             if j==a[-1] :
#                 f1.write(j+'\n')
#             else:
#                 f1.write(j+',')


# from xlutils.copy import copy
# import  xlrd
# f=xlrd.open_workbook('666.xls')
# print(f.sheet_names())
# sheet=f.sheets()[0]
# print(sheet.nrows)
# print(sheet.row_values(1))
# print(sheet.col_values(4))
# print(sheet.cell(1,4).value)



# import os
# for i in range(10):
#     a=os.mkdir('{}.txt'.format(i))
#     with open('{}.txt'.format(i),'w',encoding='utf-8') as f:
#         f.write('asdasdasd')
# import xlrd
# f=xlrd.open_workbook('666.xls')
# sheet=f.sheets()[0]
# for i in range(4):
#     sheet.col_values(i)


# # import pymysql
# # #连接数据库
# # conn=pymysql.connect(host='192.168.0.118',port=3306,user='root',password='123456',charset='utf8')
# # #创建游标
# # abc=conn.cursor()
# # #执行sql语句
# # abc.execute('show databases;')
# # print(abc.fetchall())
# # #结果需要一有容器去接收
# #  #只接收上一个sql语句的结果
# # abc.execute('use zuoye1;')
# # abc.execute('create table dianying3(名称 char(255),导演 char(255),影评 char(255),人数 char (255));')
# # f=xlrd.open_workbook('666.xls')
# # sheet=f.sheets()[0]
# # for i in range(1,sheet.nrows):
# #     a=sheet.row_values(i)
# #     print(a)
# #     abc.execute('insert into dianying3 values("{}","{}","{}","{}")'.format(a[0],a[1],a[2],a[3]))
# # abc=abc.fetchall()
# # print(abc)
# # conn.close()
#
#
# import  pymysql
# conn=pymysql.connect(host='192.168.0.118',password='123456',user='root',charset='utf8',port=3306)
# neirong=[]
# with open('c.txt','r',encoding='utf-8')as f:
#     neirong1=f.readlines()
#     for i in neirong1:
#         a=i.strip().split(',')
#         neirong.append(a)
# fubiao=conn.cursor()
# fubiao.execute('use zuoye1;')
# print(fubiao.fetchall())
# # fubiao.execute('create table dianying2(mingcheng char(255),daoyan char(255),yingping char(255),renshu char(255));')
# for i in range(1,len(neirong)):
# print(neirong)
#         print(i)
#         fubiao.execute('insert into dianying2 values("{}","{}","{}","{}");'.format(neirong[i][0],neirong[i][1],neirong[i][2],neirong[i][3]))
#         conn.commit()
#         print(fubiao.fetchall())
# conn.close()
#
#
# import threading,time
# from time import sleep
# def asd():
#     for i in range(3):
#         print('laji')
#         sleep(3)
# def qwe():
#     for i in range(3):
#         print('shit up')
#         sleep(3)
# threading.Thread(target=asd).start()
# threading.Thread(target=qwe).start()



import time
# a=int(input('!!!'))
# aa=131313132
# b=time.localtime()
# c=time.strftime('%F',b)
# aa=input('!!!')
# aaa=time.strptime(aa,'%Y-%m-%d')
# abc=time.mktime(aaa)
# abc=abc-86400
# abcd=time.localtime(abc)
# print(abcd)
# abcde=time.strftime('%F',abcd)
# print(c)
# print(aaa[0])
# if aaa[0] %100!=0:
#     if aaa[0] % 4 ==0:
#         print('{}是闰年'.format(aaa[0]))
#     else:
#         print('{}不是闰年'.format(aaa[0]))
# elif aaa[0] % 400==0:
#     print('{}是闰年'.format(aaa[0]))
# print('今天是星期{},今天是一年中的第{}天'.format(aaa[-3]+1,aaa[-2]))



# import smtplib,email.mime.multipart,email.mime.text
# server='smtp.163.com' #邮件地址服务器
# from_user='18348326189@163.com'#发件人
# res='18339914556@163.com'#收件人
# passwd='fei123456789'#授权码 允许登陆客户端的
# #创建一个空邮件
# message=email.mime.multipart.MIMEMultipart()
# message['From']=from_user #写入发件人
# message['To']=res         #邮件的接收者
# message['Subjoct']='垃圾'
# text="""askdmasmdlmaldm'
# 垃圾，吃啥饭啊
# 卡神秘代码收款码魔卡什么的拉屎拉开大垃圾阿两大类阿萨德卡卡的爱可可鞍山市
# laji"""
# #编码方式
# tet=email.mime.text.MIMEText(text,'plain','utf-8')
# message.attach(tet)


# #连接服务器
# smtp123=smtplib.SMTP_SSL(server,465)
# #登陆服务器
# smtp123.login(from_user,passwd)
# #发送邮件（发送者，接收者，内容改为字符串）
# smtp123.sendmail(from_user,res,message.as_string())
# smtp123.close()
#
# #发送带附件，对附件进行读取和编码
# att2=email.mime.text.MIMEText(open('6666.xls','rb').read(),'base64','utg-8')
# att2["Content-Type"]='application/octet-stream'
# att2["Content-Disposition"]='attachment;filename="666.xls"'
# message.attach(att2)
# #连接服务器
# smtp123=smtplib.SMTP_SSL(server,465)
# #登陆服务器
# smtp123.login(from_user,passwd)
# #发送邮件（发送者，接收者，内容改为字符串）
# smtp123.sendmail(from_user,res,message.as_string())
# smtp123.close()

# import  pymysql,xlwt
# conn=pymysql.connect(host='192.168.0.118',password='123456',user='root',charset='utf8',port=3306)
# fubiao=conn.cursor()
# fubiao.execute('use zuoye1')
# fubiao.execute('select * from dianying2')
# a=fubiao.fetchall()
# b=[]
# for j in a:
#     b.append(j)
# print(b)

# f=xlwt.Workbook()
# sheet=f.add_sheet('666')
# for i,j in enumerate(b):
#     for k in range(len(j)):
#         sheet.write(i,k,j[k])
# f.save('66666.xls')






import paramiko
# with paramiko.SSHClient() as ssh123:
#     ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy)
#     #连接主机
#     ssh123.connect(hostname='192.168.0.118',port=22,username='root',password='19961224')
#     while True:
#         try:
#             abc=input('!!!')
#             if abc!=exit:
#                 a,b,c=ssh123.exec_command(abc)
#                 print(b.read().decode())
#             else:
#                 break
#         except:
#             continue

#
# ssh123=paramiko.Transport('192.168.0.118',22)
# ssh123.connect(username='root',password='19961224')
# # 创建一个传输文件的对象
# sfps=paramiko.SFTPClient.from_transport(ssh123)
# #从linux带windonws 第一个参数是要传输的文件。第二个是接收的文件
# sfps.put(r'E:\Python\g.sh',r'/home/gb.sh')
# ssh123.close()

# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('192.168.0.31',6888))
# s.listen(3)
# while True:
#     #接收请求,会产生两个值,第一个连接信息,第二客户端的ip和端口号
#     conn,addr=s.accept()
#     #接收数据 1024表示一次最大能接收的字节
#     shuju=conn.recv(1024)
#     print(shuju.decode('utf-8'))
#     #发送数据
#     msg=input('!!!')
#     conn.send(msg.encode('utf-8'))


# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind(('127.0.0.1',9888))
# while True:
#     #接收请求,会产生两个值,第一个连接信息,第二客户端的ip和端口号
#     conn,addr=s.recvfrom(1024)
#     #接收数据 1024表示一次最大能接收的字节
#     print(conn.decode('utf-8'))
#     s.sendto('相应的数据'.encode('utf-8'),addr)

# from tkinter import *
# from tkinter import messagebox
# from PIL import Image,ImageTk
# # def closewindows():
# #     messagebox.showinfo(title='你是真的辣鸡',message='关不掉')
#     # return
# def love():
#     #创建一个顶级窗口，依赖原始窗口存在
#     love=Toplevel(windows)
#     love.title('赵又廷，夺妻之恨不共戴天')
#     love.geometry('300x200+300+100')
# def love1():
#     pass
# #创建一个窗口
# windows=Tk()
# #命名窗口标题
# windows.title('看图猜美女')
# #修改窗口大小
# windows.geometry('720x570+300+100')
# #设置窗口的位置
# # windows.geometry('')
# #当关闭窗口时触发
# # windows.protocol('WM_DELETE_WINDOW',closewindows)
# #显示窗口
# ladel=Label(windows,text='她是谁',font=("宋体",20))
# #显示标签
# ladel.grid(row=0,column=1,sticky=W)
# #添加图片
# # imag=PhotoImage(file='1.gif')
# # image=Label(windows,image=imag)
# # image.grid(row=2,columnspan=2)
# photo=Image.open('1.jpg')
# phot=ImageTk.PhotoImage(photo)
# pho=Label(windows,image=phot)
# #显示数据
# pho.grid(row=1,columnspan=2)
# #添加一个按钮
# botten=Button(windows,text='高圆圆',font=('宋体',10),width=6,height=3,command=love)
# botten.grid(row=2,column=0,sticky=W)
# botten1=Button(windows,text='罗玉凤',font=('宋体',10),width=6,height=3,command=love1)
# botten1.grid(row=2,column=1,sticky=E)
#
# windows.mainloop()

# def shiliu(x):
#     a=[str(i) for i in range(10)]+[chr(j) for j in range(97,103)]
#     b=[]
#     while True:
#         x,y=divmod(x,16)
#         b.append(a[y])
#         if x==0:
#             break
#     b.reverse()
#     c=''.join(b)
#     print(c)
# shiliu(100)
import unittest
from ddt import ddt,data,unpack
from selenium import webdriver
dr=webdriver.Chrome()
# @ddt
# class MyTesting(unittest.TestCase):
#     def setUp(self):
#         print('this is the setUp')
#     @data([1,2,3])
#     def test_1(self,value):
#         print(value)
# a=MyTesting()
# if __name__=='__main__':
#         unittest.main()
