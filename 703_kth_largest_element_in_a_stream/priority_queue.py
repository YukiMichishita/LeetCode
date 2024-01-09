import typing


class PriorityQueue:
    T = typing.TypeVar("T")

    def __init__(self, init_data: typing.Iterable[T], compare_func: typing.Callable[[T, T], bool]):
        self.compare_func = compare_func
        # 2分木を配列として保持する。rootが0,rootの左子ノードが1,rootの右子ノードが2...のように格納する
        self.data = []
        for i in init_data:
            self.push(i)

    def push(self, elem: T):
        self.data.append(elem)
        parent_index = lambda n: (n - 1) // 2
        # 最初の比較対象として末端ノードの親を取得
        new_elem_index = len(self.data) - 1
        target_index = parent_index(len(self.data) - 1)
        if target_index < 0:
            target_index = 0

        # compare_funcのもとで自分より大きい親が現れるまで、親ノードと入れ替える
        while self.compare_func(self.data[target_index], elem):
            self.data[new_elem_index] = self.data[target_index]
            self.data[target_index] = elem
            new_elem_index = target_index
            target_index = parent_index(target_index)
            if target_index < 0:
                break

    def pop(self):
        out = self.data[0]

        # 末端ノードをrootに移動させる
        self.data[0] = self.data[-1]
        self.data = self.data[:-1]

        # compare_funcのもとで自分より大きい子ノードがいる限りrootを子ノードと入れ替える
        # 左右どちらの子も自分より大きい場合は、より大きい方と入れ替える
        moving_node_index = 0
        left_child_index = 1
        right_child_index = 2
        while (self.compare_func(self.data[moving_node_index], self.data[left_child_index])
               or self.compare_func(self.data[moving_node_index], self.data[right_child_index])):
            tmp = self.data[moving_node_index]
            if self.compare_func(self.data[left_child_index], self.data[right_child_index]):
                self.data[moving_node_index] = self.data[right_child_index]
                self.data[right_child_index] = tmp
                moving_node_index = right_child_index
            else:
                self.data[moving_node_index] = self.data[left_child_index]
                self.data[left_child_index] = tmp
                moving_node_index = left_child_index

            left_child_index = 2 * left_child_index + 1
            if left_child_index >= len(self.data):
                break
            right_child_index = 2 * (right_child_index + 1)
            # 左子ノードはあるが右子ノードはいない場合の配列外アクセスを防ぐ
            if right_child_index >= len(self.data):
                right_child_index = left_child_index

        return out


def main():
    int_pq = PriorityQueue([20, 3, 6, 9, 15, 7, 5, 10, 2, 4, 12, 11], lambda x, y: x < y)
    int_pq.push(13)
    print(int_pq.pop())
    int_pq.push(14)
    print(int_pq.pop())
    print(int_pq.pop())
    print(int_pq.pop())

    char_pq = PriorityQueue(["a", "x", "f", "c", "l", "y", "s", "m", "u"], lambda x, y: x > y)
    char_pq.push("b")
    char_pq.push("a")
    print(char_pq.pop())
    print(char_pq.pop())
    print(char_pq.pop())
    print(char_pq.pop())


if __name__ == "__main__":
    main()
