'''
# Classwork 10.01.22
#var = int(input('Введи что-то: '))
#print('У вас получилось:', var + 2)
s = 'Word is a magic'
start = s.find('magic')  
end = s.find('c')
bug_name = 'иван'
print(bug_name.title())
print(bug_name.upper())
#print(bug_name.replace())
print(s[start:end+1])

counter = int(input('Counter: '))

while counter % 5 != 0:
    counter += 1
    print(counter)
'''

arr = [elem for elem in range(100000) if elem % 5 == 0]
print(arr)
