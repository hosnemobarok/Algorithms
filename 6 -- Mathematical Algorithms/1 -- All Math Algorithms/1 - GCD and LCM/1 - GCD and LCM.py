
def GCD(num1, num2):
    while num2:
        # a, b swap and a % b val
        num1, num2 = num2, (num1 % num2)
    return num1

def LCM(num1, num2):
    return (num1 // GCD(num1, num2) * num2)


# Driver Code
if __name__ == '__main__':
    # for _ in range(int(input().split()))
        num1, num2 = map(int, input().split())

        res_GCD = GCD(num1, num2)
        res_LCM = LCM(num1, num2)
        print(f'num1:->{num1} num2:->{num2}-> GCD:->',res_GCD)
        print(f'num1:->{num1} num2:->{num2}-> LCM:->', res_LCM)



from math import gcd, lcm
a, b = 15, 20
print(f'{a} and {b}->GCD:->', gcd(a, b))
print(f'{a} and {b}->LCM:->', lcm(a, b))

