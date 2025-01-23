from collections import namedtuple

TestData = namedtuple("TestData", "array target expected")

test_data = (
    TestData([1, 2, 3, 4, 5], 1, True),
    TestData([0, 4, 10, 1000], 10, True),
    TestData([], -2, False),
)

