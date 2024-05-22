class ArrQueue:

    def __init__(self, size: int) -> None:
        self.__front = -1
        self.__rear = 0
        self.__arr = [None] * size
        self.maxSize = size

    def isEmpty(self) -> bool:
        return self.__front == -1
    
    def isFull(self) -> bool:
        return self.__rear == self.maxSize

    def enqueue(self, value: any):

        if self.isFull():
            print(f"Can't enqueue {value}, Queue is full")
        else:
            self.__arr[self.__rear] = value

            # If this was the first element make the front pointer point to it

            if self.isEmpty(): 
                self.__front = self.__rear

            self.__rear += 1

    def dequeue(self) -> any:

        if self.isEmpty():
            print("Queue is empty, can't dequeue")
            return None
        else:
            temp = self.__arr[self.__front]
            self.__front += 1

            return temp
        
    def printQueue(self):
        curr = self.__front

        if self.isEmpty():
            print("Empty Queue")
            return
        
        while curr != self.__rear:

            print(self.__arr[curr])
            curr += 1



q = ArrQueue(6)

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.enqueue("D")
q.enqueue("E")

q.dequeue()
q.dequeue()
q.printQueue()