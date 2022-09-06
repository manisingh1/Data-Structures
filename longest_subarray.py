import math
import sys
from typing import List


# def subArray(arr, n):
#     max_sum = -math.inf
#     for i in range(0, n):
        
#         for j in range(i, n):
#             subarr = []
#             for k in range (i, j+1):
#                 subarr.append(arr[k])
#                 max_sum = max(max_sum, sum(subarr))
#                 print(arr[k], end=" ")
#             print("\n", end="")

#     print(max_sum)


# def subArray(arr, n):
#     max_sum = -math.inf
#     for i in range(0, n):
#         subarr = []
#         current_subarray_sum = 0
#         for j in range(i, n):
#             subarr.append(arr[j])
#             current_subarray_sum += arr[j]
#             max_sum = max(max_sum, current_subarray_sum)
#             print(subarr)
#         print("\n", end="")

#     print(max_sum)

def subArray(nums: List[int]) -> int:
    """ Returns max subarray in nums """
    max_sum = -math.inf
    current_sum = 0
    start = 0
    end = 0
    
    for i in range(len(nums)):
        
        if nums[i] > (current_sum + nums[i]):
            start = i
        current_sum = max(nums[i], current_sum + nums[i])
        
        if current_sum > max_sum:
            end = i
        max_sum = max(current_sum, max_sum)
        
    print(max_sum)
    print(nums[start:end+1])
        
    return max_sum

arr = [1, 2, 3, 4]
arr1 = [1]
arr2 = [5,4,-1,7,8]
leetcode_arr = [-2,1,-3,4,-1,2,1,-5,4]
n = len(leetcode_arr)
print ("All Non-empty Subarrays")

subArray(arr2)
