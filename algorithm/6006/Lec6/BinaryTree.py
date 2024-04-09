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


class Binary_Tree:
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
        A = X[:]  # copy

        def build_subtree(A, i, j):
            c = (i + j) // 2  # center index
            root = T.Node_Type(A[c])  # init root
            if i < c:
                root.left = build_subtree(A, i, c - 1)  # omit center
                root.left.parent = root
            if c < j:
                root.right = build_subtree(A, c + 1, j)  # omit center
                root.right.parent = root
            return root

        T.root = build_subtree(A, 0, len(A) - 1)


class BST_Node(Binary_Node):
    def subtree_find(A, k):
        if k < A.item.key:
            if A.left:
                return A.left.subtree_find(k)
        elif k > A.item.key:
            if A.right:
                return A.right.subtree_find(k)
        else:
            return A
        return None

    def subtree_find_next(A, k):  # O(h)
        if A.item.key <= k:  # if k is bigger than cur node -> go right
            if A.right:  # check if there is right
                return A.right.subtree_find_next(k)  # now traverse in sub tree
            else:  # if no right, there can't be no next. which means bigger than cur 'k'
                return None
        elif A.left:  # when the key is smaller than current node and check the left
            B = A.left.subtree_find_next(k)  # recurse in subtree
            if B:
                return B
        return A

    def subtree_find_prev(A, k):  # O(h). Equivalent pattern
        if A.item.key >= k:  # go to left
            if A.left:
                return A.left.subtree_find_prev(k)
            else:
                return None
        elif A.right:
            B = A.right.subtree_find_prev(k)
            if B:
                return B
        return A

    def subtree_insert(A, B):
        if B.item.key < A.item.key:  # to be inserted should be on the left
            if A.left:
                A.left.subtree_insert(B)
            else:
                A.subtree_insert_before(B)
        elif B.item.key > A.item.key:  # right is candidate
            if A.right:
                A.right.subtree_insert(B)
            else:
                A.subtree_insert_after(B)
        else:
            A.item = B.item


class Set_Binary_Tree(Binary_Tree):
    def __init__(self):
        super().__init__(BST_Node)

    # iter
    def iter_order(self):
        yield from self

    # build
    def build(self, X):
        for x in X:
            self.insert(x)

    # find min
    ## hint: where is the smallest item in tree
    def find_min(self):
        if self.root:
            return self.root.subtree_first().item

    # find max
    ## hint: where is the biggest item in tree
    def find_max(self):
        if self.root:
            return self.root.subtree_last().item

    # find
    ## see BST_Node API
    def find(self, x):
        if self.root:
            B = self.root.subtree_find(x)
            if B:
                return B.item

    # find next
    ## see BST_Node API
    def find_next(self,x):
        if self.root:
            B = self.root.subtree_find_next(x)
            if B:
                return B.item

    # find_prev
    ## see BST_Node API
    def find_prev(self,x):
        if self.root:
            B = self.root.subtree_find_prev(x)
            if B:
                return B.item

    # insert
    ## see BST_Node API
    def insert(self,x):
        new_node = self.Node_Type(x)
        if self.root:
            self.root.subtree(new_node)
            if new_node.parent is None:
                return False
        else:
            self.root = new_node
        self.size += 1
        return True

    # delete
    ## see BST_Node API
    def delete(self,x):
        assert self.root
        node = self.root.subtree_find(x)
        assert node
        ext = node.subtree_delete()
        if ext.parent is None:
            self.root = None
        self.size -= 1
        return ext.item



if __name__ == "__main__":
    A = [x for x in range(10)]
    tree = Binary_Tree()
    tree.build(A)
    print(f"{tree.root.item=}")
    for node in tree:
        print(node)
