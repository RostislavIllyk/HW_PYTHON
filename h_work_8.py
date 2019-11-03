# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 13:45:21 2019

@author: Rb
"""

"""

1.)

Реализовать класс «Дата», функция-конструктор которого должна принимать дату в 
виде строки формата «день-месяц-год». В рамках класса реализовать два метода. 
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и 
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, 
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). 
Проверить работу полученной структуры на реальных данных.

"""



class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt



class Date(object):
    
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year
        
    @classmethod
    def from_string(cls, date_as_string):
        is_date = cls.is_date_valid(date_as_string)
        try:
            if is_date == False:
                raise OwnError("Wrong date!")
        except OwnError as err:
            print(err)
            return
        
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


date2 = Date.from_string('11-10-2012')        

try:        
    print(date2.day, date2.month, date2.year)        
except:
    print('OOps. Something wrong')


print('======================================================================')
print()
print()


"""

2.)

Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем 
нуля в качестве делителя программа должна корректно обработать эту ситуацию и 
не завершиться с ошибкой.

"""

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_data = input("Введите положительное число: ")
inp_data2 = input("Введите не ноль : ")

try:
    inp_data = int(inp_data)
    inp_data2 = int(inp_data2)
    
    if inp_data2 == 0:
        raise OwnError("Вы ввели ноль!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {inp_data/inp_data2}")
    

print('======================================================================')
print()
print()

    
    
"""

3.)

Создайте собственный класс-исключение, который должен проверять содержимое списка 
на отсутствие элементов типа строка и булево. Проверить работу исключения на 
реальном примере. Необходимо запрашивать у пользователя данные и заполнять список. 
Класс-исключение должен контролировать типы данных элементов списка.

"""
    
class MyOwnError(Exception):
    def __init__(self, txt):
        self.txt = txt





lines=[
      [111, 444, .668, 4, 3],
      [111, 444, 'rrrr', True, 'hhh'],
      [0.667, 7, 77, False, 23.66],
      [111, 444, 'rrrr',555, 0, -45],
      [111, 444, 'rrrr', True, 'hhh']
      ]

new_lines=[]
for k in lines:
    mark=0
    for m in k:
#        print (type(m))
        try:
            if type(m) == bool or type(m) == str:
                raise MyOwnError('Wrong')
        except MyOwnError as err:
            print (err)
            mark=1
            break
    
    if mark ==0 : new_lines.append(k)    
    
print(new_lines)
        

print('======================================================================')
print()
print()

"""

4,5,6.)

Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
А также класс «Оргтехника», который будет базовым для классов-наследников. Эти 
классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе 
определить параметры, общие для приведенных типов. В классах-наследниках реализовать 
параметры, уникальные для каждого типа оргтехники. 

"""


from abc import ABC, abstractmethod



class Store(ABC):
    
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def StoreReceive(self):
        pass
    @abstractmethod
    def StoreRelease(self):
        pass



class StoreScanPrintCopy(Store):
    
    store_number=0
    list_of_Scan =[]
    list_of_Print=[]
    list_of_Copy =[]
    
    
    def __init__(self):
        self.srore_id = StoreScanPrintCopy.store_number
        StoreScanPrintCopy.store_number = StoreScanPrintCopy.store_number + 1
        self.list_of_Scan =[]
        self.list_of_Print=[]
        self.list_of_Copy =[]
        pass
        
    
    def StoreReceive(self, sabject):
        if type(sabject) is Scaner:
            StoreScanPrintCopy.list_of_Scan.append(sabject)
            self.list_of_Scan.append(sabject)    
            return
        if type(sabject) is Printer:
            StoreScanPrintCopy.list_of_Print.append(sabject)
            self.list_of_Print.append(sabject)
            return
        if type(sabject) is Xerox:
            StoreScanPrintCopy.list_of_Copy.append(sabject)
            self.list_of_Copy.append(sabject)
            return
        else: 
            print('This is store for scan print or copy machine ONLY.')
        


        
    def StoreRelease(self, sabject):
        if type(sabject) is Scaner:
            StoreScanPrintCopy.list_of_Scan.remove(sabject)
            self.list_of_Scan.remove(sabject)       
            del sabject
            return
        
        if type(sabject) is Printer:
            StoreScanPrintCopy.list_of_Print.remove(sabject)
            self.list_of_Print.remove(sabject)
            del sabject
            return
        
        if type(sabject) is Xerox:
            StoreScanPrintCopy.list_of_Copy.remove(sabject)
            self.list_of_Copy.remove(sabject)
            del sabject
            return

    def Get_party(self, list_of_items):
            set_of_items={Printer, Scaner, Xerox}
            for i in list_of_items:
                if type(i) not in set_of_items:
                    print('Wrong party...')
                    return
            for i in list_of_items:
                StoreScanPrintCopy.StoreReceive(self, i)


    def Sent_party(self, list_of_items, devision='main_shop'):
        list_of_shop=[]
        for i in list_of_items:
            list_of_shop.append(i)
            StoreScanPrintCopy.StoreRelease(self, i)
        return devision, list_of_shop


    def WhatDoWeHave(self):
        list_of_store=[]
        for i in self.list_of_Print:
            print('we do have printer named: ', i.name)
            list_of_store.append(i)
        for i in self.list_of_Scan:
            print('we do have scaner  named: ', i.name)
            list_of_store.append(i)
        for i in self.list_of_Copy:
            print('we do have xerox   named: ', i.name)
            list_of_store.append(i)
        return list_of_store




class ItemsOnStore(ABC):
    
    @abstractmethod
    def __init__(self, name):
        self.name = name
        pass
    
    @abstractmethod
    def Item_to_do(self):
        pass
    @abstractmethod
    def Item_about(self):
        print('This item has name: ', self.name)
        pass


    
class Printer(ItemsOnStore):

    def __init__(self, name):
        super().__init__(name)
        
    def Item_to_do(self):
        print('This item is printer. It is printing...')

    def Item_about(self):
        super().Item_about()


class Scaner(ItemsOnStore):

    def __init__(self, name):
        super().__init__(name)

    def Item_to_do(self):
        print('This item is scaner. It is scaning...')        

    def Item_about(self):
        super().Item_about()


class Xerox(ItemsOnStore):

    def __init__(self, name):
        super().__init__(name)

    def Item_to_do(self):
        print('This item is xerox. It is make copy...')

    def Item_about(self):
        super().Item_about()













pr = Printer('printer')
sc = Scaner('scaner')
xe = Xerox('xerox')
print('----------------------------------------------------------------------')
pr.Item_to_do()
pr.Item_about()
print('----------------------------------------------------------------------')
sc.Item_to_do()
sc.Item_about()
print('----------------------------------------------------------------------')
xe.Item_to_do()
xe.Item_about()
print('----------------------------------------------------------------------')

store_near =StoreScanPrintCopy()

print(' Store global ',StoreScanPrintCopy.list_of_Print)
print(' Store near ',store_near.list_of_Print)

print(' Store global ',StoreScanPrintCopy.list_of_Scan)
print(' Store near ',store_near.list_of_Scan)

print(' Store global ',StoreScanPrintCopy.list_of_Copy)
print(' Store near ',store_near.list_of_Copy)

print('======================================================================')
print()


store_near.StoreReceive(pr)
store_near.StoreReceive(sc)
store_near.StoreReceive(xe)
store_near.StoreReceive('test')

print(' Store global ',StoreScanPrintCopy.list_of_Print)
print(' Store near ',store_near.list_of_Print)

print(' Store global ',StoreScanPrintCopy.list_of_Print)
print(' Store near ',store_near.list_of_Scan)

print(' Store global ',StoreScanPrintCopy.list_of_Print)
print(' Store near ',store_near.list_of_Copy)
print('======================================================================')
print()



pr0 = Printer('printer0')
sc0 = Scaner('scaner0')
xe0 = Xerox('xerox0')
pr1 = Printer('printer01')

sabj_to_store = [pr0, sc0, xe0, pr1]


store_near.Get_party(sabj_to_store)
WhatDoWeHaveonstore = store_near.WhatDoWeHave()
print('WhatDoWeHaveonstore: ',len(WhatDoWeHaveonstore))
print('======================================================================')
print()

print(' Store global ',StoreScanPrintCopy.list_of_Print)
print(' Store near ',store_near.list_of_Print)

print(' Store global ',StoreScanPrintCopy.list_of_Scan)
print(' Store near ',store_near.list_of_Scan)

print(' Store global ',StoreScanPrintCopy.list_of_Copy)
print(' Store near ',store_near.list_of_Copy)
print('======================================================================')
print()


store_near.StoreRelease(pr)
store_near.StoreRelease(sc)
store_near.StoreRelease(xe)



print(' Store global ',StoreScanPrintCopy.list_of_Print)
print(' Store near ',store_near.list_of_Print)

print(' Store global ',StoreScanPrintCopy.list_of_Scan)
print(' Store near ',store_near.list_of_Scan)

print(' Store global ',StoreScanPrintCopy.list_of_Copy)
print(' Store near ',store_near.list_of_Copy)
print('======================================================================')
print()




shop, pallet=store_near.Sent_party(sabj_to_store)



print(' Store global ',StoreScanPrintCopy.list_of_Print)
print(' Store near ',store_near.list_of_Print)

print(' Store global ',StoreScanPrintCopy.list_of_Scan)
print(' Store near ',store_near.list_of_Scan)

print(' Store global ',StoreScanPrintCopy.list_of_Copy)
print(' Store near ',store_near.list_of_Copy)
print('======================================================================')
print()


print(shop, pallet)

print('======================================================================')
print('======================================================================')
print()
print()
print()




"""

7.)

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное 
число», реализуйте перегрузку методов сложения и умножения комплексных чисел. 
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив 
сложение и умножение созданных экземпляров. Проверьте корректность полученного 
результата.

"""





class My_c_num():
    
    def __init__(self, r, m):
        self.r = r
        self.m = m



    def __add__(self, other):
        
        r = self.r+other.r
        m = self.m+other.m
            
        return My_c_num(r,m)



    def __mul__(self, other):
        r = self.r*other.r - self.m*other.m
        m = self.m*other.r + self.r*other.m
        
                    
        return My_c_num(r,m)


    def __str__(self):
        line='real part '+str(self.r)+' unreal part '+str(self.m)
        return f'{line}'

x = 5
y = 3

a = complex(x,y); 

am=My_c_num(x,y)


x = -15
y = 30
b = complex(x,y); 
bm=My_c_num(x,y)



print(a,b,a+b,a*b)
print(am, bm, am+bm, am*bm)

print('======================================================================')
print('======================================================================')
print()






        

