#!/usr/bin/python3
# 1. получить список файлов в каталоге
# 2. открыть файл и найти регулярками нужные данные
# 3. записать данные в общий файл
#

import os
import re

# Указываем путь к директории
directory = "/home/testdeb/-/python/X1S/"

# Указываем путь к директории новых файлов
new_directory = "/home/testdeb/-/python/X1Snew/"

# Получаем список файлов
files = os.listdir(directory)

#print(files)

for file in files:
    with open(str(directory + file), "r", encoding="latin-1") as config:
        result = config.read()
        Phone_Number = re.search(r"SIP1 Phone Number\s*:\s*(.*)", result)
        Display_Name = re.search(r"SIP1 Display Name\s*:\s*(.*)", result)
        user_name = re.search(r"SIP1 Register User\s*:\s*(.*)", result)
        password = re.search(r"SIP1 Register Pswd\s*:\s*(.*)", result)
        #print(user_name.group(1))
        #print(password.group(1)) 
        with open(str(new_directory + file), "w", encoding="latin-1") as fix_file:        
            try:
                fix_file.write('<<VOIP CONFIG FILE>>Version:2.0000000000\n\n')
                fix_file.write('<SIP CONFIG MODULE>\n--SIP Line List--  :\n')
                fix_file.write(Phone_Number.group() + '\n')
                fix_file.write(Display_Name.group() + "\n")
                fix_file.write(user_name.group() + '\n')
                fix_file.write(password.group() + "\n")
                fix_file.write('<<END OF FILE>>')
            except Exception as err:
                with open('error.txt', "a") as errors:
                            errors.write(file + '  ' + f"Unexpected {err=}, {type(err)=}+ '\n'")
