# goal => insert(logn), extraction(logn),sort(nlogn), inplace=true

#abstract base class for priority queue

class PriorityQueu:
    def __init__(self) -> None:
        self.A:list = []
    
    def insert(self,x):
        self.A.append(x)

    def delete_max(self):
        if len(self.A) < 1: #empty
            raise IndexError('pop from empty priority queue')
        return self.A.pop()

    @classmethod
    def sort(Queue,A):
        pq = Queue()
        for x in A:
            pq.insert(x)
        out = [pq.delete_max() for _ in A]
        out.reverse()
        return out


