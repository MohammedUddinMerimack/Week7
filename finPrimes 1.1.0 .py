import random

def guess():
    return random.randint(2, 5000)

#Modified Function isPrime
def isPrime(x):
    # Check if x is less than 2 (not prime)
    if x < 2:
        return False
    # Handle the special case for the number 2 (a prime number)
    if x == 2:
        return True
    # Check if x is an even number (except 2, which is already handled)
    if x % 2 == 0:
        return False  # Skip even numbers (except 2)

    # Optimize the loop by starting from 3 and checking odd values up to the square root of x
    for i in range(3, int(x**0.5) + 1, 2):  
        if x % i == 0:
            return False  # x is divisible by i, so it's not a prime number

    return True  # If no divisors are found, x is a prime number

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

