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
