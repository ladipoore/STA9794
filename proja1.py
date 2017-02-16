# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 00:40:38 2017

@author: Oore
"""
from statistics import mean

names = ["datetime", "price", "volume"]
f = open("data-small.txt", 'r')

datetime=[]
price=[]
volume=[]

for line in f:
    line = line.strip()
    columns = line.split(",")
    datetime.append(columns[0])
    price.append(float(columns[1]))
    volume.append(int(columns[2]))
print(mean(price))



    



