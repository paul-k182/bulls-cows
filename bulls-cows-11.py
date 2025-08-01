########################################################################
#
#  Подбор пар для осеменения коров
#
#  Предложен один из алгоритмов. Подробнее в файле read_me
#
#  Copyright 2025 pk <pk@DESKTOP-5LI2RF6>
########################################################################

import csv
Yes = True
No = False

# быки-кандидаты на осеменение
with open('bulls.csv', mode='r') as file: #кодировка по умолчанию -cp1251
   # Создаем объект reader, символ-разделитель - ","
   csv_reader = csv.reader(file)
   # Считывание данных из CSV файла
   bulls = []
   header = next(csv_reader)
   for row in csv_reader:
      row2 = row[2]
      if len(row2) == 0:   # значение отсутствует?
         bulls.append((row[0], 0.0, 0))  # №,селекционная ценность,счётчик
      else:
         bulls.append((row[0], float(row2), 0))  # №,селекционная ценность,счётчик

# коровы, которых нужно осеменить
with open('cows.csv', mode='r') as file: #кодировка по умолчанию -cp1251
   # Создаем объект reader, символ-разделитель - ","
   csv_reader = csv.reader(file)
   # Считывание данных из CSV файла
   cows = []
   header = next(csv_reader)
   for row in csv_reader:
      row1 = row[1]
      if len(row1) == 0:   # значение отсутствует?
         cows.append((row[0], 0.0))   # №,селекционная ценность
      else:
         cows.append((row[0], float(row1)))  # №,селекционная ценность

# родословные животных
with open('pedigree.csv', mode='r') as file: #кодировка по умолчанию -cp1251
   # Создаем объект reader, символ-разделитель - ","
   csv_reader = csv.reader(file)
   # Считывание данных из CSV файла
   pedigree = []
   header = next(csv_reader)
   for row in csv_reader:
      pedigree.append((row[0], row[1], row[2])) # идентификатор матери, отца

# Cортировка списка быков по убыванию
bulls.sort(key=lambda k: k[1], reverse=True)

# Cортировка списка коров по убыванию
cows.sort(key=lambda k: k[1], reverse=True)

bull_limit = int((len(cows) + 0.5) // 10) # Ограничение по использованию быков -10% коров
#with open("cow_bull_assignments.csv", mode="w", encoding='utf-8') as w_file:
with open("cow_bull_assignments.csv", mode="w") as w_file:
   file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
   file_writer.writerow(["cow_id", "bull_id"])

   j = 0
   while j < len(cows):
      if len(bulls) == 0: # список быков пуст?
         print('The bull list is empty')  # Список быков исчерпан
         break
      else:
         i = 0
         # Подбор очередной пары
         restrictions = Yes
         while (i < len(bulls)) and (restrictions == Yes):
            restrictions = No

            if restrictions == No:
               file_writer.writerow([cows[j][0], bulls[i][0]]) # запись в файл
               # Проверка: один бык не может осеменить более 10% коров
               if bulls[i][2] >= bull_limit:
                  bulls.pop(i) # удаляем запись для данного быка
               else:
                  bulls[i] = bulls[i][0], bulls[i][1], bulls[i][2] + 1 # увеличиваем счётчик коров для данного быка
            i += 1
      j += 1

print('carried out') # Выполнено
