########################################################################
#
#  ������ ��� ��� ���������� �����
#
#  ��������� ���� �� ����������. ��������� � ����� read_me
#
#  Copyright 2025 pk <pk@DESKTOP-5LI2RF6>
########################################################################

import csv
Yes = True
No = False

# ����-��������� �� ����������
with open('bulls.csv', mode='r') as file: #��������� �� ��������� -cp1251
   # ������� ������ reader, ������-����������� - ","
   csv_reader = csv.reader(file)
   # ���������� ������ �� CSV �����
   bulls = []
   header = next(csv_reader)
   for row in csv_reader:
      row2 = row[2]
      if len(row2) == 0:   # �������� �����������?
         bulls.append((row[0], 0.0, 0))  # �,������������ ��������,�������
      else:
         bulls.append((row[0], float(row2), 0))  # �,������������ ��������,�������

# ������, ������� ����� ���������
with open('cows.csv', mode='r') as file: #��������� �� ��������� -cp1251
   # ������� ������ reader, ������-����������� - ","
   csv_reader = csv.reader(file)
   # ���������� ������ �� CSV �����
   cows = []
   header = next(csv_reader)
   for row in csv_reader:
      row1 = row[1]
      if len(row1) == 0:   # �������� �����������?
         cows.append((row[0], 0.0))   # �,������������ ��������
      else:
         cows.append((row[0], float(row1)))  # �,������������ ��������

# ����������� ��������
with open('pedigree.csv', mode='r') as file: #��������� �� ��������� -cp1251
   # ������� ������ reader, ������-����������� - ","
   csv_reader = csv.reader(file)
   # ���������� ������ �� CSV �����
   pedigree = []
   header = next(csv_reader)
   for row in csv_reader:
      pedigree.append((row[0], row[1], row[2])) # ������������� ������, ����

# C��������� ������ ����� �� ��������
bulls.sort(key=lambda k: k[1], reverse=True)

# C��������� ������ ����� �� ��������
cows.sort(key=lambda k: k[1], reverse=True)

bull_limit = int((len(cows) + 0.5) // 10) # ����������� �� ������������� ����� -10% �����
#with open("cow_bull_assignments.csv", mode="w", encoding='utf-8') as w_file:
with open("cow_bull_assignments.csv", mode="w") as w_file:
   file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
   file_writer.writerow(["cow_id", "bull_id"])

   j = 0
   while j < len(cows):
      if len(bulls) == 0: # ������ ����� ����?
         print('The bull list is empty')  # ������ ����� ��������
         break
      else:
         i = 0
         # ������ ��������� ����
         restrictions = Yes
         while (i < len(bulls)) and (restrictions == Yes):
            restrictions = No

            if restrictions == No:
               file_writer.writerow([cows[j][0], bulls[i][0]]) # ������ � ����
               # ��������: ���� ��� �� ����� ��������� ����� 10% �����
               if bulls[i][2] >= bull_limit:
                  bulls.pop(i) # ������� ������ ��� ������� ����
               else:
                  bulls[i] = bulls[i][0], bulls[i][1], bulls[i][2] + 1 # ����������� ������� ����� ��� ������� ����
            i += 1
      j += 1

print('carried out') # ���������
