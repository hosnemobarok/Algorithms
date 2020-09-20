"""
    Time    Complexity      --> O(log n)
    Space   Complexity      --> O(1)

"""
class Solution:

    def BinarySearch(self, Li, target):
        left = 0
        right = len(Li) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if Li[mid] == target:
                return mid

            elif Li[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return "sorry target is not found!"



if __name__=="__main__":
    op = Solution()

    Li = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    target = int(input())
    result = op.BinarySearch(Li, target)

    print(result)