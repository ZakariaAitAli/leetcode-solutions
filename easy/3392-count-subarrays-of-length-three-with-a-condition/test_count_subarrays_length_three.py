from solution import Solution


def test_example_1():
    # i=2: nums[2]+nums[4] = 1+1 = 2 == nums[3]/2 = 4/2 = 2
    assert Solution().countSubarrays([1, 2, 1, 4, 1]) == 1


def test_example_2():
    assert Solution().countSubarrays([1, 1, 1]) == 0


def test_single_triple_match():
    assert Solution().countSubarrays([1, 4, 1]) == 1


def test_no_match():
    assert Solution().countSubarrays([1, 2, 3]) == 0


def test_two_matches():
    # i=0: 1+1=2 == 4/2=2 ✓; i=3: 2+2=4 == 8/2=4 ✓
    assert Solution().countSubarrays([1, 4, 1, 2, 8, 2]) == 2


def test_odd_middle_no_match():
    # nums[i+1] is odd so nums[i+1]/2 is float; sum of ints can't equal it
    assert Solution().countSubarrays([1, 3, 1]) == 0
