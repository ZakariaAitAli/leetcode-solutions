"""
2302. Count Subarrays With Score Less Than K
Difficulty: Hard

Approach:
- Use a sliding window. For each right pointer, shrink the left pointer
  while the score (sum * length) of the current window is >= k.
- The number of valid subarrays ending at right is right - left + 1.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0
        current_sum = 0

        for right in range(len(nums)):
            current_sum += nums[right]
            while left <= right and current_sum * (right - left + 1) >= k:
                current_sum -= nums[left]
                left += 1
            count += right - left + 1

        return count
