
#1

numbers = []
while True:
    user_input = input("enter the number:")
    if user_input in numbers:
        print(f" duplicate number found i.e {user_input}")
        break
    numbers.append(user_input)
    print(user_input)
    
# numbers = []
# user_input = input("enter the number:")
# while user_input not in numbers:
#     user_input = input("enter the number:")
#     numbers.append(user_input)
#     print(f" duplicate number found i.e {user_input}")
#     break

 #2   

n = int(input("Enter a positive integer: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial:", fact)


#3

n = int(input("Enter a number: "))
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print("Sum:", total)

#4

numbers = [10, 5, 10, 8, 10, 3, 7]
target = 10
count = 0
i = 0
while i < len(numbers):
    if numbers[i] == target:
        count += 1
    i += 1
print(target, "appears", count, "times")

#5

sentence = input("Enter a sentence: ")
vowels = "aeiou"
v = 0
c = 0
i = 0
while i < len(sentence):
    ch = sentence[i].lower()
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1
    i += 1
print("Vowels:", v)
print("Consonants:", c)

#6
n = int(input("Enter an integer: "))
n = abs(n)
count = 0
if n == 0:
    count = 1
while n > 0:
    n //= 10
    count += 1
print("Number of digits:", count)

#7

n = int(input("Enter a positive integer: "))
seq = [n]
while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
    seq.append(n)
print(", ".join(str(x) for x in seq))

#8

c = ord('A')
while c <= ord('Z'):
    print(chr(c), end=' ')
    c += 1
print()

#9
start = int(input("Start: "))
end = int(input("End: "))
i = start
while i <= end:
    print(i, end=' ')
    i += 1
print()

#10
n = 49
while n >= 1:
    print(n, end=' ')
    n -= 2
print()

#11
n = 7
while n <= 100:
    print(n, end=' ')
    n += 7
print()

#12
total = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
print("Total:", total)

#!3

age = int(input("Enter your age: "))
while age < 0 or age > 120:
    print("invalid age")
    age = int(input("Enter your age: "))
print("Valid age:", age)

#14
total = 0
count = 0
score = int(input("Enter score (-1 to finish): "))
while score != -1:
    total += score
    count += 1
    score = int(input("Enter score (-1 to finish): "))

if count > 0:
    print("Average:", total / count)
else:
    print("No scores entered")

#15

password = "secret123"
attempts = 0
granted = False
while attempts < 3:
    entry = input("Enter password: ")
    if entry == password:
        print("access granted")
        granted = True
        break
    attempts += 1

if not granted:
    print("access denied")

#16

n = int(input("Enter an integer: "))
reversed_num = 0
while n > 0:
    digit = n % 10
    reversed_num = reversed_num * 10 + digit
    n //= 10
print(reversed_num)


#17

n = int(input("How many terms? "))
a, b = 0, 1
count = 0
while count < n:
    print(a, end=' ')
    a, b = b, a + b
    count += 1
print()



#18
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ""
i = 0
while i < len(s):
    if s[i] not in vowels:
        result += s[i]
    i += 1
print(result)

#19

s = input("Enter a string: ")
count = 0
i = 0
while i < len(s) - 1:
    if s[i:i+2] == "hi":
        count += 1
    i += 1
print('"hi" appears', count, 'times')



#20
numbers = [12, 25, 7, 30, 18, 40, 55, 9]
i = 0
while i < len(numbers):
    if numbers[i] % 5 == 0:
        print(numbers[i], end=' ')
    i += 1
print()


#21

s = input("Enter a string: ")
result = ""
i = 0
while i < len(s):
    ch = s[i]
    if ch.islower():
        result += ch.upper()
    elif ch.isupper():
        result += ch.lower()
    else:
        result += ch
    i += 1
print(result)

#22

i = 1
while i <= 2:
    j = 1
    while j <= 2:
        print(f'({i},{j})', end=' ')
        j += 1
    i += 1

#23


i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print('*', end='')
        j += 1
    i += 1
print()

#24

found = False
x = 1
while not found:
    if x * x > 20:
        found = True
    else:
        x += 1
print(x)


#25
total = 0
user_input = 0
while user_input != -1:
    total += user_input
    user_input = int(input('enter: '))
print(total)

#26

x = 10
while x < 5:
    x += 1
    print('loop')
print(x)

#27
x = 3
while x:
    print(x, end=' ')
    x -= 1


#28

a, b = 0, 1
while a < 10:
    print(a, end=' ')
    a, b = b, a + b

#29

def count_case(s):
    upper = 0
    lower = 0
    i = 0
    while i < len(s):
        if s[i].isupper():
            upper += 1
        elif s[i].islower():
            lower += 1
        i += 1
    print("No. of upper case characters :", upper)
    print("No. of lower case characters :", lower)

count_case('The quick Brow Fox')



#30
while True:
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Multiply two numbers")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "4":
        print("Goodbye")
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", a + b)
    elif choice == "2":
        print("Result:", a - b)
    elif choice == "3":
        print("Result:", a * b)
    else:
        print("Invalid choice, try again")



#31
pos = 0
neg = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    if num > 0:
        pos += 1
    else:
        neg += 1
print("Positive:", pos)
print("Negative:", neg)



#32
start = int(input("Start: "))
end = int(input("End: "))

num = start if start >= 2 else 2
while num <= end:
    is_prime = True
    d = 2
    while d * d <= num:
        if num % d == 0:
            is_prime = False
            break
        d += 1
    if is_prime:
        print(num, end=' ')
    num += 1
print()



#33
numbers = [12, 40, 21, 31, 10, 7, 5]
i = 0
while i < len(numbers):
    if numbers[i] < 20:
        print(numbers[i], end=' ')
    i += 1
print()



#34
numbers = [45, 60, 12, 75, 30, 55, 8, 90]
i = 0
while i < len(numbers):
    if numbers[i] > 50:
        numbers[i] = 0
    i += 1
print(numbers)



#35
numbers = [15, 25, 30, 45, 60, 12, 90, 7]
count = 0
i = 0
while i < len(numbers):
    if numbers[i] % 15 == 0:
        count += 1
    i += 1
print("Count:", count)


#36

numbers = [10, 15, 25, 30, 45]
i = 0
ascending = True
while i < len(numbers) - 1:
    if numbers[i] > numbers[i + 1]:
        ascending = False
        break
    i += 1
print("sorted" if ascending else "not sorted")


#37
c = ord('a')
while c <= ord('z'):
    print(chr(c), end=' ')
    c += 1
print()



#38
pages = [45, 30, 50, 40]
i = 0
while i < len(pages):
    print(f"Chapter {i + 1} has {pages[i]} pages")
    i += 1


#39

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = []
i = 0
while i < len(list1):
    if list1[i] in list2:
        common.append(list1[i])
    i += 1
print(common)


#40
tables = [2, 4, 6, 7, 8]
t = 0
while t < len(tables):
    num = tables[t]
    print(f"\nMultiplication table of {num}:")
    i = 1
    while i <= 10:
        print(f"{num} x {i} = {num * i}")
        i += 1
    t += 1



#41
numbers = [10, 15, 25, 30, 45, 15]
has_dup = False
i = 0
while i < len(numbers):
    j = i + 1
    while j < len(numbers):
        if numbers[i] == numbers[j]:
            has_dup = True
            break
        j += 1
    if has_dup:
        break
    i += 1
print("has Duplicates" if has_dup else "no duplicates")
