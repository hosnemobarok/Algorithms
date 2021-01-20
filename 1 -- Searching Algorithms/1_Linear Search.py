'''
    Time Complexity     : O(n)
    Space Complexity    : O(1)

    Best Cases          : ---
    Average Cases       : ---
    Worst Cases         : ---

'''
def Linear_Search(li, t):
    n = len(li)
    for i in range(n):
        if li[i] == t:
            return i

    else:
        return 'sorry t is not found!'


# Driver Code
if __name__ == '__main__':
    li = [1, 4, 2, 5, 3]
    t = int(input())
    res = Linear_Search(li, t)
    print(res)