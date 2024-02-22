from typing import Any, Optional, Self


class Array_seq:
    def __init__(self):
        self.A = []
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        yield from self.A

    def __str__(self) -> str:
        return str(self.A)

    def build(self, X: list[Any]):
        self.A = [a for a in X]
        self.size = len(self.A)

    def get_at(self, i):
        return self.A[i]

    def set_at(self, i, x):
        self.A[i] = x

    def _copy_forward(self, i, n, A, j):
        for k in range(n):
            A[j + k] = self.A[i + k]

    def _copy_backward(self, i, n, A, j):
        for k in range(n - 1, -1, -1):
            A[j + k] = self.A[i + k]

    def insert_at(self, i, x):
        n = self.size
        A = [None] * (self.size + 1)
        self._copy_forward(0, i, A, 0)
        A[i] = x
        self._copy_forward(i, n - i, A, i + 1)
        self.build(A)

    def delete_at(self, i):
        n = len(self)
        A = [None] * (n - 1)
        self._copy_forward(0, i, A, 0)
        x = self.A[i]
        self._copy_forward(i + 1, n - i - 1, A, i)
        self.build(A)
        return x

    def insert_first(self, x):
        self.insert_at(0, x)

    def delete_first(self):
        return self.delete_at(0)

    def insert_last(self, x):
        self.insert_at(len(self), x)

    def delete_last(self):
        return self.delete_at(len(self) - 1)


class Linked_List_Node:

    def __init__(self, x) -> None:
        self.item = x
        self.next: Optional[Self] = None

    def later_node(self, i: int) -> Self:
        if i == 0:
            return self
        assert self.next
        return self.next.later_node(i - 1)


class Linked_List_Seq:
    def __init__(self) -> None:
        self.head: Optional[Linked_List_Node] = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return str([x for x in self.__iter__()])

    def build(self, A: list) -> None:
        for item in reversed(A):
            self.insert_first(item)

    def get_at(self, i: int):
        assert self.head is not None
        return self.head.later_node(i).item

    def insert_first(self, item: Any) -> None:
        new_node = Linked_List_Node(item)  # create new node
        new_node.next = self.head  # assign new.next as head
        self.head = new_node  # now head becomes new node
        self.size += 1  # update size

    def delete_first(self) -> Optional[Linked_List_Node]:
        assert self.head
        old_node = self.head
        self.head = self.head.next
        self.size -= 1
        result = old_node.item
        old_node.next = None
        return result

    def insert_at(self, i: int, item) -> None:
        if i == 0:
            self.insert_first(item)
            return
        assert self.head
        new_node = Linked_List_Node(item)
        cur = self.head.later_node(i - 1)
        new_node.next = cur.next
        cur.next = new_node
        self.size += 1

    def delete_at(self, i) -> Optional[Linked_List_Node]:
        if i == 0:
            return self.delete_first()
        assert self.head
        cur = self.head.later_node(i - 1)
        if cur.next:
            next = cur.next
            cur.next = cur.next.next
            self.size -= 1
            next.next = None
            return next.item
        return None

    def insert_last(self, item) -> None:
        self.insert_at(len(self), item)

    def delete_last(self) -> Optional[Linked_List_Node]:
        return self.delete_at(len(self) - 1)


class Dynamic_Array_Sequence(Array_seq):
    def __init__(self, r=2):
        super().__init__()
        self.size = 0
        self.r = r #r=2 -> doubling
        self._compute_bounds()
        self._resize(0)

    def __len__(self): #O(1)
        return self.size

    def __iter__(self): #O(n)
        for i in range(len(self)):
            yield self.A[i]

    def __str__(self):
        return str([x for x in self.__iter__()])

    def build(self, X: list[Any]): #O(n)
        for a in X:
            self.insert_last(a)

    def _compute_bounds(self): #O(1)
        self.upper = len(self.A)
        self.lower = len(self.A) // (self.r * self.r)

    def _resize(self, n):
        if self.lower < n < self.upper:
            return
        m = max(n, 1) * self.r
        A = [None] * m
        self._copy_forward(0, self.size, A, 0)
        self.A = A
        self._compute_bounds()

    def insert_last(self, x):
        self._resize(self.size + 1)
        self.A[self.size] = x
        self.size += 1

    def delete_last(self):
        self.A[self.size - 1] = None
        self.size -= 1
        self._resize(self.size)

    def insert_at(self, i, x):
        self.insert_last(None)
        self._copy_backward(i, self.size - (i + 1), self.A, i)
        self.A[i] = x

    def delete_at(self, i):
        x = self.A[i]
        self._copy_forward(i + 1, self.size - (i + 1), self.A, i)
        self.delete_last()
        return x

    def insert_first(self, x):
        self.insert_at(0, x)

    def delete_first(self):
        return self.delete_at(0)
