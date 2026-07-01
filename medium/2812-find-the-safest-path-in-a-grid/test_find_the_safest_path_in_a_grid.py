from solution import Solution


def test_example_1():
    assert Solution().maximumSafenessFactor([[1, 0, 0], [0, 0, 0], [0, 0, 1]]) == 0


def test_example_2():
    assert Solution().maximumSafenessFactor([[0, 0, 1], [0, 0, 0], [0, 0, 0]]) == 2


def test_example_3():
    grid = [[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]
    assert Solution().maximumSafenessFactor(grid) == 2


def test_single_cell_thief():
    assert Solution().maximumSafenessFactor([[1]]) == 0


def test_interior_thief():
    # Only the 4 corners are distance 2 from the center thief; any path between
    # opposite corners must cross a distance-1 edge cell, so the answer is 1.
    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert Solution().maximumSafenessFactor(grid) == 1
