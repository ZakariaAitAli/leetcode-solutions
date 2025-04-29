from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        n = len(nums)
        count = 0
        left = 0
        max_freq = 0

        for right in range(n):
            if nums[right] == max_val:
                max_freq += 1

            while max_freq >= k:
                count += n - right
                if nums[left] == max_val:
                    max_freq -= 1
                left += 1

        return count
