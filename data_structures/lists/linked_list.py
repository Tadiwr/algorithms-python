class ListNode:
    def __init__(self, data :any = None) -> None:
        self.data : any = data
        self.next : ListNode = None

class LinkedList:

    def __init__(self) -> None:
        self.__head = ListNode()
        self.__last = self.__head
        

    def isEmpty(self) -> bool:
        return self.__head.next is None

    def insert(self, value: any):
        newNode = ListNode(value)

        self.__last.next = newNode
        self.__last = self.__last.next

    def insertInFront(self, value):
        newNode = ListNode(value)
        newNode.next = self.__head.next
        self.__head.next = newNode

    def find(self, target: any) -> int:
        count = 1
        curr = self.__head.next

        while curr is not None:
            if curr.data == target:
                return count
            curr = curr.next
            count += 1
        
        return -1
    
    def delete(self, target: any) -> bool:
        if not self.isEmpty():
            curr = self.__head.next
            prev = self.__head

            while curr is not None:
                if curr.data == target:
                    prev.next = curr.next
                    curr.next = None
                    return True
                
                prev = curr
                curr = curr.next
            
        return False
    
    def printList(self):

        if not self.isEmpty():
            curr = self.__head.next
            outStr = "Start ->"

            while curr is not None:
                outStr += f" {curr.data} ->"
                curr = curr.next

            print(outStr + " End")

        else:
            print("Linked List is Empty")

# letters = LinkedList()

# letters.insert("A")
# letters.insert("B")
# letters.insert("C")
# letters.insert("D")
# letters.insert("E")
# letters.delete("C")

# print(letters.find("B"))
# letters.printList()




