from typing import Callable


my_list: list[int | float] = [1, 2, 3, 4.5]  # the list can receive int and float


def valid_pass(submited_pass: str, hash_method: str = "sh256") -> bool:
    return tuple


"""callble func takes two args
 1) the list of numbers
 2) function which takes as args list of numbers and retuns an int
"""


def callable_func(nums: list[int], func: Callable[[int], int]):
    return [func(i) for i in nums]


def square(v: int):
    return v**2


def main():
    nums = [1, 2, 3]
    print(callable_func(nums, square))


if __name__ == "__main__":
    main()
