class CircularQueue:

    def __init__(self, size: int) -> None:
        self.__front = -1
        self.__rear = 0 # Points to the next free space
        self.__arr = [None] * size
        self.maxSize = size

    def isFull(self) -> bool:
        return self.__rear == self.__front
    
    def isEmpty(self) -> bool:
        return self.__front == -1
    
    def enqueue(self, value) -> bool:

        if not self.isFull():
            self.__arr[self.__rear] = value

            if self.isEmpty():
                self.__front = self.__rear
            
            self.__rear += 1

            if self.__rear == self.maxSize:
                self.__rear = 0
            
            return True

        return False
    
    def dequeue(self) -> any:

        if not self.isEmpty():

            temp = self.__arr[self.__front]
            self.__arr[self.__front] = None

            if self.__front == self.maxSize - 1:
                self.__front = 0
            else:
                self.__front += 1

            return temp

        return None
    
    def printQueue(self):
        print(self.__arr)
    
q = CircularQueue(5)

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.enqueue("D")
q.enqueue("E")

q.dequeue()
q.dequeue()
q.enqueue("X")
q.dequeue()

q.printQueue()