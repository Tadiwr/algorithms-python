from turtle import position


class TwoArrayLinkedList:
    
    def __init__(self, size: int) -> None:
        self.size: int = size
        self.__data = [None] * size
        self.__pointers = [-1] * size
        self.__startPointer = -1
        self.__freePointer = 0
        self.__lastPointer = self.__startPointer
        self.itemCount = 0


    def isEmpty(self) -> bool:
        return self.__startPointer == -1
    
    def isFull(self) -> bool:
        return self.__freePointer == self.size

    def insert(self, value: any) -> bool:

        if self.isFull():
            return False

        if self.isEmpty():
            self.__startPointer = self.__freePointer
        else:
            self.__pointers[self.__lastPointer] = self.__freePointer

        self.__data[self.__freePointer] = value
        self.__lastPointer = self.__freePointer
        self.__freePointer += 1

        return True
    
    def find(self, target: any) -> int:

        """ - Returns the position of the element with in the list
            - First Element in position 0
        """

        count = 0
        currentIndex = self.__startPointer

        while currentIndex != -1:
            currentData = self.__data[currentIndex]

            if currentData == target:
                return count
            else:
                currentIndex = self.__pointers[currentIndex]
                count += 1
            
        return -1
    
    def delete(self, target: any) -> bool:

        if self.isEmpty():
            return False
        
        currentIndex = self.__startPointer

        if self.__data[currentIndex] == target:
            self.__startPointer = self.__pointers[currentIndex]
            self.__pointers[currentIndex] = -1

            return True
        
        nextIndex = self.__pointers[currentIndex]

        # Get the current index which points to target
        while nextIndex != -1:

            nextData = self.__data[nextIndex]
            if nextData == target:
                break
            
            currentIndex = nextIndex
            nextIndex = self.__pointers[currentIndex]
        
        if nextIndex == -1: # Delete target was not found
            return False

        indexAfter = self.__pointers[nextIndex]
        self.__pointers[currentIndex] = indexAfter
        self.__pointers[nextIndex] = -1

        return True

    
    def printList(self):
        currentIndex  = self.__startPointer

        print(list.__data)
        print(list.__pointers)

        if currentIndex == -1:
            return "List is empty"
        else:

            outstr = "START ->"
            while currentIndex != -1:
                currentData = self.__data[currentIndex]
                outstr += f" {currentData} ->"

                currentIndex = self.__pointers[currentIndex]
    
            print(outstr + " END")

list = TwoArrayLinkedList(10)

list.insert("A")
list.insert("B")
list.insert("C")
list.insert("D")
list.insert("E")
list.insert("X")

list.delete("C")
list.insert("0")
list.printList()

print("E's position: ", list.find("E"))
