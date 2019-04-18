# ！/usr/bin/python
#author:xx


import xlrd
import os
from xlutils.copy import copy

def basic_file(filename=None):
	return os.path.join(os.path.dirname(__file__),filename)

# data=xlrd.open_workbook(basic_file('data.xls'))
# sheet=data.sheet_by_index(0)
# print(sheet.nrows)
# print(sheet.cell_value(3,2))

'''修改Excel中的值'''
work=xlrd.open_workbook(basic_file('data.xls'))
old=copy(work)
sheet=old.get_sheet(0)
sheet.write(9,3,'update1')
old.save(basic_file('data.xls'))