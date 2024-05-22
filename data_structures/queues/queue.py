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

    def dequeue(self) -> any:

        dequeuedItem = self.__front.next
        self.__front.next = dequeuedItem.next
        dequeuedItem.next = None
        return dequeuedItem.data
    
    def printQueue(self):

        if self.isEmpty():
            print("The Queue is empty")
        else:
            curr = self.__front.next

            while curr is not None:
                print(curr.data)
                curr = curr.next