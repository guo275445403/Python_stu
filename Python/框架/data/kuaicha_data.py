#!/usr/bin/python  
#-*-coding:utf-8-*-
#userbiubiubiu
import xlrd
shuju=[]
class Kuaicha_data(object):

    def duqu_kuaicha(self):
        f=xlrd.open_workbook(r'E:\Python\框架\data\666.xlsx')
        sheet=f.sheets()[0]
        num=sheet.nrows
        for i in range(num):
            if i==0:
                continue
            else:
                shuju.append(sheet.row_values(i))
        return shuju
if __name__=='__main__':
    data=Kuaicha_data()
    data.duqu_kuaicha()