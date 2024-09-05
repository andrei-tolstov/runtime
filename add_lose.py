import os
import re

in_file = "C:\\vscode\\-\\ast.txt"

endpoints = {}

with open(in_file, "r", encoding="utf8") as f:
    for i in f.readlines():
        if 'No matching endpoint found' in i :
            with open('only_endp.txt', 'a', encoding="utf8") as f2:
                f2.write(i)

with open('only_endp.txt', "r", encoding="utf8") as f:
    for i in f.readlines():
            try:
                user_name = re.search(r'"(.*)"', i)
                ip = re.search(r"([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})", i)
                endpoint = re.search(r":(\d*)@", i)
                endpoints.update({(endpoint.group(1) if endpoint is not None else 'Not found'): [(ip.group(1) if ip is not None else 'Not found')  , (user_name.group(1) if user_name is not None else 'Not found')]})

          
            except Exception as err:
                print(err)


endpoints = sorted(endpoints.items())
endpoints = dict(endpoints)
#print(endpoints)
with open('enpdo.txt', "w", encoding="utf8") as f:
     for i in endpoints:
          value = endpoints[i]
          f.write(i + str(value) + "\n")

