import os
import zipfile
test_zip = zipfile.ZipFile('C:\\Users\\Ульяночка\\PycharmProjects\\lab_1\\archive.zip')

#Задание 1
print('---------------------------------Извлечение всех файлов из архива в директорию---------------------------------')
destination = 'C:\\Users\\Ульяночка\\PycharmProjects\\lab_1\\folder'
test_zip.extractall(destination)
print('the archive has been unzipped')
test_zip.close()

list = os.listdir(destination)
print(list)

#Задание 2
print('-------------------------------------------Поиск всех файлов формата txt---------------------------------------')
txt_files = []
for dirpath, dirnames, filenames in os.walk('.'):
    #for dirname in dirnames:  # перебрать каталоги
        #print("Каталог:", os.path.join(dirpath, dirname))

    destination = 'C:\\Users\\Ульяночка\\PycharmProjects\\lab_1'
    for filename in filenames:  # перебрать файлы
        # print("Файл:\t", os.path.join(dirpath, filename))
        if filename.endswith('.txt'):
            txt_files.append(destination + (os.path.join(dirpath, filename))[1::])

# print('\ntxt файл:\t '.join(txt_files))                                       печать списка текстовых файлов
# print('\n ----------------------------------------------- \n')

import hashlib

for filename in txt_files:  # печать списка текстовых файлов
    target_file_data = open(filename, 'rb').read()
    result = hashlib.md5(target_file_data).hexdigest()
    print('{:100s}'.format(filename), result)
print('\n ----------------------------------------------- \n')

#Задание 3
print('-------------------------------------------Поиск файла по заданному хешу----------------------------------------')
target_hash = "4636f9ae9fef12ebd56cd39586d33cfb"                                 # поиск файла по его хешу
target_file = " "
target_file_way = " "
target_file_data = " "
for dirpath, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        path = dirpath + '/' + filename
        tmp = open(path, "rb").read()
        tmp_data = hashlib.md5(tmp).hexdigest()
        if tmp_data == target_hash:
            target_file_data = tmp
            target_file_way = destination + path[1::]
            target_file_hash = tmp_data
            break
print(target_file_data)
print(target_file_way)
print('\n Полученный хеш: \t' + target_file_hash)
print('\n Искомый хеш: \t\t' + target_hash)

#Задание 4
print('---------------------------------------Парсинг страницы по полученному хешу------------------------------------')
import requests
import re

r = requests.get(target_file_data)
result_dct = {}                                                                     # словарь для записи содержимого таблицы

counter = 0

lines = re.findall(r'<div class="Table-module_row__3TH83">.*?</div>.*?</div>.*?</div>.*?</div>.*?</div>', r.text)       # Получение списка строк таблицы
for line in lines:
    if counter == 0:                                                                # извлечение заголовков таблицы
        headers = re.sub("<.*?>", " ", line)                                        # Удаление тегов
        headers = re.findall("Заболели|Умерли|Вылечились|Активные случаи", headers) # Извлечение списка заголовков
    temp = re.sub("<.*?>", ';', line)
    temp = re.sub(r'\(.*?\)', '', temp)
    temp = re.sub(r'\xa0', '', temp)
    temp = re.sub(r'\s', ';', temp)
    temp = re.sub(r'\;;+', '!', temp)
    temp = re.sub(';', ' ', temp)
    temp = re.sub(r'^\!+|\s+$', '', temp)
    temp = re.sub(r'^\W+', '', temp)
    temp = re.sub(r'^\!', '', temp)
    temp = re.sub('_', '-1', temp)
    temp = re.sub(r'[*]', '', temp)
    tmp_split = re.split(r'\!', temp)
    if tmp_split != headers:
        country_name = tmp_split[0]
        result_dct[country_name] = [0, 0, 0, 0]
        for i in range(4):
            result_dct[country_name][i] = int(tmp_split[i+1])
    counter += 1
print(headers)
for key, value in result_dct.items():
    print('{:30s}'.format(key), ':',value) #хотела вывести красиво с табуляцией, почему-то не получилось...
#print('\n'.join(lines))

#Задание 5
print('----------------------------------------Запись данных из словаря в файл----------------------------------------')
import csv
output = open('data.csv', 'w')
file_writer = csv.writer(output, delimiter=";")
file_writer.writerow(headers)
for key in result_dct.keys():
    file_writer.writerow([key, result_dct[key][0], result_dct[key][1], result_dct[key][2], result_dct[key][3]])
output.close()

#Задание 6
print('-------------------------------------------Вывод данных таблицы по ключу---------------------------------------')

target_country = input("Введите название страны: ")
print(headers)
print(result_dct[target_country])
