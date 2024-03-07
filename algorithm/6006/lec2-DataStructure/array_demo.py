class Static_array:
    def __init__(self) -> None:
        self.A = []
        self.size = 0

    def __len__(self)->int:
        return self.size

    def __iter__(self):
        yield from self.A

    def __str__(self)->str:
        return str(self.A)

    def build(self, A):
        arr = [None]*len(A)
        for i,item in enumerate(A):
            arr[i] = A[i] # copy

    def get_at(self, i):
        return self.A[i]

    def set_at(self, i, x)-> None:
        self.A[i] = x

    def _forward_copy(self, A, i, j, n):
        for k in range(n):
            A[k+i] = self.A[k+j]

    def insert_at(self, i, x):
        new_arr = [None] *(self.size +1)
        self._forward_copy(new_arr,0,0,i) # [:i]
        new_arr[i] = x #[i]
        self._forward_copy(new_arr,i+1,i,self.size -i -1) #[i+1:]
        self.size += 1


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
print(test)


