#!/usr/bin/python  
#-*-coding:utf-8-*-
#userbiubiubiu
import xlrd

class Diandan_data(object):

    def diandan_shuju(self):
        shuju = []
        f=xlrd.open_workbook(r'E:\Python\框架\data\abcd.xlsx')
        sheet=f.sheets()[0]
        num=sheet.nrows
        for i in range(num):
            if i==0:
                continue
            else:
                shuju.append(sheet.row_values(i))
        return shuju