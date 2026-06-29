# 1967. Number of Strings That Appear as Substrings in Word

## Problem

Given an array of strings `patterns` and a string `word`, return the number of strings in `patterns` that exist as a substring in `word`.

Constraints:
- `1 <= patterns.length <= 100`
- `1 <= patterns[i].length <= 100`
- `1 <= word.length <= 100`
- `patterns[i]` and `word` consist of lowercase English letters

---

## Examples

### Example 1
**Input:**
```
patterns = ["a","abc","bc","d"]
word = "abc"
```
**Output:** `3`

### Example 2
**Input:**
```
patterns = ["a","b","c"]
word = "aaaaabbbbb"
```
**Output:** `2`

### Example 3
**Input:**
```
patterns = ["a","a","a"]
word = "ab"
```
**Output:** `3`

---

## Approach

For each pattern, check if it is a substring of `word` using Python's `in` operator.
Duplicate patterns each count independently.

---

## Complexity

- Time Complexity: `O(k * n * m)` — k patterns, n = len(word), m = len(pattern)
- Space Complexity: `O(1)`

---

## Solution

[solution.py](./solution.py)
