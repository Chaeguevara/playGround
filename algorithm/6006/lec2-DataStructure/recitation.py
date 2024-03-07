class Array_sequ:
    def __init__(self)->None:
        self.A = []
        self.size = 0
    def __len__(self)->int:
        return self.size
    def __iter__(self):
        yield from self.A