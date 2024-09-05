#!/usr/bin/python3
# 1. получить список файлов в каталоге
# 2. открыть файл и найти регулярками нужные данные
# 3. записать данные в общий файл


import os
import re
from ipaddress import ip_address, ip_network

# Указываем путь к директории ввода
directory = "D:\\VScodeWorkSpace\\070824\\-\\in\\"

# Указываем путь к директории вывода
directory_out = "D:\\VScodeWorkSpace\\070824\\-\\out\\"

# Получаем список файлов
files = os.listdir(directory)

#формирую список подсетей магазинов
nets = []
net_file = "D:\\VScodeWorkSpace\\070824\\-\\shops_net.txt"

with open(net_file, "r",  encoding="utf8") as net_f:
    for line in net_f.readlines():
        nets0 = list(line.strip('\n').split(","))
        nets.append(nets0)
        
#объявляю иготовый список

lf = []

#объявляю временный список

temp_list = []

# for ns in nets:
#     print(ns)

# print(files)
for file in files:
        with open(str(directory + file), "r",  encoding="utf8") as config:
            result = config.read()
            search = re.findall('(.{12}\.cfg)\s.*\s([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})', result)
            #search1 = re.findall('commonName=(Yealink)', result)
            #tr_for_write = str(file)
            search = list(set(search))
            print(str(len(search)))
            
            for n in search:
                
                ip = ip_address(n[1])
                for ts in nets:
                    net = ip_network(ts[1])
                    if ip in net:
                        #классное применение распаковки и добавления элемента в кортеж
                        n = (*n, ts[0])
                        break
                lf.append(n)
                print(n)

for el in lf:
    if len(el) == 3:
        with open(directory_out + el[0], "w",  encoding="utf8") as cfg:
            user_name = "3" + str(el[2]) + "1"
            while user_name in temp_list:
                user_name = str(int(user_name) + 1)
            
            temp_list.append(user_name)
            password = user_name + "y"
            display_name = "Магазин " + user_name[1:-1] + "-" + user_name[5:]
            #print(user_name, password, display_name)
            cfg.write('#!version:1.0.0.2\n')
            cfg.write('## the file header "#!version:1.0.0.1" can not be edited or deleted. ##\n\n')
            cfg.write('account.1.auth_name = ' + user_name + '\n')
            cfg.write('account.1.label = ' + user_name + '\n')
            cfg.write('account.1.user_name = ' + user_name + '\n')
            cfg.write('account.1.password = ' + password + '\n')
            cfg.write('account.1.display_name = ' + display_name + '\n')
            cfg.write('account.1.outbound_proxy_enable = 0\n')
            cfg.write('account.1.shared_line = 0\n')
            cfg.write('account.1.enable = 1\n')
  
