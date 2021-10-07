import os

import zipfile

test_zip = zipfile.ZipFile('C:\\Users\\Ульяночка\\PycharmProjects\\lab_1\\archive.zip')

# test_zip_files = test_zip.namelist()
# print(test_zip_files)

print('---------------------------------Извлечение всех файлов из архива в директорию---------------------------------')
destination = 'C:\\Users\\Ульяночка\\PycharmProjects\\lab_1\\folder'
test_zip.extractall(destination)
print('the archive has been unzipped')

test_zip.close()

list = os.listdir(destination)
# test= filter(lambda x: x.endswith('.txt'), list)
# print(test)
print(list)

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

print('---------------------------------------Парсинг страницы по полученному хешу------------------------------------')

import requests
import re

r = requests.get(target_file_data)
result_dct = {}                                                                 # словарь для записи содержимого таблицы

counter = 0

lines = re.findall(r'<div class="Table-module_row__3TH83">.*?</div>.*?</div>.*?</div>.*?</div>.*?</div>', r.text)       # Получение списка строк таблицы
for line in lines:
    if counter == 0:                                                            # извлечение заголовков таблицы
        headers = re.sub("<.*?>", ';', line)                                    # Удаление тегов
        headers = re.findall("<.*?>", '', headers)                              # Извлечение списка заголовков
print('\n'.join(lines))

        # TODO


    # Значения в таблице, заключенные в скобках, не учитывать. Для этого удалить скобки и символы между ними.
    # Замена последовательности символов ';' на одиночный символ
    # Удаление символа ';' в начале и в конце строки

    # TODO

    # Разбитие строки на подстроки
    tmp_split = ...

    # Извлечение и обработка (удаление "лишних" символов) данных из первого столбца
    country_name = tmp_split[0]

    # TODO

    # Извлечение данных из оставшихся столбцов. Данные из этих столбцов должны иметь числовое значение (прочерк можно заменить на -1).
    # Некоторые строки содержат пробелы в виде символа '\xa0'.
    col1_val = ...
    col2_val = ...
    col3_val = ...
    col4_val = ...

    # Запись извлеченных данных в словарь
    result_dct[country_name] = ...
    result_dct[country_name][...] = int(col1_val)
    result_dct[country_name][...] = int(col2_val)
    result_dct[country_name][...] = int(col3_val)
    result_dct[country_name][...] = int(col4_val)

    counter += 1
