'''
# Homework 27.12.21
# Task 1 - Word extractor
word = tuple([input('Enter a word or text: ')])
finder = input('Search word: ')

res = word[0].find(finder)
res2 = word[0].find(finder[-1])

word_result = word[0]

print(f"Result: {word_result[res:res2 + 1]}")

# Task 2 - Tuple methods
tup = (1,2,3)

print(tup.count(2))
print(sum(tup))

# Task 3 - Short word extractor

arr = ["I'm sorry", "Dog", "That's it"]
res_arr = []
loc = ''
for elem in arr:
    for letter in elem:
        if letter == ' ' and loc.count("'") != 0:
            res_arr.append(loc)
            break
        loc += letter
        
    loc = ''
print(res_arr)

# Task 4 - Even letter (Viber)
word = input('Enter a word: ')
res = ''

for letter in range(len(word)):
    if letter % 2 == 1:
        res += word[letter]

print(res)

'''
# Classwork 27.12.21

def hello(name):
    return 'Hello! ' + name

result = hello('Andrii')
print(result)

my_name = 'Oleg'
hello(my_name)

def add(number, number2):
    

hello(input('Enter a name: '))
