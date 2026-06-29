"""
1. Two Sum
Difficulty: Easy

Approach:
- For each value, compute complement = target - value.
- If the complement was seen before, return both indices immediately.
- Otherwise, record the current value and its index.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {}

        for i, value in enumerate(nums):
            complement = target - value
            if complement in seen:
                return [seen[complement], i]
            seen[value] = i

        return []  # pragma: no cover — problem guarantees exactly one solution
