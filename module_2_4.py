#Третий вариант (vebinar)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        continue
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print('primes', primes)
print('not_primes', not_primes)

"""
второй вариант
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers[1:]:
    k = 0
    for j in numbers[1:i-1]:
        if i % j == 0:
            k += 1
            break
    if k > 0:
        not_primes += [i]
    else:
        primes += [i]
print('Primes:', primes)
print('Not Primes:', not_primes)

Первый вариант
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers[1:]:
    k = 0
    for j in numbers[1:i]:
        if i % j == 0:
            k += 1
        if k > 1:
            not_primes += [i]
            break
    if k == 1:
        primes += [i]
print('Primes:', primes)
print('Not Primes:', not_primes)
"""