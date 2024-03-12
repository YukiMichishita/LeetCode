import random
from typing import List


def median3(x, y, z):
    return max(min(x, y), min(max(x, y), z))


def quick_sort(target: List):
    def quick_sort_impl(target: List, left: int, right: int):
        if left == right:
            return
        prev_left = left
        prev_right = right

        pivot = median3(target[left], target[left + (right - left) // 2], target[right])
        while True:
            while target[left] < pivot:
                left += 1
            while target[right] > pivot:
                right -= 1
            if left > right:
                quick_sort_impl(target, prev_left, left - 1)
                quick_sort_impl(target, left, prev_right)
                return
            target[left], target[right] = target[right], target[left]
            left += 1
            right -= 1

    quick_sort_impl(target, 0, len(target) - 1)


a = [8, 4, 3, 7, 6, 5, 2, 1, 8, 6]
quick_sort(a)
print(a)
assert a == sorted(a), "a is not sorted"
b = [423, 246, 437, 513, 844, 716, 153, 609, 150, 163]
quick_sort(b)
print(b)
assert b == sorted(b), "b is not sorted"
c = [67, 88, 58, 49, 56, 98, 8, 45, 15, 67, 56]
quick_sort(c)
print(c)
assert c == sorted(c), "c is not sorted"

for _ in range(100):
    target = [int(random.random() * 1000) for i in range(1000)]
    original = target.copy()
    quick_sort(target)
    assert target == sorted(original), f"target is not sorted original:{original},target:{target}"
