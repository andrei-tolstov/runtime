file_source_list = "/home/andrei/vscode/271124/runtime/sort_list/in/all_ips_Продуктив.txt"

file_no_access_tolstov = "/home/andrei/vscode/271124/runtime/sort_list/in/tols_all.txt"
file_no_access_bogdanov = "/home/andrei/vscode/271124/runtime/sort_list/in/bog_all.txt"
file_no_access_golubenkov = "/home/andrei/vscode/271124/runtime/sort_list/in/gol_all.txt"

file_out_tolstov = "/home/andrei/vscode/271124/runtime/sort_list/out/out_tolstov.txt"
file_out_bogdanov = "/home/andrei/vscode/271124/runtime/sort_list/out/out_bogdanov.txt"
file_out_golubenkov = "/home/andrei/vscode/271124/runtime/sort_list/out/out_golubenkov.txt"
file_out_no_access = "/home/andrei/vscode/271124/runtime/sort_list/out/out_no_access.txt"
# формирую списки для обработки

source_list = []

no_access_tolstov = []
no_access_bogdanov = []
no_access_golubenkov = []


# функция формирования списка из файла
def file_to_list(file, list):
    with open(str(file), "r",  encoding="utf8") as l:
        for line in l.readlines():
            if line.strip('\n') != "":
                list.append(line.strip('\n'))


file_to_list(file_source_list, source_list)
file_to_list(file_no_access_tolstov, no_access_tolstov)
file_to_list(file_no_access_bogdanov, no_access_bogdanov)
file_to_list(file_no_access_golubenkov, no_access_golubenkov)


out_range = []
out_tolstov = []
out_bogdanov = []
out_golubenkov = []
out_all = []

share_dict = {
    "out_tolstov": no_access_tolstov,
    "out_bogdanov": no_access_bogdanov,
    "out_golubenkov": no_access_golubenkov
}




# функция записи списка в файл
def list_to_file(file, list):
    with open(str(file), "w", encoding="utf8") as l:
        for line in list:
            l.write(line + '\n')


# функция выбора списка для заполнения
def select_list(list):
    list.sort(key=len)
    if len(list) > 0:
        return list[0]
    


# функция проверки ip
def check_ip(ip, list):
    if list == out_tolstov:
        var = "out_tolstov"
    elif list == out_bogdanov:
        var = "out_bogdanov"
    else:
        var = "out_golubenkov"
    if ip in share_dict.get(var):
        return False
    else:
        return True
    

# заполнение списков
for ip in source_list:
    list_for_select = [out_tolstov, out_bogdanov, out_golubenkov]
    while True:
        if len(list_for_select) == 0:
            out_all.append(ip)
            break
        sel_list = select_list(list_for_select)
        if check_ip(ip, sel_list):
            sel_list.append(ip)
            break
        else:
            list_for_select.remove(sel_list)

list_to_file(file_out_tolstov, out_tolstov)
list_to_file(file_out_bogdanov, out_bogdanov)
list_to_file(file_out_golubenkov, out_golubenkov)
list_to_file(file_out_no_access, out_all)
             
             
