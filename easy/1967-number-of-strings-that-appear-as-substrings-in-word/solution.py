"""
1967. Number of Strings That Appear as Substrings in Word
Difficulty: Easy

Approach:
- For each pattern, check if it is a substring of word using the `in` operator.
- Count how many patterns satisfy the check.

Time Complexity: O(k * n * m) — k patterns, n = len(word), m = len(pattern)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(p in word for p in patterns)
