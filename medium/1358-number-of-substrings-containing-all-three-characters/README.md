# 1358. Number of Substrings Containing All Three Characters

## Problem

Given a string `s` consisting only of characters `a`, `b` and `c`.

Return the number of substrings containing at least one occurrence of all these characters `a`, `b` and `c`.

Constraints:
- `3 <= s.length <= 5 x 10^4`
- `s` only consists of `a`, `b` or `c` characters.

---

## Examples

### Example 1
**Input:**
```
s = "abcabc"
```
**Output:** `10`

### Example 2
**Input:**
```
s = "aaacb"
```
**Output:** `3`

### Example 3
**Input:**
```
s = "abc"
```
**Output:** `1`

---

## Approach

Sliding window with a count of `a`, `b`, `c` occurrences in `[left, right]`.
Advance `right`, and once the window contains all three characters, shrink
from the left as much as possible while still containing all three. At that
point every substring `s[i..right]` for `i` in `[0, left]` also contains all
three characters, so add `left + 1` to the answer (since `left` is now
already advanced past the shrink, this is simply `left`).

---

## Complexity

- Time Complexity: `O(n)` — each pointer moves forward at most n times
- Space Complexity: `O(1)` — fixed-size count of 3 characters

---

## Solution

[solution.py](./solution.py)
