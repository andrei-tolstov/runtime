#!/usr/bin/python3
import os
import re

# Указываем путь к директории ввода
directory = "D:\\VScodeWorkSpace\\070824\\-\\in\\"

# Указываем путь к директории вывода
directory_out = "D:\\VScodeWorkSpace\\070824\\-\\out\\"

# Получаем список файлов
files = os.listdir(directory)


# print(files)
for file in files:
        with open(str(directory + file), "r",  encoding="utf8") as config:
            result = config.read()
            search = re.search('<User_ID_1_                       ua="na">\d(\d{4})\d</User_ID_1_>', result)
            #search1 = re.findall('commonName=(Yealink)', result)
            #tr_for_write = str(file)
            print(search.group(1))
            
