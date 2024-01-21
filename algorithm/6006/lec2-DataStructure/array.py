class Static_array:
    def __init__(self) -> None:
        self.A = []
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        yield from self.A

    def build(self, A):
        self.A = [i for i in A]
        self.size = len(A)

    def get_at(self, i):
        return self.A[i]

    def set_at(self, i, x):
        self.A[i] = x

    def _forward_copy(self, A, i, j, n):
        for k in range(n):
            A[i + k] = self.A[j + k]

    def insert_at(self, i, x):
        cur_len = self.size
        new_arr = [None] * (cur_len + 1)
        self._forward_copy(new_arr, 0, 0, i)  # exclusive index
        new_arr[i] = x
        self._forward_copy(new_arr, i + 1, i, cur_len - i)
        self.build(new_arr)

    def delete_at(self, i):
        cur_len = self.size
        new_arr = [None] * (cur_len - 1)
        self._forward_copy(new_arr, 0, 0, i)
        x = self.get_at(i)
        self._forward_copy(new_arr, i, i + 1, cur_len - i - 1)
        self.build(new_arr)
        return x

    def insert_first(self, x):
        self.insert_at(0, x)

    def delete_first(self):
        return self.delete_at(0)

    def insert_last(self, x):
        self.insert_at(len(self), x)

    def delete_last(self):
        return self.delete_at(len(self) - 1)


test = Static_array()
test.build([1, 2, 3, 4])
print(test.delete_at(2))  # 3
print(test.A)
test.insert_at(1, 3)  # [1,3,2,4]
print(test.A)
test.insert_last(5)  # [1,3,2,4,5]
print(test.A)


