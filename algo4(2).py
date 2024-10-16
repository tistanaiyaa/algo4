# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 23:01:35 2024

@author: Lenovo
"""

while True: 
    month = int(input("enter the month (1-12): "))
    if month == -1:
        print("program stopped.")
    else:
        year = int(input("please enter the year (eg.,2023): "))
    if month in [1,3,5,7,8,10,12]:
        print("there are 31 days in the month")
    elif month in [4,6,9,11]:
        print("there are 30 days in a month")
    #tahun kabisat
    elif month == 2:
        if (year%400==0)or(year%100!= 0 and year%4 == 0):
            print("there are 29 days in the month")
        else:
            print("there are 28 days in the month")