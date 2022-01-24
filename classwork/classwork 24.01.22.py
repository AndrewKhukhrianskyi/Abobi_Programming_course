'''
# Homework 24.01.22
# Task 1 - NameError Exception

try:
    n1 = 2
    n2 = 3
    print(n3)

except NameError:
    print("Внимание - данной переменной не существует. Напишите ее ниже!")
    n3 = int(input('Введите число: '))
    print(n1 + n2 +n3)

# Task 2 - IndexError Exception

try:
    word = input('Введи слово: ')
    index = int(input('Индекс: '))
    print(word[index])

except IndexError:
    print(f"Ты обращаешься к несуществуюещму элементу\nДлина слова состоит из {len(word)} символов")

# Task 3 - Exception catcher        

try:
    do = ''
    while do != 'exit':
        do = input('Введите любое слово: ')
        num = int(input('Число: '))
        print(do + num)
except TypeError:
    print('Ты пытаешься сложить число и букву')
'''
# classwork 24.01.22

def say_hi():
    print('Hello!')

def say_hi_again():
    username = input('Enter name: ')
    hi_form = input('Hi form: ')
    return hi_form + ' ' + username

#result = say_hi_again()
#print(result)

#result = result.replace(' ', '____')
#print(result)

def perimeter(figure_side, amount):
    return figure_side * amount

def vowels_remover(word):
    voc = 'aouyie'
    for letter in word:
        if letter in voc:
            word = word.replace(letter, '')
    return word


