

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
            A.item, B.item = B.item, A.item
            return B.delete()
        if A.parent:
            if A.parent.left is A:
                A.parent.left = None
                A.parent = None
            else:
                A.parent.right = None
                A.parent = None
        return A


class Binary_tree:
    def __init__(T, Node_Type=Binary_Node):
        T.root = None
        T.size = 0
        T.Node_Type = Node_Type

    def __len__(T):
        return T.size

    def __iter__(T):
        if T.root:
            for A in T.root.subtree_iter():
                yield A.item

    def build(T, X):
        A = X[:] #copy

        def build_subtree(A, i, j):
            c = (i + j) // 2 #center index
            root = T.Node_Type(A[c]) #init root
            if i < c:
                root.left = build_subtree(A, i, c - 1) #omit center
                root.left.parent = root
            if c < j:
                root.right = build_subtree(A, c + 1, j) #omit center
                root.right.parent = root
            return root

        T.root = build_subtree(A, 0, len(A) - 1)

A = [ x for x in range(10)]
tree = Binary_tree()
tree.build(A)
print(f"{tree.root.item=}")
for node in tree:
    print(node)