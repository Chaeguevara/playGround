from typing import Any, Optional, Self

class Array_seq:
    def __init__(self):
        self.A = []
        self.size = 0

    def __len__(self):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

    def build(self, X: list[Any]):
        raise NotImplementedError

    def get_at(self, i):
        raise NotImplementedError

    def set_at(self, i, x):
        raise NotImplementedError

    def _copy_forward(self, i, n, A, j):
        raise NotImplementedError

    def _copy_backward(self, i, n, A, j):
        raise NotImplementedError

    def insert_at(self, i, x):
        raise NotImplementedError

    def delete_at(self, i):
        raise NotImplementedError

    def insert_first(self, x):
        raise NotImplementedError

    def delete_first(self):
        raise NotImplementedError

    def insert_last(self, x):
        raise NotImplementedError

    def delete_last(self):
        raise NotImplementedError

#---------------- LL Sequence

class Linked_List_Node:

    def __init__(self, x) -> None:
        self.item = x
        self.next: Optional[Self] = None

    def later_node(self, i: int) -> Self:
        raise NotImplementedError

class Linked_List_Seq:
    def __init__(self) -> None:
        self.head: Optional[Linked_List_Node] = None
        self.size = 0

    def __len__(self) -> int:
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

    def build(self, A: list) -> None:
        raise NotImplementedError

    def get_at(self, i: int):
        raise NotImplementedError

    def insert_first(self, item: Any) -> None:
        raise NotImplementedError

    def delete_first(self) -> Optional[Linked_List_Node]:
        raise NotImplementedError

    def insert_at(self, i: int, item) -> None:
        raise NotImplementedError

    def delete_at(self, i) -> Optional[Linked_List_Node]:
        raise NotImplementedError

    def insert_last(self, item) -> None:
        raise NotImplementedError

    def delete_last(self) -> Optional[Linked_List_Node]:
        raise NotImplementedError

#Dynamic sequence
class Dynamic_Array_Sequence(Array_seq):
    def __init__(self, r=2):
        super().__init__()
        self.size = 0
        self.r = r #r=2 -> doubling
        self._compute_bounds()
        self._resize(0)

    def __len__(self): #O(1)
        raise NotImplementedError

    def __iter__(self): #O(n)
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

    def build(self, X: list[Any]): #O(n)
        raise NotImplementedError

    def _compute_bounds(self): #O(1)
        raise NotImplementedError

    def _resize(self, n):
        raise NotImplementedError

    def insert_last(self, x):
        raise NotImplementedError

    def delete_last(self):
        raise NotImplementedError

    def insert_at(self, i, x):
        raise NotImplementedError

    def delete_at(self, i):
        raise NotImplementedError

    def insert_first(self, x):
        raise NotImplementedError

    def delete_first(self):
        raise NotImplementedError
