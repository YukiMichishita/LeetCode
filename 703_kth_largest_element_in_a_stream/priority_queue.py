import typing


class PriorityQueue:
    T = typing.TypeVar("T")

    def __parent_index(self, index: int) -> int:
        return (index - 1) // 2

    def __left_child_index(self, index: int) -> int:
        return 2 * index + 1

    def __right_child_index(self, index: int) -> int:
        return 2 * (index + 1)

    def has_child(self, index: int) -> bool:
        return self.__left_child_index(index) < len(self.data)

    def larger_child_index(self, index: int) -> typing.Optional[int]:
        if not self.has_child(index):
            return None

        left_index = self.__left_child_index(index)
        right_index = self.__right_child_index(index)
        if right_index >= len(self.data) or self.compare_func(self.data[right_index], self.data[left_index]):
            return left_index

        return right_index

    def __init__(self, init_data: typing.Iterable[T], compare_func: typing.Callable[[T, T], bool]):
        self.compare_func = compare_func
        # 2分木を配列として保持する。rootが0,rootの左子ノードが1,rootの右子ノードが2...のように格納する
        self.data = []
        for i in init_data:
            self.push(i)

    def push(self, elem: T):
        new_elem_index = len(self.data)
        self.data.append(elem)

        # compare_funcのもとで自分より大きい親が現れるまで、親ノードと入れ替える
        while new_elem_index > 0:
            parent_index = self.__parent_index(new_elem_index)
            if self.compare_func(elem, self.data[parent_index]):
                break

            self.data[parent_index], self.data[new_elem_index] = self.data[new_elem_index], self.data[parent_index]
            new_elem_index = parent_index

    def pop(self):
        if len(self.data) <= 0:
            return None
        out = self.data[0]
        # 末端ノードをrootに移動させる
        self.data[0] = self.data[-1]
        self.data = self.data[:-1]

        # compare_funcのもとで自分より大きい子ノードがいる限りrootを子ノードと入れ替える
        # 左右どちらの子も自分より大きい場合は、より大きい方と入れ替える
        moving_node_index = 0
        while self.has_child(moving_node_index):
            larger_child_index = self.larger_child_index(moving_node_index)
            if self.compare_func(self.data[larger_child_index], self.data[moving_node_index]):
                break

            self.data[moving_node_index], self.data[larger_child_index] = self.data[larger_child_index], self.data[
                moving_node_index]
            moving_node_index = larger_child_index

        return out


def main():
    desc_pq = PriorityQueue([20, 3, 6, 9, 15, 7, 5, 10, 2, 4, 12, 11], lambda x, y: x < y)
    desc_pq.push(13)
    print(desc_pq.pop())
    desc_pq.push(14)
    print(desc_pq.pop())
    print(desc_pq.pop())
    print(desc_pq.pop())

    asc_pq = PriorityQueue([], lambda x, y: x > y)
    print(asc_pq.pop())
    asc_pq.push(1)
    asc_pq.push(4)
    asc_pq.push(5)
    print(asc_pq.pop())
    print(asc_pq.pop())

    char_pq = PriorityQueue(["a", "x", "f", "c", "l", "y", "s", "m", "u"], lambda x, y: x > y)
    char_pq.push("b")
    char_pq.push("a")
    print(char_pq.pop())
    print(char_pq.pop())
    print(char_pq.pop())
    print(char_pq.pop())


if __name__ == "__main__":
    main()
