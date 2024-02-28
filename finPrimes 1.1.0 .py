import random

def guess():
    return random.randint(2, 5000)

def isPrime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False  # Skip even numbers (except 2)

    for i in range(3, int(x**0.5) + 1, 2):  # Check odd values starting from 3
        if x % i == 0:
            return False

    return True


def findPrimes(num):
    primes = []
    for i in range(num):
        p = guess()
        while not isPrime(p):
            p = guess()
        primes += [p]
    return primes

import cProfile
cProfile.run('print(findPrimes(500)[:10])')

