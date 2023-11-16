#Если слово из первого файла есть во втором, то к слову из первого файла добавляется слово из второго файла. Если слова из первого файла нет о втором файле - оно остается одно.

import csv

def merge_csv(input_file1, input_file2, output_file):
    # Чтение второго CSV файла и создание словаря с парами (слово, значение)
    with open(input_file2, 'r', newline='', encoding='utf-8') as file2:
        reader2 = csv.reader(file2)
        word_value_dict = {row[0]: row[1] for row in reader2}

    # Обработка первого CSV файла
    with open(input_file1, 'r', newline='', encoding='utf-8') as file1:
        reader1 = csv.reader(file1)
        data = []
        for row in reader1:
            word = row[0]
            value = word_value_dict.get(word, '')
            row.append(value)
            data.append(row)

    # Запись результата в новый CSV файл
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(data)

# запускаем функцию
merge_csv('input1.csv', 'input2.csv', 'output.csv')
