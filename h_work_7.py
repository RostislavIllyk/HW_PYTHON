# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 13:45:21 2019

@author: Rb
"""

"""

1.)

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса 
(метод __init__()), который должен принимать данные (список списков) для 
формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных
 в виде прямоугольной схемы.

"""



import random
import numpy as np

def random_input_matrix(rank):
    M_structura=[]
    for i in range(rank[0]):
        line=[0]*rank[1]
        for j in range(rank[1]):
            line[j] = random.randint(0, 100)
        M_structura.append(line)
        
    return My_matrix(M_structura)


class My_matrix():
    
    def __init__(self, M):
        self.matrix = M
        self.r0 = len(M)
        self.r1 = len(M[0])



    def __add__(self, other):
        
        answer =[]
        
        if (len(other.matrix) != len(self.matrix)) or (len(other.matrix[0]) != len(self.matrix[0])):
            print('matrix has wrong rank')
            return('rank error')
            
        for i in range(self.r0):
            line = [0]*self.r1
            for j in range(self.r1):
                line[j] = self.matrix[i][j]+other.matrix[i][j]
            answer.append(line)   
        return My_matrix(answer)





    def __mul__(self, other):
        
        if (len(other.matrix) != len(self.matrix[0])):
            print('matrix has wrong rank')
            return('rank error')
        
        
        
        answer = np.zeros([len(self.matrix), len(other.matrix[0])])
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[0])):
                for k in range(len(self.matrix[0])):
                    
                    answer[i][j]=answer[i][j]+self.matrix[i][k]*other.matrix[k][j]
                    
#        a=np.array(self.matrix)        
#        b=np.array(other.matrix)     
#        c=np.dot(a,b)   
#        print(c)
                    
        return My_matrix(answer)


    def __str__(self):
        line=''
        for i in range(self.r0):
                line=line+(str(self.matrix[i])+'\n')
        return f'{line}'







rank = [3, 5]                
a= random_input_matrix(rank)                               
print(a)
print('---------------------------------------------------------------------')     

rank = [3, 5]                
b= random_input_matrix(rank)                               
print(b)
print('---------------------------------------------------------------------')                

rank = [5, 9]                
c= random_input_matrix(rank)                               
print(c)
print('---------------------------------------------------------------------')                
print('---------------------------------------------------------------------')     
          

result=(a+b)*c
print(result)
print('=====================================================================')                
print()


"""

2.)

Реализовать проект расчета суммарного расхода ткани на производство одежды. 
Основная сущность (класс) этого проекта — одежда, которая может иметь 
определенное название. К типам одежды в этом проекте относятся пальто и костюм. 
У этих типов одежды существуют параметры: размер (для пальто) и рост 
(для костюма). Это могут быть обычные числа: V и H, соответственно. 
Для определения расхода ткани по каждому типу одежды использовать формулы: для 
пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов 
на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на 
этом уроке знания: реализовать абстрактные классы для основных классов проекта, 
проверить на практике работу декоратора @property.

"""
       

from abc import ABC, abstractmethod

class Сlothes(ABC):
    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Сlothes):
    
    def __init__(self, v):
        self.v = v
        self.result=0
        
    @property
    def tissue_consumption(self):
        self.result = self.v/6.5 + 0.5
        return self.result

class Suit(Сlothes):
    
    def __init__(self, h):
        self.h=h       
        self.result=0
        
    @property
    def tissue_consumption(self):
        self.result = 2*self.h + 0.3
        return self.result


coat_1 = Coat(3)        
print(coat_1.tissue_consumption)        
suitt_1 = Suit(10)        
print(suitt_1.tissue_consumption)        
print(suitt_1.tissue_consumption+coat_1.tissue_consumption)        
        
print('=====================================================================')                
print()


"""

3.)

Реализовать программу работы с органическими клетками, состоящими из ячеек. 
Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, 
соответствующий количеству ячеек клетки (целое число). В классе должны быть 
реализованы методы перегрузки арифметических операторов: сложение (__add__()), 
вычитание (__sub__()) , умножение (__mul__()), деление (__truediv__()). Данные 
методы должны применяться только к клеткам и выполнять увеличение, уменьшение, 
умножение и обычное (не целочисленное) деление клеток, соответственно. В методе 
деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно 
равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если 
разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее 
сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется 
как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется 
как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса 
и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек 
между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, 
то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда 
метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда 
метод make_order() вернет строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.

"""

class Cell():
    
    def __init__(self, partition):
        self.partition = partition
        


    def __add__(self, other):
        result = self.partition+other.partition
        return Cell(result)

    def __sub__(self, other):
        result = self.partition
        if(self.partition-other.partition > 0):
            result = self.partition-other.partition
        else:
            print('error impossible to do it.')
        return Cell(result)

    def __mul__(self, other):
        result = self.partition*other.partition
        return Cell(result)

    def __truediv__(self, other):
        result = self.partition//other.partition
        return Cell(result)


    def make_order(self, c='None', number=3):
        if c == 'None':
            c=self
        i=c.partition//number
        j=c.partition%number
        line = '*'*number+'\n'
        line = line*i+'*'*j+'\n'        
        return f'{line}'



a=Cell(2)
b=Cell(7)
d=Cell(3)

result=a+b*d
print('result: ')

print(result.make_order(c=result, number=5))
print('a: ',result.make_order(c=a, number=5))
print('b: ')
print(result.make_order(c=b, number=5))
print('d: ',result.make_order(c=d, number=5))
print('result: ')
print(result.make_order( number=7))



