# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:17:00 2019

@author: Rb
"""

"""
  1.)

Создать программно файл в текстовом формате, записать в него построчно данные, 
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""
import sys
with open('my_file.txt', "w") as f_to_read:
    
    string = " "
    while True:
        string = input('Give me a string: ')
        if len(string) > 0: 
            string=string+'\n'
        else:
            break
        try:
            f_to_read.write(string)
        except:
            print('IO Error')
            sys.exit(0)

        print(string)


print('======================================================================')
print('======================================================================')

"""
  2.)
Создать текстовый файл (не программно), сохранить в нем несколько строк, 
выполнить подсчет количества строк, количества слов в каждой строке.    
"""
try: 
    with open('my_file.txt', "r") as f_to_read:
        content = f_to_read.readlines()
        for i, line in  enumerate( content ):
            line = line.replace('\n','')
            print(line)
            line = line.split()
            print(f'line {i} contain {len(line)} words')
except:
    print('IO Error')
    sys.exit(0)


print('======================================================================')
print('======================================================================')

"""
  3.)
Создать текстовый файл (не программно), построчно записать фамилии сотрудников 
и величину их окладов. Определить, кто из сотрудников имеет оклад менее 
20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины 
дохода сотрудников.
"""

spisok=[]
summm=0.


try: 
    with open('VEDOMOST.txt', "r") as f_to_read:
        content = f_to_read.readlines()
        for i, line in  enumerate( content ):
            line = line.replace('\n','')
            line = line.split()
            spisok.append(line)
            summm = summm+float(line[1])
            if float(line[1])<20000: 
                spisok.append(line)
                print(line[0])
    av_s=summm/len(content)
    print(f' Mean incom is {av_s:.2f}')
except:
    print('IO Error')
    sys.exit(0)

print('======================================================================')
print('======================================================================')


"""
  4.)
Создать (не программно) текстовый файл со следующим содержимым: 
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно 
данные. При этом английские числительные должны заменяться на русские. Новый 
блок строк должен записываться в новый текстовый файл.
"""

slovar ={ "One" : "Один",
         "Two"  : "Два",
         "Three": "Три",
         "Four" : "Четыре"
         }


try:
    f_to_read = open('NUMBERS.txt', 'r')
    f_to_write = open('NUMera.txt', 'w')
    
    read_content = f_to_read.readlines()
    for line in read_content:
        line = line.split()
        line[0]=slovar[line[0]]
        print(line)
        line.append('\n')
        f_to_write.writelines(line)
    f_to_read.close()
    f_to_write.close()
except:
    print('IO Error')
    sys.exit(0)


print('======================================================================')
print('======================================================================')

"""
  5.)
Создать (программно) текстовый файл, записать в него программно набор чисел, 
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и 
выводить ее на экран.
"""

import random 

try:
    f_to_write = open('NUMS.txt', 'w')
    
    summm=0
    for i in range(30):
        a= random.randint(1, 100)
        f_to_write.write(str(a)+' ')
        summm = summm+a
        
    f_to_write.close()
    print(f'Summa: {summm}')
except:
    print('IO Error')
    sys.exit(0)



print('======================================================================')
print('======================================================================')


"""
  6.)
Необходимо создать (не программно) текстовый файл, где каждая строка описывает 
учебный предмет и наличие лекционных, практических и лабораторных занятий по 
этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно 
были все типы занятий. Сформировать словарь, содержащий название предмета и общее 
количество занятий по нему. Вывести словарь на экран.
"""

d_line ={}

try:
    f_to_read = open('SUBG.txt', 'r')
    read_content = f_to_read.readlines()
    f_to_read.close()
except:
    print('IO Error')
    sys.exit(0)
    
    
for i in range(2, len(read_content)):
    line = read_content[i].split()
    d_line[line[0]] = float(line[1])+float(line[2])+float(line[3])
    print(line)
print('----------------------------------------------------------------------')    
for k,j in d_line.items():
    
    print(f'{k:>15} {j:>15}')    
        


print('======================================================================')
print('======================================================================')



"""
  7.)
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая 
строка должна содержать данные о фирме: название, форма собственности, выручка, 
издержки. 
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также 
среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
 а также словарь со средней прибылью. Если фирма получила убытки, также добавить
 ее в словарь (со значением убытков). 
Пример списка: [{‘firm_1’: 5000, ‘firm_2’: 3000, ‘firm_3’: 1000}, {‘average_profit’: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Подсказка: использовать менеджер контекста.
"""

import json



margin_line ={}
try:    
    with open('FIRMS_STAT.txt', 'r') as f_to_read: 
        read_content = f_to_read.readlines()
        read_content = read_content[2:]
        for i in range(len(read_content)):
            line = read_content[i].split()
            print(line)
            margin_line[line[0]] = float(line[2])-float(line[3])
        print('----------------------------------------------------------------------')    
        print(margin_line)
except:
    print('IO Error')
    sys.exit(0)

print('----------------------------------------------------------------------')    

mean_margin=0.
loss =0
for i,k in margin_line.items():
    
    if k > 0: 
        mean_margin = mean_margin + k
    else:
        loss=loss+1
 
mean_margin = mean_margin/(len(margin_line)-loss)    
    
LIST = [margin_line, {'average_profit': mean_margin}]    

print(LIST)

try:    
    with open('FIRMS_STAT_more.json', 'w') as f_to_write:     
        json.dump(LIST, f_to_write)
except:
    print('IO Error')
    sys.exit(0)
        
    

print('======================================================================')
print('======================================================================')









