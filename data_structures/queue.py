class QueueItem:

    def __init__(self, data: any = None) -> None:
        self.data = data
        self.next : QueueItem = None

class ShangwaQueue:

    def __init__(self) -> None:
        self.__front = QueueItem()
        self.__rear =  self.__front

    def isEmpty(self):
        return self.__front.next is None

    def enqueue(self, value: any):
        newItem = QueueItem(value)
        self.__rear.next = newItem
        self.__rear = self.__rear.next

    # def dequeue(self):
