from solution import Solution


def test_example_1():
    assert Solution().numOfStrings(["a", "abc", "bc", "d"], "abc") == 3


def test_example_2():
    assert Solution().numOfStrings(["a", "b", "c"], "aaaaabbbbb") == 2


def test_example_3():
    # duplicate patterns each count independently
    assert Solution().numOfStrings(["a", "a", "a"], "ab") == 3


def test_no_match():
    assert Solution().numOfStrings(["x", "y", "z"], "abc") == 0


def test_all_match():
    assert Solution().numOfStrings(["a", "b", "ab"], "ab") == 3


def test_single_match():
    assert Solution().numOfStrings(["abc"], "abc") == 1


def test_pattern_longer_than_word():
    assert Solution().numOfStrings(["abcd"], "abc") == 0
