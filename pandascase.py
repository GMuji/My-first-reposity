# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 11:55:45 2019

@author: ASUS
"""

import pandas as pd
file_loc="C:\Users\ASUS\My-first-reposity\worksht.csv"
filepd=pd.read_csv(file_loc)

#print filepd.head(2)
#print filepd

file_loc1="C:\Users\ASUS\My-first-reposity\worksheet.xlsx"
filepd1=pd.read_excel(file_loc1)
#print filepd1

file_loc2="C:\Users\ASUS\My-first-reposity\worksht.txt"
filepd2=pd.read_csv(file_loc2, delimiter='\t')
print filepd2
print filepd2.columns
#print filepd2.rows
print filepd2[['Name', 'Phone']]
print filepd2.head(2)
#print filepd2.iloc[1:3] # select specific location
#print filepd2.iloc[1,2]
#print filepd2.iterrows
for ind, row in filepd2.iterrows():
    print ind, row['Name']
    
print filepd2.loc[filepd2['Name'] =="Muji4"]
print filepd2.describe()
