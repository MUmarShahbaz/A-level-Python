class Stack:
    def __init__(self, Size):
        self.size = Size
        self.items = []
        for i in range(Size):
            self.items.append(None)
        self.endPointer = -1

    def stackIsFull(self):
        if (self.endPointer < self.size):
            return False
        else :
            return True
    
    def stackIsEmpty(self):
        if (self.endPointer > -1):
            return False
        else :
            return True
    
    def push(self, Value):
        if (not self.stackIsFull()) :
            self.endPointer += 1
            self.items[self.endPointer] = Value
            
    def pop(self):
        if (not self.stackIsEmpty()):
            self.items[self.endPointer] = None
            self.endPointer -= 1
    
    def printItems(self):
        for i in range(self.size - 1, -1, -1):
            if self.items[i] != None :
                print(f"\t{self.items[i]}")
            else:
                print("\t.")


# Example Usage
Books = Stack(5)

print("Stack before anything is added to it")
Books.printItems()

print("\nStack after adding 3 elements")
Books.push("Language and the rise of the Algorithm")
Books.push("In Search of Schrödinger's Cat")
Books.push("Designing Embedded Systems")
Books.printItems()

print("\nStack after removing 2 elements from the new Stack")
Books.pop()
Books.pop()
Books.printItems()

print("\nStack after adding a new element")
Books.push("The Essence of Software")
Books.printItems()