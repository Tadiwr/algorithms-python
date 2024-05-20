class LinkedListNode:

    def __init__(self, data = None) -> None:
        self.data = data
        self.next = -1

class OneArrayLinkedList:

    def __init__(self, size: int) -> None:
        self.__arr : list[LinkedListNode] = [None] * size
        self.size = size
        self.__startPointer = -1
        self.__freePointer = 0
        self.__lastPointer = self.__startPointer

    def isFull(self) -> bool:
        return self.__freePointer == self.size

    def isEmpty(self) -> bool:
        return self.__startPointer == -1

    def insert(self, value) -> bool:

        if not self.isFull():
            newNode = LinkedListNode(value)
            self.__arr[self.__freePointer] = newNode

            if self.isEmpty():
                self.__startPointer = self.__freePointer
            else:
                self.__arr[self.__lastPointer].next = self.__freePointer

            self.__lastPointer = self.__freePointer
            self.__freePointer += 1

            return True

        return False
            
    def printList(self):

        currentIndex = self.__startPointer

        if currentIndex == -1:
            print("Linked List is empty")
        else:
            outStr = "Start ->"

            while currentIndex != -1:
                currentNode = self.__arr[currentIndex]
                outStr += f" {currentNode.data} ->"
                currentIndex = currentNode.next

            print(outStr + " End")


list = OneArrayLinkedList(10)

list.insert("A")
list.insert("B")
list.insert("C")
list.insert("D")
list.insert("E")
list.insert("X")

# list.delete("C")
list.printList()

# print("E's position: ", list.find("E"))