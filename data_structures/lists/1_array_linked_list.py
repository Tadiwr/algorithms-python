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
    
    def find(self, target: any) -> int:

        count = 1
        currentIndex = self.__startPointer

        while currentIndex != -1:
            currentNode = self.__arr[currentIndex]
            
            if currentNode.data == target:
                return count
            
            count += 1
            currentIndex = currentNode.next

        return -1
    
    def delete(self, target) -> bool:

        if self.__arr[self.__startPointer].data == target:
            self.__startPointer = self.__arr[self.__startPointer].next
            return True
        
        currentIndex = self.__startPointer
        prevIndex = currentIndex

        while currentIndex != -1:
            currentNode = self.__arr[currentIndex]

            if currentNode.data == target:
                self.__arr[prevIndex].next = currentNode.next 
                return True
            
            prevIndex = currentIndex
            currentIndex = currentNode.next

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


list1 = OneArrayLinkedList(10)

list1.insert("A")
list1.insert("B")
list1.insert("C")
list1.insert("D")
list1.insert("E")
list1.insert("X")

list1.delete("B")
list1.printList()

print("E's position: ", list1.find("X"))