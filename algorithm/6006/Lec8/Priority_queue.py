# goal => insert(logn), extraction(logn),sort(nlogn), inplace=true

# abstract base class for priority queue


class PriorityQueue:
    def __init__(self) -> None:
        self.A: list = []

    def insert(self, x):
        self.A.append(x)

    def delete_max(self):
        if len(self.A) < 1:  # empty
            raise IndexError("pop from empty priority queue")
        return self.A.pop()

    @classmethod
    def sort(Queue, A):
        pq = Queue()
        for x in A:
            pq.insert(x)
        out = [pq.delete_max() for _ in A]
        out.reverse()
        return out


class PQ_Array(PriorityQueue):
    def elete_max(self):
        n, A, m = len(self.A), self.A, 0
        for i in range(1, n):
            if A[m].ke < A[i].key:
                m = i
        A[m], A[n] = A[n], A[m]
        return super().delete_max()


class PQ_SortedArray(PriorityQueue):
    def insert(self, *args):
        super().insert(*args)
        i, A = len(self.A) - 1, self.A
        while 0 < i and A[i + 1].key < A[i].key:
            A[i + 1], A[i] = A[i], A[i + 1]
            i -= 1


# Binary Heaps


def parent(i):
    p = (i - 1) // 2
    return p if 0 < i else i


def left(i, n):
    left = 2 * i + 1
    return left if left < n else i


def right(i, n):
    r = 2 * i + 2
    return r if r < n else i

def max_heapify_up(A,n,c):
    p = parent(c)
    if A[p].key < A[c].key:
        A[c], A[p] = A[p], A[c]
        max_heapify_up(A,n,p)

def max_heapify_down(A,n,p):
    l,r = left(p,n),right(p,n)  # noqa: E741
    c = l if A[r].key < A[l].key else r
    if A[p].key < A[c].key:
        A[c] ,A[p] = A[p], A[c]
        max_heapify_down(A,n,c)

def build_max_heap(A):
    n = len(A)
    for i in range(n//2,-1,-1):
        max_heapify_down(A,n,i)
class PQ_Heap(PriorityQueue):
    def insert(self, *args):
        super().insert(*args)
        n, A = self.n, self.A
        max_heapify_up(A, n, n - 1)

    def delete_max(self):
        n, A = self.n, self.A
        A[0], A[n] = A[n], A[0]
        max_heapify_down(A, n, 0)
        return super().delete_max()
