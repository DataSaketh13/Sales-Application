#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 10:40:37 2023

@author: saketh
"""

from tkinter import *
import random

root = Tk()
root.title("Sales Application")
root.geometry("500x500")

month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
profit = (20000, 45000, 78000, 97000, 12000, 456000, 65000, 540000, 10000, 30000, 70000, 90000)

max_profit = max(profit)
max_profit_index = profit.index(max_profit)
print(max_profit_index)


max_profit_month = month[max_profit_index]
print("The maximum number of" + str(max_profit) + "was recorded in the month of" + str(max_profit_month))

min_profit = min(profit)
min_profit_index = profit.index(min_profit)
print(min_profit_index)

min_profit_month = month[min_profit_index]
print("The minimum number of" + str(min_profit) + "was recorded in the month of" + str(min_profit_month))