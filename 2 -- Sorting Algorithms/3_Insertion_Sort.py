'''
    Time Complexity     : O(n^2)
    Space Complexity    : O(1)
'''

def Insertion_Sort(li):
    size = len(li)

    for i in range(1, size):
        # li[1] index number value store
        key = li[i]

        # li[0] index number value store
        j = i-1

        while j >= 0 and li[j] > key:
            li[j+1] = li[j]
            j -= 1

        li[j+1] = key

    return li



# Driver Code
if __name__ == '__main__':
    li = [4, 1, 5, 2, 3]
    res = Insertion_Sort(li)
    print(res)