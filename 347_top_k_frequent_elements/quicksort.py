import random
from typing import List
from statistics import median

def quick_sort(target: List):
    def partition(target: List, left: int, right: int, pivot: int):
        while True:
            while target[left] < pivot:
                left += 1
            while target[right] > pivot:
                right -= 1
            if left >= right:
                return left - 1
            target[left], target[right] = target[right], target[left]
            left += 1
            right -= 1

    def quick_sort_impl(target: List, left: int, right: int):
        if left == right:
            return
        pivot = median([target[left], target[right], target[left + (right - left + 1) // 2]])
        p = partition(target, left, right, pivot)
        quick_sort_impl(target, left, p)
        quick_sort_impl(target, p + 1, right)

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
    target = [random.randint(0, 1000) for _ in range(1000)]
    original = target.copy()
    quick_sort(target)
    assert target == sorted(original), f"target is not sorted original:{original},target:{target}"
