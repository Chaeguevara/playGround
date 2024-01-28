from typing import Optional


class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.E:Optional[Node] = None
        self.W:Optional[Node] = None
        self.S:Optional[Node] = None
        self.N:Optional[Node] = None

class LinkedList:
    def __init__(self, length:int, width:int) -> None:
        self.head = None
        self.tail = None
        self.length = length
        self.count = 0
        self.width = width
        self.cur_row = 0

    def build(self) -> None:
        self.build_helper()

    def build_helper(self,
                     runner: Optional[Node] = None, 
                     anchor: Optional[Node] = None, 
                     follower:Optional[Node] = None)-> None:

        if self.cur_row > 0:
            self.connect_runner_follower(runner,follower)
        # base case
        if self.count >= self.length:
            self.tail = runner
            print("end")
            return

        new_node = Node(self.count)
        # caset 1 : first node 
        if self.count == 0:
            print(f"At first node {self.count=}")
            self.head = new_node
            anchor = new_node
        # case 2 : go down
        elif self.count % self.width == 0:
            print(f"Go down at {self.count=}")
            anchor.S = new_node
            new_node.N = anchor
            follower = anchor
            anchor = new_node
            self.cur_row += 1
        # case 3 : go right
        else:
            print(f"Go right at {self.count=}")
            new_node.W = runner
            runner.E = new_node
            if follower:
                follower = follower.E

        # initialize follower
        # if self.count == self.width:
        #     print("initialize follower")
        #     follower = runner


        runner = new_node

        self.count += 1
        self.build_helper(runner,anchor,follower)


        return
        

    def connect_runner_follower(self, runner:Optional[Node], follower:Optional[Node]) -> None:
        if follower and runner:
            runner.N = follower
            follower.S = runner
        return None


    def iter(self):
        cur = self.head
        count = 1
        while cur:
            print(cur.val)
            #go down
            if count == 1:
                cur = cur.E
            elif count % self.width == 0:
                print("down")
                cur = cur.S
            # go right
            elif int(count / self.width) %2 == 0:
                cur = cur.E
            elif int(count / self.width) %2 == 1:
                cur = cur.W
            count += 1



test = LinkedList(25,5)
test.build()
test.iter()
# print(test.head.val)
