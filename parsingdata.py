# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 11:38:25 2019

@author: ASUS
"""

import xlrd
file_loc="C:\Users\ASUS\My-first-reposity\worksheet.xlsx"
wrkbk=xlrd.open_workbook(file_loc)
sheet=wrkbk.sheet_by_index(0)
print sheet.cell_value(0,0)
print sheet.nrows
print sheet.ncols
for col in range(sheet.ncols):
    print sheet.cell_value(0, col)
    print sheet.cell_value(1, col)
    print sheet.cell_value(2, col)
    
data=[[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
print type(data)