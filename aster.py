#!/usr/bin/python3
# 1. получить список файлов в каталоге
# 2. открыть файл и найти регулярками нужные данные
# 3. записать данные в общий файл
#

import os
import re

# Указываем путь к директории
directory = "C:\\vscode\\configs\\yealink\\"

# Получаем список файлов
files = os.listdir(directory)

# print(files)
with open('users.sql', "w", encoding="utf8") as users:
    users.write('# количестово файлов для обработки ' + str(len(files)) + '\n')
    for file in files:
        try:
            with open(str(directory + file), "r", encoding="utf8") as config:
                result = config.read()
                user_name = re.search(r"account.1.user_name =\s*(.*)", result)
                password = re.search(r"account.1.password =\s*(.*)", result)
                display_name = re.search(r"account.1.display_name =\s*(.*)", result)
                #print(user_name.group(1))
                #print(password.group(1)) 
            users.write('# ' + str(files.index(file)) + ' '  + directory + file + '\n')
        except Exception as err:
            with open('error.txt', "a") as errors:
                        errors.write(file + '  ' + f"Unexpected {err=}, {type(err)=}+ '\n'")                
        try:
            users.write('INSERT INTO `ps_aors` (`id`, `max_contacts`, `qualify_frequency`) VALUES (' + user_name.group(1) + ', 3, 60);\n')
            users.write("INSERT INTO `ps_auths` (`id`, `auth_type`, `password`, `username`) VALUES (" + user_name.group(1) + ", 'userpass', '" + password.group(1) + "', " + user_name.group(1) + ");\n")
            users.write("INSERT INTO `ps_endpoints` (`id`, `password`, `callerid`, `transport`, `aors`, `auth`, `context`, `disallow`, `allow`, `direct_media`, `deny`, `permit`, `mailboxes`) VALUES (" + user_name.group(1) + ", '" + password.group(1) + "', '" + display_name.group(1) + "', 'transport-udp', '" + user_name.group(1) +"', '" + user_name.group(1) +"', 'MainDial', 'all', 'opus,ulaw,alaw', 'no', '0.0.0.0/0', '0.0.0.0/0', '" + user_name.group(1) +"@default' );\n")
        except Exception as err:
            with open('error.txt', "a") as errors:
                        errors.write(file + '  ' + f"Unexpected {err=}, {type(err)=}+ '\n'")

# INSERT INTO `ps_auths` (`id`, `auth_type`, `password`, `username`) VALUES (177777, 'userpass', 'L29lOwngsg', 177777);
# insert into ps_auths (id, auth_type, password, username) values (100, 'userpass', 100, 100);
# insert into ps_endpoints (id, transport, aors, auth, context, disallow, allow, direct_media, deny, permit, mailboxes) values (100, 'transport-udp', '100', '100', 'testing', 'all', 'ulaw,alaw,gsm', 'no', '0.0.0.0/0', '0.0.0.0/0', '100@default');