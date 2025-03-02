from problem_0217 import containsDuplicate


def test_base():
    nums = [1]
    expected = False

    assert containsDuplicate(nums) == expected


def test_one():
    nums = [1,2,3,1]  
    expected = True

    assert containsDuplicate(nums) == expected


def test_two():
    nums = [1,2,3,3,5,5,4,1]  
    expected = True

    assert containsDuplicate(nums) == expected


def test_three():
    nums = [1,2,3,5,4]  
    expected = False

    assert containsDuplicate(nums) == expected


def test_four():
    nums = [1,2]
    expected = False

    assert containsDuplicate(nums) == expected