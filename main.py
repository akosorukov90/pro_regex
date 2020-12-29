import re
import csv
import collections


def search_dubl(name_list):
    dict_name = collections.defaultdict(list)
    for key, value in name_list:
        dict_name[key].append(value)
    contacts_list_new.append(contacts_list[0])
    for key, value in dict_name.items():
        if len(value) > 1:
            dubl = ['', '', '', '', '', '', '']
            for index in value:
                i = 0
                while i != 7:
                    if len(dubl[i]) >= len(contacts_list[index][i]):
                        pass
                    else:
                        dubl[i] = contacts_list[index][i]
                    i += 1
            contacts_list_new.append(dubl)
        else:
            contacts_list_new.append(contacts_list[value[0]])
    return contacts_list_new


def regex_phone(phone):
    phone = re.sub('[\s|\(|\)|\-]', '', phone)
    pattern = re.compile("(\+7|8|7)(\d{3})(\d{3})(\d{2})(\d{2})")
    phone = pattern.sub(r"+7(\2)\3-\4-\5 ", phone)
    return phone


# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
name_list = []
contacts_list_new = []
position = 0
for value in contacts_list:
    if value[0] != 'lastname':
        #Склеить и разделить ФИО
        fio = value[0] + ' ' + value[1] + ' ' + value[2]
        lastname = fio.split(' ')[0]
        firstname = fio.split(' ')[1]
        surname = fio.split(' ')[2]
        value[0] = lastname
        value[1] = firstname
        value[2] = surname

        #Регуляка исправления номеров
        phone = value[5]
        value[5] = regex_phone(phone)

        name_list.append((lastname + ' ' + firstname, position))
    position += 1

#Поиск дублей
search_dubl(name_list)

# # TODO 2: сохраните получившиеся данные в другой файл
# # код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list_new)
