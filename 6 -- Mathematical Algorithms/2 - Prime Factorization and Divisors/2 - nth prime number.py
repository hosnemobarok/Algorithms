def nth_prime_number(n):
    if n==1:
        return 2

    count = 1
    num = 3

    while(count <= n):
        if is_prime(num):
            count +=1
            if count == n:
               return num
        num +=2 #optimization

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True

    if num > 2 and num % 2 == 0:
        return False

    root = int(num ** 0.5)
    for i in range(3, root+1, 2):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        res = nth_prime_number(n)
        print(res)