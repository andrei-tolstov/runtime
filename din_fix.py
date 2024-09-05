#!/usr/bin/python3
# 1. получить список файлов в каталоге
# 2. открыть файл и найти регулярками нужные данные
# 3. записать данные в общий файл
#

import os
import re

# Указываем путь к директории
directory = "D:\\VScodeWorkSpace\\070824\\-\\in\\"

# Указываем путь к директории новых файлов
new_directory = "D:\\VScodeWorkSpace\\070824\\-\\out\\"

# Получаем список файлов
files = os.listdir(directory)

#print(files)

for file in files:
    with open(str(directory + file), "r", encoding="utf-8") as config:
        result = config.read()
        Display_Name = re.search(r"Config.Account1.GENERAL.DisplayName\s*=\s*(.*)", result)
        user_name = re.search(r"Config.Account1.GENERAL.UserName\s*=\s*(.*)", result)
        password = re.search(r"Config.Account1.GENERAL.Pwd\s*=\s*(.*)", result)
        #print(user_name.group(1))
        #print(password.group(1)) 
        with open(str(new_directory + file), "w", encoding="utf-8") as fix_file:        
            try:
                fix_file.write('Config.Autoprovision.CFG.Version = 2\n\n')
                fix_file.write('Config.Account1.GENERAL.Label = ' + user_name.group(1) + "\n")
                fix_file.write('Config.Account1.GENERAL.DisplayName = ' + Display_Name.group(1) + '\n')
                fix_file.write('Config.Account1.GENERAL.UserName = ' + user_name.group(1) + "\n")
                fix_file.write('Config.Account1.GENERAL.AuthName = ' + user_name.group(1) + "\n")
                fix_file.write('Config.Account1.GENERAL.Pwd = ' + password.group(1) + "\n")
                fix_file.write('Config.Firmware.Url = http://msk-co-yealink.ivoin.ru/c60u/2.60.11.12.11.rom\n')
                fix_file.write('Config.Autoprovision.MODE.Mode = 4\n')
            except Exception as err:
                with open('error.txt', "a") as errors:
                            errors.write(file + '  ' + f"Unexpected {err=}, {type(err)=}+ '\n'")
