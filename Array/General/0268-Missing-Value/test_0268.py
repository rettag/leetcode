from problem_0268 import missingNumber


def test_one():
    nums = [0, 1, 2, 3, 4, 6]  
    expected = 5

    assert missingNumber(nums) == expected


def test_two():
    nums = [4, 2, 3, 0]  
    expected = 1

    assert missingNumber(nums) == expected


def test_three():
    nums = [3,0,1]
    expected = 2

    assert missingNumber(nums) == expected


def test_four():
    nums = [1,2]
    expected = 0

    assert missingNumber(nums) == expected