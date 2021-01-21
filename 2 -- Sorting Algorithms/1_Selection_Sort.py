'''
    Time Complexity     : O(n^2)
    Space Complexity    : O(1)
'''

def Selection_Sort(li):
    # li size store
    size = len(li)

    for i in range(size-1):

        min_ind = i

        for j in range(i+1, size):
            if li[min_ind] > li[j]:
                min_ind = j

        # swap
        li[i], li[min_ind] = li[min_ind], li[i]

    return li
# Driver Code
if __name__ == '__main__':
    li = [5, 1, 4, 2, 3]
    res = Selection_Sort(li)
    print(res)
