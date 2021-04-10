
def isPrime(num):

    if num < 2: return False

    if num == 2: return True
    if num > 2 and num % 2 == 0: return False

    for i in range(3, num, 2):
        if num % 2 == 0:
            return False
    return True


if __name__ == '__main__':
    for _ in range(int(input())):
        num = int(input())
        res = isPrime(num)
        print(res)
