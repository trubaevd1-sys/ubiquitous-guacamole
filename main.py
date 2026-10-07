# Рівень 1: розминка

# 1
a = 17
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)

# 2
print(a // b)
print(a % b)


# 3
print(2 ** 10)
print(10 ** 3)

# 4
price = 249.99
count = 3

print(price * count)

# 5
print(type(7 / 2))
print(type(7 // 2))
print(type(7.0 // 2))


# 6
name = "Python"

print(name * 3)

# 7
text = "Привіт, " + "світ!"

print(text)


# Рівень 2: практичні обчислення

# 8
students = 28
desks = 6

print(students // desks)
print(students % desks)

# 9
seconds = 3725

hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds_left = seconds % 60

print(hours)
print(minutes)
print(seconds_left)

# 10
minutes = 150

hours = minutes // 60
minutes_left = minutes % 60

print(hours)
print(minutes_left)

# 11
c = 36.6

f = c * 9 / 5 + 32

print(f)

# 12
a = 12.5
b = 8

area = a * b
perimeter = 2 * (a + b)

print(area)
print(perimeter)

# 13
r = 7
pi = 3.14159

area = pi * r ** 2
length = 2 * pi * r

print(area)
print(length)

# 14
price = 1200
discount = 15

discount_sum = price * discount / 100
final_price = price - discount_sum

print(discount_sum)
print(final_price)

# 15
salary = 25000
tax = 19.5

tax_sum = salary * tax / 100
money = salary - tax_sum

print(money)

# 16
speed = 90
time = 2.5

distance = speed * time

print(distance)

# 17
a = 10
b = 11
c = 8

average = (a + b + c) / 3

print(average)


# Рівень 3: цифри та числа

# 18
n = 7

print(n % 2)

# 19
n = 473

print(n % 10)

# 20
n = 473

hundreds = n // 100
tens = (n // 10) % 10
ones = n % 10

print(hundreds)
print(tens)
print(ones)

# 21
n = 859

hundreds = n // 100
tens = (n // 10) % 10
ones = n % 10

print(hundreds + tens + ones)

# 22
n = 123

hundreds = n // 100
tens = (n // 10) % 10
ones = n % 10

number = ones * 100 + tens * 10 + hundreds

print(number)

# 23
print(144 ** 0.5)

# 24
print(365 * 24 * 60 * 60)


# Рівень 4: типи даних і хитрощі

# 25
x = "5"
y = "3"

print(x + y)

x = int(x)
y = int(y)

print(x + y)


# 26
x = 9.99

print(int(x))


# 27
print(True + True + True)
print(True * 10)


# 28
a = 5
b = 10

a = a + b
b = a - b
a = a - b

print(a)
print(b)

# 29
deposit = 10000
rate = 0.12
years = 3

sum = deposit * (1 + rate) ** years

print(sum)

# 30
line = "-"
number = 20

print(line * number)
print("Результат: " + str(2 ** 20))