# Python program to Prime Factors
def Prime_Factors(n):
    c = 2
    while n > 1:
        if n % c == 0:
            print(c, end=" ")
            n //= c
        else:
            c += 1

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        Prime_Factors(n)



"""
from math import sqrt
def primeFactors(n):
    while n % 2 == 0:
        print(2, end=' ')
        n //= 2

    for i in range(3, int(sqrt(n))+1, 2):
        while n % i == 0:
            print(i)
            n //= i
    # number greater then 2
    if n > 2:
        print(n)

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        res = primeFactors(n)"""
