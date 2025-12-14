from solution import Solution

tests = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([-1, -2, -3, -4, -5], -8, [2, 4]),
    ([0, 4, 3, 0], 0, [0, 3]),
]

solver = Solution()

for nums, target, expected in tests:
    result = solver.twoSum(nums, target)
    assert result == expected, f"Failed: {nums}, {target}, got {result}"

print("All tests passed.")
