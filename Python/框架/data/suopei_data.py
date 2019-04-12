#!/usr/bin/python  
#-*-coding:utf-8-*-
#userbiubiubiu
import xlrd
shuju=[]
class Suopei_duqu(object):

    def duqu_shuju(self):
        f=xlrd.open_workbook(r'E:\Python\框架\data\abcd.xlsx')
        sheet=f.sheets()[0]
        num=sheet.nrows
        for i in range(num):
            if i==0:
                continue
            else:
                shuju.append(sheet.row_values(i))
        print(shuju)
        return shuju
if __name__=='__main__':
    data=Suopei_duqu()
    data.duqu_shuju()