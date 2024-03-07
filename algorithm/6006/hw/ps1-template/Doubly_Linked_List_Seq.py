

class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        node = Doubly_Linked_List_Node(x)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node



    def insert_last(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        node = Doubly_Linked_List_Node(x)
        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def delete_first(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        ###########################
        if self.head is not None:
            x = self.head.item
            #case 1 -only one item
            if self.head is self.tail:
                self.head = None
                self.tail = None
            else:
                cur = self.head
                self.head = self.head.next
                self.head.prev = None
                cur = None
        return x

    def delete_last(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        ###########################
        if self.tail is not None:
            x = self.tail.item
            # case1 one item
            if self.head is self.tail:
                self.head = None
                self.tail = None
            else: # general case : more than one
                cur = self.tail
                self.tail = self.tail.prev
                self.tail.next = None
                cur = None
        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        ###########################
        # Part (b): Implement me! # 
        ###########################
        # delete -> assign to L2 -> x1.prev.next = x2.next
        # base case x1 or x2 is none
        # case 1 : x1 is head -> self.head -> x2.next
        L2.head = x1
        L2.tail = x2
        if x1 is self.head:
            self.head = x2.next
        else:
            x1.prev.next = x2.next
        if x2 is self.tail:
            self.tail = x1.prev
        else:
            x2.next.prev = x1.prev
        L2.head.prev = None
        L2.tail.next = None


        return L2

    def splice(self, x, L2):
        ###########################
        # Part (c): Implement me! # 
        ###########################
        x.next.prev = L2.tail
        L2.tail.next = x.next
        x.next = L2.head
        L2.head.prev = x
        L2.head = None
        L2.tail = None

