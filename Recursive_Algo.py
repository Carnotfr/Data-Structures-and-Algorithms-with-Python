import sys
sys.setrecursionlimit(10000)


def powerOfTwo(n):
    if n == 0:
        return 1
    else:
        power = powerOfTwo (n - 1)
        return power * 2


#Iterative function
def powerOfTwoIt(n):
    i = 0 
    power = 1
    while i < n:
        power = power * 2
        i += 1
        return power

#Factorial function
def factorial(n):
    assert n>=0 and int(n) == n, 'The number must be positive integer only'
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(10))

#Fibonacci function
def fibonacci(n):
    assert n >= 0 and int(n) == n, 'The number must be positive integer only'
    if n in [0, 1]:
        return n
    else:

        return fibonacci(n-1) + fibonacci(n-2) 

print(fibonacci(5))

#Sum of digits using recursion

def sumOfDigits(n):
    assert n >= 0 and int(n) == n, 'The number must be positive integer only'
    if n == 0:
        return 0
    else:
        return int(n%10) + sumOfDigits(int(n//10))

print(sumOfDigits(854))

# Power of a number using recursion
def powerOfNumber(base, exponent):
    assert int(exponent) == exponent, 'The exponent must be integer only'
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1/base * powerOfNumber(base, exponent - 1)
    return base * powerOfNumber(base, exponent - 1)

print(powerOfNumber(5, 5))

# Great Common Diviser 

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print(gcd(48, 18))

# Convert a number decimal to binary
def decimalToBinary(m):
    assert int (m) == m, 'The number must be integer only'

    if m == 0:
        return 0
    else:
        return m % 2 + 10 * decimalToBinary(int(m//2))

print(decimalToBinary(10))

