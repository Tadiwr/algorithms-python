class StackItem:

    def __init__(self, data: any = None) -> None:
        self.next : StackItem = None
        self.data = data

class ShangwaStack:

    def __init__(self) -> None:
        self.__dummy = StackItem()

    def isEmpty(self) -> bool:
        return self.__dummy.next is None

    def push(self, value: any) -> bool:

        newStackItem = StackItem(value)
        temp = self.__dummy.next
        newStackItem.next = temp
        self.__dummy.next = newStackItem

    def pop(self):
        
        poppedItem = self.__dummy.next
        self.__dummy.next = poppedItem.next
        poppedItem.next = None

        return poppedItem.data


# stack = ShangwaStack()

# stack.push("K")
# stack.push("C")
# stack.push("A")
# stack.push("T")
# stack.push("S")
# stack.push(" ")
# stack.push("A")

# outStr = ""

# while not stack.isEmpty():
#     outStr += stack.pop()

# print(outStr)