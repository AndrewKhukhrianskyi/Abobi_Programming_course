# Homework 07.02.22
# Task 1 - Length converter
def l_converter(cm):
    len_list = ['д', 'мл', 'ммл', 'мм']
    values = [2.54, 160934, 185200, 10]
    for elem in range(len(len_list)):
        print(f"Результат: {cm / values[elem], len_list[elem]}")

#l_converter(1500)
# Task 2 - Vowel Counter
# HW - Bug fix
def vowels_counter(sentence):
    vowel_dict = 'аоеияюэыеу'
    vowel_c_dict = {}
    value = 1
    sentence = sentence.lower()
    for elem in sentence:
        if elem in vowel_dict:
            if elem not in vowel_c_dict:
                vowel_c_dict[elem] = value
            else:
                vowel_c_dict[elem] = value + 1
                
    print(vowel_c_dict)

#vowels_counter('собакаааааа')

# Task 3 - Glass optimism
from random import randint
#glass_volume = int(input('Enter glass volume: '))

def glass_checker(ml, glass_volume):
    if ml > glass_volume // 2:
        print(True, ml)
    elif ml < glass_volume // 2:
        print(False, ml)
    else:
        print(None, ml)
        
#glass_checker(randint(10, glass_volume), glass_volume)
# Classwork 07.02.22
def func(*userdata):
    for elem in userdata:
        print(elem)
        
    print(type(userdata))
#func('Andy', 'Andersen', 25,
#     'Male', 'Married', 'user1@gmail.com')

#func('Mary', 'Poppins', 32,
#     'Female')
def func2(**userdata):
    print(userdata)

#func2(name = 'Andy', surename = 'Harris',
#     age = 25)
def func3(a,b):
    print(a + b)

#func3(2,3)
#func('a', 'b')
