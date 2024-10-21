class Stack:
    def __init__(self, Size):                                                               # Initializer function
        self.size = Size                                                                    # Initializes the list and pointer to contain the stack items
        self.items = []
        for i in range(Size):
            self.items.append(None)
        self.endPointer = -1

    def stackIsFull(self):                                                                  # Function to check whether the stack is full
        if (self.endPointer < self.size):
            return False
        else :
            return True
    
    def stackIsEmpty(self):                                                                 # Function to check whether the stack is empty
        if (self.endPointer > -1):
            return False
        else :
            return True
    
    def push(self, Value):                                                                  # Push Function
        if (not self.stackIsFull()) :                                                       # Pushes an item to the top of the stack
            self.endPointer += 1
            self.items[self.endPointer] = Value
        else :
            print(f"\n-> Stack is full, can't push {Value}. Max limit is {self.size}")
            
    def pop(self):                                                                          # Pop Function
        if (not self.stackIsEmpty()):                                                       # Removes the topmost item
            self.items[self.endPointer] = None
            self.endPointer -= 1
        else :
            print("\n-> Stack is Empty, there is no element to pop")
    
    def printItems(self):                                                                           # Print Function
        print(f"\n-> Stack Length : {self.size}, Items present : {self.endPointer + 1}, Stack:")    # Prints info regarding the stack
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