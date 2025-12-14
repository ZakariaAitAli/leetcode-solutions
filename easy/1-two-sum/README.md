# 1-two-sum

## Problem

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that their sum equals `target`.

Constraints:
- Exactly one valid solution exists
- The same element cannot be used twice
- Indices can be returned in any order

---

## Examples

### Example 1
**Input**
```

nums = [2, 7, 11, 15]
target = 9

```

**Output**
```

[0, 1]

```

### Example 2
**Input**
```

nums = [3, 2, 4]
target = 6

```

**Output**
```

[1, 2]

```

### Example 3
**Input**
```

nums = [3, 3]
target = 6

```

**Output**
```

[0, 1]

````

---

## Approach

This is a lookup problem, not a brute-force pairing problem.

Core idea:
- For each number `x`, the required counterpart is `target - x`
- If that counterpart was already seen, the solution is complete

Algorithm:
1. Initialize an empty hash map (`value → index`)
2. Iterate through the array once
3. For each element:
   - Compute `complement = target - current_value`
   - If `complement` exists in the map, return both indices
   - Otherwise, store the current value and index

This guarantees a solution in one pass.

---

## Complexity

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

---

## Solution

[solution.py](./solution.py)
