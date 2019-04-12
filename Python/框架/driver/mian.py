
#!/usr/bin/python
#-*-coding:utf-8-*-
#userbiubiubiu
from 框架.report.baogao import baogao

def run(aa):
    baogao(aa)
with open(r'E:\Python\框架\driver\回归.txt','r')as f:
    a = f.readlines()
    if a[0] == 'all':
        run('*')
    else:
        run(a)