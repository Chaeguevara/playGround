class Static_array:
    def __init__(self) -> None:

    def __len__(self):

    def __iter__(self):

    def build(self, A):

    def get_at(self, i):

    def set_at(self, i, x):

    def _forward_copy(self, A, i, j, n):

    def insert_at(self, i, x):

    def delete_at(self, i):

    def insert_first(self, x):

    def delete_first(self):

    def insert_last(self, x):

    def delete_last(self):


test = Static_array()
test.build([1, 2, 3, 4])
print(test.delete_at(2))  # 3
print(test.A)
test.insert_at(1, 3)  # [1,3,2,4]
print(test.A)
test.insert_last(5)  # [1,3,2,4,5]
print(test.A)


