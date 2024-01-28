from typing import Any


class Static_Array:
    def __init__(self) -> None:
        self.A: list[Any] = []
        self.size = 0

    def __iter__(self):
        yield from self.A

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        return str(self.A)

    def build(self, A: list[Any]):
        self.size = len(A)
        new_arr = [None] * self.size
        for i, item in enumerate(A):
            new_arr[i] = item
        self.A = new_arr

    def get_at(self, i: int) -> Any:
        return self.A[i]

    def set_at(self, i: int, x: Any) -> None:
        self.A[i] = x
        return

    def _forward_copy(self, A: list[Any], i: int, j: int, n: int) -> None:
        for k in range(n):
            A[i + k] = self.A[j + k]

    def insert_at(self, i: int, x: Any) -> None:
        new_arr = [None] * (self.size + 1)
        self.size += 1
        self._forward_copy(new_arr, 0, 0, i)
        new_arr[i] = x
        self._forward_copy(new_arr, i + 1, i, self.size - i - 1)
        self.A = new_arr
        return

    def delete_at(self, i: int) -> Any:
        new_arr = [None] * (self.size - 1)
        self.size -= 1
        x = self.A[i]
        self._forward_copy(new_arr, 0, 0, i)
        self._forward_copy(new_arr, i, i+1, self.size-i)
        self.A = new_arr
        return x
        

    def insert_first(self, x: Any) -> None:
        self.size += 1
        self.insert_at(0, x)

    def insert_last(self, x: Any) -> None:
        self.size += 1
        self.insert_at(self.size, x)

    def delete_first(self) -> Any:
        self.size -= 1
        return self.delete_at(0)

    def delete_last(self) -> Any:
        x = self.delete_at(self.size-1)
        self.size -= 1
        return x

class Linked_List_Node:
    def __init__(self,x) -> None:
        self.x:Any = x
        self.next: Linked_List_Node | None = None

    def later_node(self,i:int):
        if i == 0:
            return self
        assert self.next
        return self.next.later_node(i-1)

class Array_Stack(Static_Array):
    def __init__(self):
        super().__init__()



s_arr = Static_Array()
s_arr.build([1, 2, 3, 4, 5])
print(s_arr)
s_arr.insert_at(1, 0)
print(s_arr)
print(s_arr.delete_at(0))
print(s_arr)
print(f"{s_arr.delete_last()=}")
print(s_arr)

arr_stack = Array_Stack()
arr_stack.build([1,2,3,4,5])
print(arr_stack)
