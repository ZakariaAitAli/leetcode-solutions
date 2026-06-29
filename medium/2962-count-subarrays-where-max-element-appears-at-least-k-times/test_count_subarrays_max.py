from solution import Solution


def test_example_1():
    # max=3 at indices 1,3; valid windows: [0,3],[0,4],[1,3],[1,4]
    assert Solution().countSubarrays([1, 3, 2, 3, 1], 2) == 4


def test_example_2():
    # max=4 appears only once, can never reach k=3
    assert Solution().countSubarrays([1, 4, 2, 1], 3) == 0


def test_all_equal_k1():
    # every subarray contains the max at least once
    assert Solution().countSubarrays([3, 3, 3], 1) == 6


def test_all_equal_k2():
    # subarrays of length >= 2 contain max at least twice: [0,1],[0,2],[1,2]
    assert Solution().countSubarrays([3, 3, 3], 2) == 3


def test_dense_max_k2():
    # [3,3,3,3]: all C(4,2) + 4 length-1 subarrays except length-1 → length>=2: 6
    assert Solution().countSubarrays([3, 3, 3, 3], 2) == 6


def test_single_element():
    assert Solution().countSubarrays([5], 1) == 1
