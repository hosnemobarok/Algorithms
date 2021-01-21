'''
    Time Complexity     : O(n^2)
    Space Complexity    : O(1)


    Best Case           : O(n)

    Worst Case          : O(n^2)
    Average Case        : O(n^2)
'''

def Bubble_Sort(li):
    # li size store
    size = len(li)

    for i in range(size-1):
        for j in range(0, size-i-1):
            if li[j] > li[j+1]:

                # li[0] and li[i] index value [swap]
                li[j], li[j+1] = li[j+1], li[j]

    return li


# Driver Code
if __name__ == '__main__':
    li = [5, 1, 3, 2, 4]
    res = Bubble_Sort(li)
    print(res)
