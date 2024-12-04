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
    else:
        primes += [i]
print('Primes:', primes)
print('Not Primes:', not_primes)
