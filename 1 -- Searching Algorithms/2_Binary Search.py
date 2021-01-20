'''
    Time Complexity     : O(log n)
    Space Complexity    : O(1)

    Best Cases          : ---
    Average Cases       : ---
    Worst Cases         : ---

'''

# Iterative implementation of Binary Search
def Binary_Search(li, t):
    left = 0
    right = len(li)-1

    while left <= right:

        mid = left + (right - left) // 2
        if li[mid] == t:
            return mid

        elif li[mid] < t:
            left = mid + 1

        else:
            right = mid - 1

    else:
        return 'sorry t is not found!'


# Driver Code
if __name__ == '__main__':
    # Sorted Array
    li = [1, 3, 5, 7, 9]
    t = int(input())
    res = Binary_Search(li, t)
    print(res)