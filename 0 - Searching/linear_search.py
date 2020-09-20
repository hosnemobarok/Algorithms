"""
    Time Complexity  -->    O(n)
    Space Complexity -->    O(1)
    best case        -->    O(1)
    worst case       -->    O(n)
    average case     -->    O(n/2)

"""
class Solution:

    def LinearSearch(self, Li, target):
        length = len(Li)
        for i in range(length):
            if Li[i] == target:
                return i

        return "Sorry targets is not found!"


if __name__=="__main__":
    op = Solution()

    Li = [4, 1, 2, 3, 5, 3, 5]
    target = int(input())
    res = op.LinearSearch(Li, target)

    print(res)
