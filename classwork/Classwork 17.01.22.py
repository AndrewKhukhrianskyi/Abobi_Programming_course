"""
# Homework 17.01.22

# Task 1 - Figure type

print('Task 1 - Figure type')
while True:
    question = input('Do you want to continue? Y/N ')

    if question == 'Y':
        side = int(input('Enter a side: '))
        figure = int(input('Amount of sides: '))

        if figure == 3:
            print(f"Triangle and perimeter = {side * figure}")

        elif figure == 4:
            print(f"Square and perimeter = {side * figure}")

        elif figure >= 5:
            print(f"Polygon and perimeter = {side * figure}")

        else:
            print('Error. Incorrect value. Try again.')
    else:
        break

print('--------------')
# Task 2 - Cone area

print('Task 2 - Cone area')
cone_height = int(input('Enter a height: '))
radius = int(input('Enter a radius: '))

print(f"Cone area = 1/3 pi * R^2 * h => Cone area = {round((1/3) * 3.14 * radius ** 2 * cone_height, 2)}")

        
# Task 3 - Sewing
jacket = 15
pants = 10
length = 1000

print(f'Amount of jackets: {length // jacket}')
print(f'Amount pf pants: {length // pants}')

# Classwork 17.01.22
try:
    arr = [1,2,3]
    print(arr[6])
except IndexError:
    print('Ахтунг! Обращаешься к несуществующему элементу')
finally:
    print(arr[2])

try:
    num1 = int(input('Num 1: '))
    num2 = int(input('Num 2: '))
    oper = input('Operation: ')
    if oper == '+':
        print(num1 + num2)
    elif oper == '-':
        print(num1 - num2)
    elif oper == '*':
        print(num1 * num2)
    elif oper == '/':
        print(num1 / num2)
    else:
        print('Error. Incorrect operaion')
except ZeroDivisionError:
   print('Division by 0')
"""

gunners = {'Joey' : 'aye', 'Bill' : 'nei', 'Tom' : 'aye'}
yes = 0

for gunner in gunners:
    if gunners[gunner] == 'aye':
        yes += 1

if yes == len(gunners):
    print('Fire!')

elif yes < len(gunners):
    print('We died')
