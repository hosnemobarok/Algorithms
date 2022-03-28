"""
    Time Complexity: This Approach is best for all composite numbers and achieves O(log n) but is O(n) otherwise.
    Auxiliary Space: O(1)
"""

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
