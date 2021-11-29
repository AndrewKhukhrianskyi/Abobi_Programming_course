"""
# Task 1 - Triangles

perimeter = 0

count_triangle = int(input('Введи кол-во треугольников: '))

for triangle in range(count_triangle):
    side_1 = int(input('Сторона 1: '))
    side_2 = int(input('Сторона 2: '))
    side_3 = int(input('Сторона 3: '))
    perimeter += side_1 + side_2 + side_3

print(f"Периметр всех треугольников: {perimeter}")

# Task 2 - Students
students = int(input('Введите кол-во студентов: '))
marks = 0

for mark in range(students):
    marks += int(input("Оценка студента: "))

print(f"Средняя оценка: {round(marks / students, 2)}")

# Task 3 - Films
from random import randint

film = ''
stop = '1'
while 1:
    if film == stop:
        break
    
    else:
        film = input('Введи название фильма: ')
       print(film + '|' + str(randint(1,10)))

# Task 4 - Flash

file = 0
f1 = 256
f2 = 512
f3 = 1024
f4 = 2097152 # 2 TB

while f4 > 50:
    file += 1
    f4 -= 50

print('2TB' + '|' + str(file))


#...
    
# Неизменяемый ТД (Статический)
string = 'Dog'
print(string)
print(string.replace('g', 'ctor'))
print(string)

# Списки
arr1 = [1,2,3,4]
arr2 = [1.5, 2.5, 3.5]
arr3 = ['Hi', 'Saw']
arr4 = [True, False]
arr5 = [1, 1.5, True, 'STRING', 2]

print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5)

from random import randint
arr = []
for elem in range(randint(3,10)):
    arr.append(randint(1,5))
    
arr.sort()
print(arr)
for number in arr:
    if number == 1:
        arr.append('Я нашел единицу')
        
arr.pop(1)
print(arr)

"""

# HW - Even numbers

arr = []

for elem in range(1,10,2):
    arr.append(elem)


print(arr)
