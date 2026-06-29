"""
3392. Count Subarrays of Length Three With a Condition
Difficulty: Easy

Approach:
- Loop through the array to check each subarray of length 3.
- For each subarray, check if nums[i] + nums[i+2] == nums[i+1] / 2.
- If true, increment the count.
- Return the final count.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) - 2):
            if nums[i] + nums[i + 2] == nums[i + 1] / 2:
                count += 1
        return count
