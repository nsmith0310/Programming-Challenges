class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.que = []
        self.cap = k
        self.lim = 0
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.lim<self.cap:
            self.que.append(value)
            self.lim+=1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.lim>0:
            del self.que[0]
            self.lim-=1
            return True
        else:
            return False

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.lim>0:
            return self.que[0]
        else:
            return -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.lim>0:
            return self.que[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.lim==0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.lim==self.cap
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
