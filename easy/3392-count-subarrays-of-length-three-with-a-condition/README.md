# 3392. Count Subarrays of Length Three With a Condition

## Problem

Given an integer array `nums`, return the number of subarrays of length 3 such that the sum of the first and third numbers equals exactly half of the second number.

---

## Example

**Input:**  
`nums = [1,2,1,4,1]`  
**Output:**  
`1`

**Input:**  
`nums = [1,1,1]`  
**Output:**  
`0`

---

## Approach

- Loop over all subarrays of size 3.
- Check if `(first element + third element) == (half of the middle element)`.
- Increment a counter whenever the condition is true.
- Return the final count.

---

## Complexity

- Time Complexity: **O(n)** (single pass)
- Space Complexity: **O(1)** (constant extra space)

---

## Solution

[solution.py](./solution.py)
