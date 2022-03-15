def isPrime(num):
    
    if num <= 1: return False
    if num == 2: return True

    if num > 2 and num % 2 == 0: return False

    root = int(num ** 0.5)

    for i in range(3, root+1, 2):
        print(i)
        
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    for _ in range(int(input())):
        num = int(input())
        res = isPrime(num)
        print(res)
