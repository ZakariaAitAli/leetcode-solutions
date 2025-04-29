# 2962. Count Subarrays Where Max Element Appears at Least K Times

## Problem

You are given an integer array `nums` and a positive integer `k`.

Return the number of **subarrays** where the **maximum element** of `nums` appears **at least `k` times** in that subarray.

A **subarray** is a contiguous sequence of elements within an array.

---

## Examples

**Example 1:**

```txt
Input: nums = [1,3,2,3,3], k = 2
Output: 6

Explanation:
The subarrays that contain the element 3 at least 2 times are:
[1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3], [3,3]
```

**Example 2:**

```txt
Input: nums = [1,4,2,1], k = 3
Output: 0

Explanation:
No subarray contains the element 4 at least 3 times.
```

---

## Approach

- First, determine the **maximum element** `max_val` in the entire array.
- Use the **two-pointer sliding window** technique:
  - Expand the window to the right while counting how many times `max_val` appears.
  - If it appears **at least `k` times**, then all subarrays starting from `left` to `right` and ending anywhere from `right` to the end are valid.
  - Move the `left` pointer to reduce the frequency of `max_val` and continue.

---

## Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---

## Solution

[solution.py](./solution.py)
