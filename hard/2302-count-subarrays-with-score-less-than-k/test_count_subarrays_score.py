from solution import Solution


def test_example_1():
    assert Solution().countSubarrays([2, 1, 4, 3, 5], 10) == 6


def test_example_2():
    assert Solution().countSubarrays([1, 1, 1], 5) == 5


def test_single_element_below_k():
    assert Solution().countSubarrays([1], 2) == 1


def test_single_element_at_k():
    # score = 2 * 1 = 2, not < 2
    assert Solution().countSubarrays([2], 2) == 0


def test_window_shrinks_to_empty():
    # [1,2]: score = 3*2 = 6 >= 4; [1]: 1 < 4; [2]: 2 < 4
    assert Solution().countSubarrays([1, 2], 4) == 2


def test_all_subarrays_valid():
    assert Solution().countSubarrays([1, 1], 10) == 3
