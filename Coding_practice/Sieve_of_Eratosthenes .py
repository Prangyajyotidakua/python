def fun(limit):
    primes = [True] * (limit + 1)

    primes[0] = primes[1] = False

    for num in range(2, int(limit**0.5) + 1):
        if primes[num]:
            for multiple in range(num * num, limit + 1, num):
                primes[multiple] = False

    prime_numbers = []
    for num, prime in enumerate(primes):
        if prime:
            prime_numbers.append(num)

    return prime_numbers

limit = 50
result = fun(limit)
print(result)
