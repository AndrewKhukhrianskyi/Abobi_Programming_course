'''
Classwork
dictionary = {'name': 'Oleg', 'surename': 'Ivanov', 'id': 1}
#print(dictionary.keys())
#print(dictionary.values())

dictionary_new = dict.fromkeys(['name', 'surename', 'age'], None)

dictionary_new['name'] = input('Name: ')
dictionary_new['surename'] = input('Surename: ')
dictionary_new['age'] = input('Age: ')

print(dictionary_new)

# Homework 13.12.2021
# 1000 => 1,0,0,0
# Task 1 - Lucky tickets
ticket = [1,2,4,3,3,1]

if sum(ticket[0:3]) == sum(ticket[3:6]):
    print(True)

else:
    print(False)

# Subtask - Odd & Even

odds = 0
evens = 0

for num in ticket:
    if num % 2 == 0:
        odds += num
    else:
        evens += num


if odds == evens:
    print(True)

else:
    print(False)

# Task 2 - Ones extracting

arr = [[1,2,4,8,1], [2,3,4,1,1,5,6,1]]
ones = []
for subarr in arr:
    for elem in subarr:
        if elem == 1:
            ones.append(elem)

print(ones)
print(sum(ones))

# Task 3 - Filters
arr = [1,2,3,4,4,5,6,6,6,7]
unique = []

for elem in arr:
    if elem in unique:
        continue
    else:
        unique.append(elem)

print(unique)


# Subtask - set

new_unique = list(set(arr))
print(new_unique)

'''

# True - Овца есть в загоне
# False - Овцы нет в загоне

from random import randint

sheeps = []

for sheep in range(randint(2,20)):
    sheeps.append(bool(randint(0,1)))

print(sheeps)
print(sheeps.count(True))
