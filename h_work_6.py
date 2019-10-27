# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 13:45:21 2019

@author: Rb
"""

"""

1.)

Создать класс TrafficLight (светофор) и определить у него один атрибут color 
(цвет) и метод running (запуск). Атрибут реализовать как приватный. В рамках 
метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Время перехода между режимами должно составлять 7 и 2 секунды. Проверить 
работу примера, создав экземпляр и вызвав описанный метод.

"""


import time
from itertools import cycle

class TraffivLight():
    def __init__(self):
        self.__colors = ['red', 'yellow', 'green']
        self.pool = cycle(self.__colors)
        
    def running(self):
        self.__color = next(self.pool)
        print(self.__color)

a=TraffivLight()
time_delays = [7, 2, 3]
pool2 = cycle(time_delays)

for i in range(12):
    a.running()
    time.sleep(next(pool2))
print()
print()
print('======================================================================')
print()







"""

2.)

Реализовать класс Road (дорога), в котором определить атрибуты: length (длина),
 width (ширина). Значения данных атрибутов должны передаваться при создании 
 экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета массы
 асфальта, необходимого для покрытия всего дорожного полотна. Использовать 
 формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги 
 асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т

"""

global dense

dense=25
class Road():

    def __init__(self, length, wides):
        self._length = length
        self._wides  = wides
        self._h  = 5

    def mass(self):
        mass = self._length*self._wides*dense*self._h
        return mass
        
road_1 = Road(100,10)
print(f'Total mass: {road_1.mass()}')
print()
print()
print('======================================================================')
print()







"""

3.)

Реализовать базовый класс Worker (работник), в котором определить атрибуты: 
name, surname, position (должность), income (доход). Последний атрибут
должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад 
и премия, например, {"profit": profit, "bonus": bonus}. Создать класс 
Position (должность) на базе класса Worker. В классе Position реализовать 
методы получения полного имени сотрудника (get_full_name) и дохода с учетом 
премии (get_full_profit). Проверить работу примера на реальных данных (создать 
экземпляры класса Position, передать данные, проверить значения атрибутов, 
вызвать методы экземпляров).

"""


class Worker():

    def __init__(self, name, surname, posision, profit, bonus):
        self.name     = name
        self.surname  = surname
        self.posision = posision
        self.income   = {'profit': profit, 'bonus': bonus}





class Possision(Worker):

    def get_full_profit(self):
        return self.income['profit']+self.income['bonus']

    def get_full_name(self):
        return self.name+' '+self.surname



name, surname, posision, profit, bonus = 'Petr','Petrov','Driver',1000,100

W1 = Worker( name, surname, posision, profit, bonus)
print(W1.income, W1.name, W1.surname, W1.posision)
print()
name, surname, posision, profit, bonus = 'Ivan','Pavlov','Plumber',3000,300

P1 = Possision( name, surname, posision, profit, bonus)
print(P1.get_full_name(), P1.get_full_profit())
print(P1.income, P1.name, P1.surname, P1.posision)
print()
print()
print('======================================================================')
print()








"""

4.)

Опишите несколько классов: TownCar, SportCar, WorkCar, PoliceCar. У каждого 
класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
 А также несколько методов: go, stop, turn(direction), которые должны сообщать, 
 что машина поехала, остановилась, повернула (куда).

"""



import random 

class Car():
    
    
    list_of_cars_name=[]
    list_of_cars_obj=[]
    
    
    
    
    def __init__(self,name = 'Car', color = 'Blue', police = False, speed=0):
        
        self.name   = name+'_'+str(len(Car.list_of_cars_name))
        self.color  = color
        self.speed  = speed
        self.is_police = police
        self.list_add()
        
    def list_add(self):    
        Car.list_of_cars_name.append(self.name)
        Car.list_of_cars_obj.append(self)
    
    
    def go(self):
        print('Car named', self.name, 'start to go.')
    
    def stop(self):
        print('Car named', self.name, 'stop.')
    
    def turn_left(self):
        print('Car named', self.name, 'turn left.')
        
    def turn_right(self):
        print('Car named', self.name, 'turn right.')       
    
    def move_ahead(self):
        print('Car named', self.name, 'move ahead.')              
 
    
    
    
    
    
class TownCar(Car):
    def __init__(self, color = 'Blue'):
        super().__init__(name = 'TownCar', color = 'Blue', police = False, speed=10)
        self.color = color
        
class SportCar(Car):
    def __init__(self, color = 'Blue'):
        super().__init__(name = 'SportCar', color = 'Blue', police = False, speed=100)
        self.color = color
    
class WorkerCar(Car):
    def __init__(self,  color = 'Blue'):
        super().__init__(name = 'WorkerCar', color = 'Blue', police = False, speed=3)
        self.color = color
    
class PoliceCar(Car):
    def __init__(self):
        super().__init__(name = 'PoliceCar', color = 'Blue', police = True, speed=70)
    
    
    
    
    
a=Car()
b=SportCar(color = 'Red')
c=PoliceCar()
d=TownCar()
e=WorkerCar(color = 'Brown')


#haos=[a,b,c,d,e]
print('On the roads: ', Car.list_of_cars_name)    

print()
for i in range(30):
    numer= random.randint(0, len(Car.list_of_cars_obj)-1)   
    car_choice=Car.list_of_cars_obj[numer]
    n_comand = random.randint(0,4)
    
    if n_comand == 0:
        car_choice.go()
    if n_comand == 1:
        car_choice.stop()
    if n_comand == 2:
        car_choice.turn_left()
    if n_comand == 3:
        car_choice.turn_right()
    if n_comand == 4:
        car_choice.move_ahead()

print()
print()
#print(Car.list_of_cars_obj)
print('======================================================================')
print()






"""

5.)

Реализовать класс Stationery (канцелярская принадлежность). Определить в нем 
атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение 
“Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш)
, Handle (маркер). В каждом из классов реализовать переопределение метода draw.
 Для каждого из классов методы должен выводить уникальное сообщение. Создать 
 экземпляры классов и проверить, что выведет описанный метод для каждого 
 экземпляра.

"""




class Stationery():
    def __init__(self):
        self.title = ' чем то'
        
    def draw(self):
        print('Запуск отрисовки', self.title)


class Pen(Stationery):
    title = 'РУЧКОЙ'
    def draw(self):
        print('Запуск отрисовки ', Pen.title)

class Pencil(Stationery):
    title = 'КАРАНДАШОМ'
        
    def draw(self):
        print('Запуск отрисовки ', Pencil.title)

class Handel(Stationery):
    title = 'МАРКЕРОМ'
        
    def draw(self):
        print('Запуск отрисовки ', Handel.title)


a=Stationery()
b=Pen()
c=Pencil()
d=Handel()

a.draw()
b.draw()
c.draw()
d.draw()

print()
print()
print('======================================================================')
print()











