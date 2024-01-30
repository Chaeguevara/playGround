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
        self._forward_copy(new_arr, i, i + 1, self.size - i)
        self.A = new_arr
        return x

    def insert_first(self, x: Any) -> None:
        self.insert_at(0, x)

    def insert_last(self, x: Any) -> None:
        self.insert_at(self.size, x)

    def delete_first(self) -> Any:
        return self.delete_at(0)

    def delete_last(self) -> Any:
        x = self.delete_at(self.size - 1)
        return x


class Linked_List_Node:
    def __init__(self, x) -> None:
        self.x: Any = x
        self.next: Linked_List_Node | None = None

    def later_node(self, i: int):
        if i == 0:
            return self
        assert self.next
        return self.next.later_node(i - 1)


class Array_Stack(Static_Array):
    def __init__(self):
        super().__init__()
        self.head = None

    def push(self, x): #O(n) for static array(extend memory), O_a(1) for dynamic array
        self.insert_last(x)
        self.head = self.A[-1]

    def pop(self): #O(n) for static array (shirink memory), O_a(1) for dynamic arr
        if self.size > 0: 
            return self.delete_last()
        else:
            return None

    def isEmpty(self): #O(1)
        return True if self.size <= 0 else False

    def top(self): # O(1)
        return self.A[-1]


class LL_Stack:
    def __init__(self) -> None:
        self.head: Linked_List_Node | None = None
        self.size = 0
        pass

    def push(self, x: Any): #O(1)
        x = Linked_List_Node(x)
        self.size += 1
        if self.head is None:
            self.head = x
        else:
            x.next = self.head
            self.head = x

    def pop(self) -> Linked_List_Node | None: #O(1)
        if self.head:
            self.size -= 1
            x = self.head
            self.head = self.head.next
            x.next = None
            return x
        else:
            return None

    def isEmpty(self) -> bool: #O(1)
        return True if self.head is None else False

    def top(self) -> Linked_List_Node | None: #O(1)
        x = Linked_List_Node(self.head.x) if self.head else None
        return x

    def __str__(self) -> str:
        a = []
        cur = self.head
        while cur:
            a.append(cur.x)
            cur = cur.next
        return str(a)


class Array_Queue(Static_Array):
    def __init__(self) -> None:
        super().__init__()
        self.head = None
        self.tail = None

    def add(self, x) -> None: #O(n) for static, O_a(1) for dynamic
        self.insert_last(x)
        self.tail = x
        self.head = self.A[0]

    def popFirst(self): #O(n) for static, O_a(1) for dynamic
        x = self.delete_first()
        if self.size > 0:
            self.head = self.A[0]
            self.tail = self.A[-1]
        return x

    def popLast(self): #O(n) for static(memory shirink), O_a(1) for dynamic
        x = self.delete_last()
        if self.size > 0:
            self.head = self.A[0]
            self.tail = self.A[-1]
        return x

    def first(self): #O(1)
        return self.head

    def last(self): #O(1)
        return self.tail

    def isEmpty(self): #O(1)
        return True if self.size < 1 else False


class LL_Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __str__(self) -> str:
        a:list[Linked_List_Node] = []
        cur = self.head
        while cur:
            a.append(cur.x)
            cur = cur.next
        return str(a)

    def _find_prev_of_last(self) -> None | Linked_List_Node: #lower_bound(n)
        cur = self.head
        if cur is None or cur.next is None:
            return cur
        prev = None
        while cur.next:
            prev = cur
            cur = cur.next
        return prev

    def add(self, x: Any): #O(1)
        x = Linked_List_Node(x)
        if self.head is None or self.tail is None:
            self.head = x
            self.tail = x
            return
        self.tail.next = x
        self.tail = x

    def popFirst(self) -> None | Linked_List_Node: #O(1)
        if self.head is None:
            return None
        cur = self.head
        self.head = cur.next
        cur.next = None
        return cur

    def popLast(self) -> None | Linked_List_Node: #lower_bound(n) for Singly LL
        if self.tail is None:
            return None
        prev_tail = self._find_prev_of_last()
        if prev_tail is None:
            raise ValueError
        cur = self.tail
        self.tail = prev_tail
        prev_tail.next = None
        return cur

    def first(self) -> None | Linked_List_Node: #O(1)
        if self.head is None:
            return None
        cur = Linked_List_Node(self.head.x)
        return cur

    def last(self) -> None | Linked_List_Node: #O(1)
        if self.tail is None:
            return None
        cur = Linked_List_Node(self.tail.x)
        return cur

    def isEmpty(self) -> bool: #O(1)
        if self.head is None or self.tail is None:
            return True
        else:
            return False


print("Static_Array")
s_arr = Static_Array()
s_arr.build([1, 2, 3, 4, 5])
s_arr.insert_last(6)
print(s_arr)
print("s_arr.insert_at(1, 0)")
s_arr.insert_at(1, 0)
print(s_arr)
print(f"{s_arr.delete_at(0)=}")
print(s_arr)
print(f"{s_arr.delete_last()=}")
print(s_arr)
print()

print("Array_Stack")
arr_stack = Array_Stack()
arr_stack.build([1, 2, 3, 4, 5])
print(arr_stack)
print("arr.stack.push(6)")
print(arr_stack)
print(f"{arr_stack.pop()=}")
print(arr_stack)
print(f"{arr_stack.top()=}")
print(f"{arr_stack.isEmpty()=}")
print()

print("LL Stack")
ll_stack = LL_Stack()
print(f"{ll_stack.isEmpty()=}")
for i in range(5):
    ll_stack.push(i)
print(ll_stack)
print(f"{ll_stack.pop().x=}")
print(ll_stack)
print()

print("Array Queue")
arr_queue = Array_Queue()
arr_queue.add(1)
print(arr_queue)
arr_queue.add(2)
print(arr_queue)
arr_queue.add(3)
print(arr_queue)
arr_queue.add(4)
print(arr_queue)
print(f"{arr_queue.popFirst()=}")
print(f"{arr_queue.popLast()=}")
print(arr_queue)

print("LL Queue")
ll_queue = LL_Queue()
print(ll_queue)
ll_queue.add(1)
ll_queue.add(2)
ll_queue.add(3)
print(ll_queue)
print(f"{ll_queue.tail.x=}")
print(f"{ll_queue.popLast().x=}")
print(ll_queue)
print(f"{ll_queue.popFirst().x=}")
print(ll_queue)
print(f"{ll_queue.popFirst().x=}")
print(ll_queue)
