#!/usr/bin/python3
# 1. получить список файлов в каталоге
# 2. открыть файл и найти регулярками нужные данные
# 3. записать данные в общий файл


import os
import re
from ipaddress import ip_address, ip_network

#формирую список подсетей магазинов
nets = []
net_file = "D:\\VScodeWorkSpace\\070824\\-\\shops_net.txt"

with open(net_file, "r",  encoding="utf8") as net_f:
    for line in net_f.readlines():
        nets0 = list(line.strip('\n').split(","))
        nets.append(nets0)
        
#объявляю иготовый список

lf = []

file = "D:\\VScodeWorkSpace\\070824\\-\\dins.txt"

user = "admin"
ips = []

with open(str(file), "r",  encoding="utf8") as list0:
    for line in list0.readlines():
        ips0 = list(line.strip('\n').split(" "))
        ips = ips + ips0

#print(ips)

for n in ips:
                
                ip = ip_address(n)
                for ts in nets:
                    net = ip_network(ts[1])
                    if ip in net:
                        #классное применение распаковки и добавления элемента в кортеж
                        n = (n, ts[0])
                        break
                lf.append(n)
                #print(n)

with open('ipss_yealink.txt', "w", encoding="utf8") as ipss:
    for l in lf:  
        try:
            ipss.write(l + '\n')  
        except:
             print(l)