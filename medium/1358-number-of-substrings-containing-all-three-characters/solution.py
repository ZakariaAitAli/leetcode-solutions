"""
1358. Number of Substrings Containing All Three Characters
Difficulty: Medium

Approach:
- Sliding window with a count of 'a', 'b', 'c' occurrences in [left, right].
- Advance right, and once the window contains all three characters, shrink
  from the left as much as possible while still containing all three.
- At that point every substring s[i..right] for i in [0, left] also
  contains all three characters, so add (left + 1) to the answer.

Time Complexity: O(n) — each pointer moves forward at most n times
Space Complexity: O(1) — fixed-size count of 3 characters
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {"a": 0, "b": 0, "c": 0}
        left = 0
        result = 0

        for right, char in enumerate(s):
            count[char] += 1

            while all(count.values()):
                count[s[left]] -= 1
                left += 1

            result += left

        return result
