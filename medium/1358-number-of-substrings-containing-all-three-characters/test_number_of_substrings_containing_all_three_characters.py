from solution import Solution


def test_example_1():
    assert Solution().numberOfSubstrings("abcabc") == 10


def test_example_2():
    assert Solution().numberOfSubstrings("aaacb") == 3


def test_example_3():
    assert Solution().numberOfSubstrings("abc") == 1


def test_single_repeated_block():
    assert Solution().numberOfSubstrings("aaabbbccc") == 9


def test_all_same_character():
    assert Solution().numberOfSubstrings("aaaaaaa") == 0
