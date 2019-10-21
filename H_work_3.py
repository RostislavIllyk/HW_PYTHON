"""

1.)

Реализовать функцию, принимающую два числа (позиционные аргументы) и 
выполняющую их деление. Числа запрашивать у пользователя, предусмотреть 
обработку ситуации деления на ноль.

"""


def divide(a, b):
    
    c=0
    errorr=None
    
    try:
        a=float(a)
    except:
        errorr = 'numerator is not a number error.'
        return c, errorr
    
    try:
        b=float(b)
    except:
        errorr = 'denominator is not a number error.'
        return c, errorr
        
    try:
        c=a/b
    except:
        errorr = 'Divide by zero error.'
        return c, errorr
    return c, errorr

a=(input('numerator : '))
b=(input('denominator : '))
c, errorr=divide(a, b)

if errorr is None:
    print(f'{c:.2f}')
else:
    print(errorr)


print()
print('======================================================================')
print()

"""    

2.)    
    
Реализовать функцию, принимающую несколько параметров, описывающих данные 
пользователя: имя, фамилия, год рождения, город проживания, email, 
телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
    
"""    

name='Ivan'
soname='Petrov'
y_of_b = 1991
town = 'Moscow'
email = 'aaa@email.com'
tel = '985 777 77 77'



def text_in_line(name='Elvis', soname='Brown', y_of_b = 1951, \
                 town = 'London', email = 'bbb@gmail.com', \
                 tel = '833 83 23 34 55'):
    
    
    agr = str(name) + ' ' + str(soname)  + ' ' + str(y_of_b) + \
    ' года рождения проживает в ' + str(town) + ' телефон  ' + \
    str(tel) + ' emai ' + str(email)
    
    return agr



a = text_in_line(name=name, soname=soname, y_of_b = y_of_b, \
                 town = town, email = email, tel = tel)


print(a)

print()
print('======================================================================')
print()


"""    

3.)    

Реализовать функцию my_func(), которая принимает три позиционных аргумента, 
и возвращает сумму наибольших двух аргументов.
    
"""    


a1='a'
a2='b'
a3='n'

#a1=10
#a2=11
#a3=22

def func_m(a,b,c):
    y =[a,b,c]
    z = min(y)
    y.remove(z)
    return y[0]+y[1]
    
print(func_m(a1,a2,a3))    

print()
print('======================================================================')
print()

"""    

4.) 
    
Программа принимает действительное положительное число x и целое отрицательное 
число y. Необходимо выполнить возведение числа x в степень y. Задание
 необходимо реализовать в виде функции my_func(x, y). При решении задания 
 необходимо обойтись без встроенной функции возведения числа в степень.
    
"""    


def power_(a, b):
    
    c=0
    errorr=None
    
    try:
        a=float(a)
    except:
        errorr = 'number is not a number error.'
        return c, errorr
    
    if a <=0:
        errorr = 'numer must be >0 error.'
        return c, errorr
    
    
    
    
    try:
        b=float(b)
    except:
        errorr = 'number is not a number error.'
        return c, errorr
    
    if b>=0:
        errorr = 'numer must be <0 error.'
        return c, errorr
    if (int(b)-b)!=0:
        errorr = 'numer must be int error.'
        return c, errorr
    
    x=1
    for i in range(int(-b)):
        x=x*a
    c = 1/x

    return c, errorr

a=(input('real number must be > 0 : '))
b=(input('number must be int and < 0 : '))
c, errorr=power_(a, b)

if errorr is None:
    print(f'{c:.7f}')
else:
    print(errorr)

print(float(a)**(int(b)))


print()
print('======================================================================')
print()

"""    

5.) 
    
Программа запрашивает у пользователя строку чисел, разделенных пробелом. При 
нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод
 чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных 
 чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа 
 вводится специальный символ, выполнение программы завершается. Если специальный
 символ введен после нескольких чисел, то вначале нужно добавить сумму этих 
 чисел к полученной ранее сумме и после этого завершить программу.
 
"""    


def my_func(*args):
    result = sum(args)
    return result


itog=0.
while True:

    str_of_dig = input('введите строку чисел или "Z" для выхода:  ')
    if str_of_dig =='Z':
        break
    
    digits = str_of_dig.split(' ')
    d=[]
    for i in range(len(digits)):
        d.append(float(digits[i]))
        
    result=my_func(*d)
    print(result)
    itog = itog+result
    print('itog: ', itog)


print()
print('======================================================================')
print()



"""    

6.)    

Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
 возвращающую его же, но с прописной первой буквой. Например,
 print(int_func(‘text’)) -> Text. 
Продолжить работу над заданием. В программу должна попадать строка из слов, 
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
 Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной 
 буквы. Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(a):
    return a.capitalize()

line = input('введите строку :  ')
line_of_words = line.split(' ')
print()
result=''
for i in range (len(line_of_words)):
    result=result+int_func(line_of_words[i])+' '

print(result)
print()
print('======================================================================')
print()





















