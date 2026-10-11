# Execrise A

a = int(input())
b = int(input())
print((a ** 2 + b ** 2) ** 0.5)

# Exercise B

n = int(input())
print('The next number for the number ', n, ' is ', n + 1, '.', sep='')
print('The previous number for the number ', n, ' is ', n - 1, '.', sep='')

# Exercise C

n = int(input())
k = int(input())
print(k // n)

# Exercise D

n = int(input())
k = int(input())
print(k % n)

# Exercise E

v = int(input())
t = int(input())
print((v * t) % 109)

# Exercise F

n = int(input())
print(n % 10)

# Exercise G

n = abs(int(input()))
print(n // 10)

# Exercise H

n = int(input())
print(n // 10 % 10)

# Exercise I

n = abs(int(input()))
print(n // 100 + n // 10 % 10 + n % 10)

# Exercise J

n = int(input())
print(n + 2 - n % 2)

# Exercise K

n = int(input()) % 1440
print(n // 60, n % 60)

# Exercise L

n = int(input()) % 86400
h = n // 3600
m = n // 60 % 60
s = n % 60
print(f'{h}:{m:02}:{s:02}')

# Exercise M

a = int(input())
b = int(input())
a, b = b, a
print(a, b)

# Exercise N

k = int(input())
t = 540 + 45 * k + 5 * (k // 2) + 15 * ((k - 1) // 2)
print(t // 60, t % 60)

# Exercise O

a = int(input())
b = int(input())
n = int(input())
total = (a * 100 + b) * n
print(total // 100, total % 100)