import datetime as dt
import time as time
import os


raw = {
    'M009': (dt.time(5,38), dt.time(6,18)),
    'M046': (dt.time(6,38), dt.time(7,20)),
    'M071': (dt.time(7,31), dt.time(8,16)),
    'M118': (dt.time(8,33), dt.time(9,15)),
    'M161': (dt.time(10,37), dt.time(11,34)),
    'M182': (dt.time(11,59), dt.time(12,43))      
}

tn = list(raw.keys())
schedule = list(raw.values())

td = dt.datetime(1,1,1)
for i in raw.keys():
    k = raw[i]

with open("mtr_duty.json", 'r', encoding="utf-8") as duty:
    print(duty)