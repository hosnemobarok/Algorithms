# Python3 Program for recursive binary search.

# Returns index of x in arr if present, else -1
def binarySearch (arr, left, right, x):

	# Check base case
	if right >= left:

		mid = left + (right - left) // 2

		# If element is present at the middle itself
		if arr[mid] == x:
			return mid

		# If element is smaller than mid, then it
		# can only be present in left subarray
		elif arr[mid] > x:
			return binarySearch(arr, left, mid-1, x)

		# Else the element can only be present
		# in right subarray
		else:
			return binarySearch(arr, mid + 1, right, x)

	else:
		# Element is not present in the array
		return -1

# Driver Code
arr = [ 2, 3, 4, 10, 40 ]
x = 10

left = 0
right = len(arr) - 1

# Function call
result = binarySearch(arr, left, right, x)

if result != -1:
	print ("Element is present at index % d" % result)
else:
	print ("Element is not present in array")
