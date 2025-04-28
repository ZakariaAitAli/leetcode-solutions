# 2302. Count Subarrays With Score Less Than K

## Problem

The score of an array is defined as the product of its sum and its length.

Given a positive integer array `nums` and an integer `k`, return the number of non-empty subarrays of `nums` whose score is strictly less than `k`.

A subarray is a contiguous sequence of elements within an array.

---

## Example

**Input:**  
`nums = [2,1,4,3,5]`, `k = 10`  
**Output:**  
`6`

**Input:**  
`nums = [1,1,1]`, `k = 5`  
**Output:**  
`5`

---

## Approach

- Use two pointers (`left` and `right`) to maintain a sliding window.
- Extend the window to the right by adding `nums[right]` to the current sum.
- Shrink the window from the left if the score (`current_sum * window_size`) becomes greater than or equal to `k`.
- For each valid window ending at `right`, add the number of valid subarrays (`right - left + 1`) to the answer.

---

## Complexity

- Time Complexity: **O(n)** (single pass over the array)
- Space Complexity: **O(1)** (only a few extra variables)

---

## Solution

[solution.py](./solution.py)
