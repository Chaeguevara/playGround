from Set_AVL_Tree import BST_Node 

class Measurement:
    def __init__(self, temp, date):
        self.key = date
        self.temp = temp

    def __str__(self):
        return "%s %s" % (self.key, self.temp)
