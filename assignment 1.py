# Exsecrise A

a = int(input())
b = int(input())
print((a ** 2 + b ** 2) ** 0.5)

# Exsecrise B

n = int(input())
print('The next number for the number ', n, ' is ', n + 1, '.', sep='')
print('The previous number for the number ', n, ' is ', n - 1, '.', sep='')

# Exsecrise C

n = int(input())
k = int(input())
print(k // n)

# Exsecrise D

n = int(input())
k = int(input())
print(k % n)

# Exsecrise E

v = int(input())
t = int(input())
print((v * t) % 109)

# Exsecrise F

n = int(input())
print(n % 10)

# Exsecrise G

n = abs(int(input()))
print(n // 10)

# Exsecrise H

n = int(input())
print(n // 10 % 10)

# Exsecrise I

n = abs(int(input()))
print(n // 100 + n // 10 % 10 + n % 10)

# Exsecrise J

n = int(input())
print(n + 2 - n % 2)

# Exsecrise K

n = int(input()) % 1440
print(n // 60, n % 60)

# Exsecrise L

n = int(input()) % 86400
h = n // 3600
m = n // 60 % 60
s = n % 60
print(f'{h}:{m:02}:{s:02}')

# Exsecrise M

a = int(input())
b = int(input())
a, b = b, a
print(a, b)

# Exsecrise N

k = int(input())
t = 540 + 45 * k + 5 * (k // 2) + 15 * ((k - 1) // 2)
print(t // 60, t % 60)

# Exsecrise O

a = int(input())
b = int(input())
n = int(input())
total = (a * 100 + b) * n
print(total // 100, total % 100)