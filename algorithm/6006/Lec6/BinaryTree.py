from networkx import null_graph


class Binary_Node:
    def __init__(A, x):
        A.item = x
        A.left: Binary_Node | None = None
        A.right: Binary_Node | None = None
        A.parent: Binary_Node | None = None

    def subtree_iter(A):
        # left -> self -> riggt 순서로 탐색을 진행함 O(n). 왜냐하면 모든 아이템을 탐색하게 됨
        if A.left:
            yield from A.left.subtree_iter()
        yield A
        if A.right:
            yield from A.right.subtree_iter()

    def subtree_first(A):
        if A.left:
            return A.left.subtree_first()
        else:
            return A

    def subtree_last(A):
        if A.right:
            return A.right.subtree_last()
        else:
            return A

    def sucessor(A):
        if A.right:
            return A.right.subtree_first()
        while A.parent and (A.parent.right is A):
            A = A.parent
        return A.parent

    def predecessor(A):
        if A.left:
            return A.left.subtree_last()
        while A.parent and (A.parent.left is A):
            A = A.parent
        return A.parent

    def subtree_insert_before(A, B):
        if A.left:
            A = A.left.subtree_last()
            A.right, B.parent = B, A
        else:
            A.left, B.parent = B, A

    def subtree_insert_after(A, B):
        if A.right:
            A = A.right.subtree_first()
            A.left, B.parent = B, A
        else:
            A.right, B.parent = B, A

    def delete(A):
        if A.left or A.right:
            if A.left:
                B = A.predecessor()
            else:
                B = A.sucessor()
            A.item, B.item = B.item ,A.item
            return B.delete()
        if A.parent:
            if A.parent.left is A:
                A.parent.left = None
                A.parent = None
            else:
                A.parent.right = None
                A.parent =None
        return A




A = [Binary_Node(i) for i in range(10)]

right_node = None
for i in range(5, len(A) - 2):
    if right_node is None:
        right_node = A[i]
    cur = A[i]
    cur.right = A[i + 1]

left_node = None
for i in range(3, 0, -1):
    if left_node is None:
        left_node = A[i]
    cur = A[i]
    cur.left = A[i - 1]


center = A[4]
center.left = left_node
center.right = right_node


test = center.subtree_iter()
for item in test:
    print(item.item)

print(center.right.subtree_last().item)
