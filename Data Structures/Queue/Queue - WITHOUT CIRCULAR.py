class Queue:
    def __init__(self, Size):                                               # Initializer Function
        self.size = Size                                                    # initializes a list of specific size and a pointer
        self.items = []
        for i in range(Size):
            self.items.append(None)
        self.endPointer = -1

    def queueIsFull(self):                                                  # Function to check whether the queue is full or not
        if (self.endPointer < self.size - 1):
            return False
        else :
            return True
    
    def queueIsEmpty(self):                                                 # Function to check whether the queue is empty or not
        if (self.endPointer > -1):
            return False
        else :
            return True
    
    def push(self, Value):                                                  # Push Function
        if (not self.queueIsFull()) :                                       # Pushes an item at the end of the queue
            self.endPointer += 1
            self.items[self.endPointer] = Value
        else :
            print(f"\n-> Queue is full, can't push {Value}. Max limit is {self.size}")
            
    def pop(self):                                                          # Pop Function
        if (not self.queueIsEmpty()):                                       # Pops the very first item in the queue
            for i in range(self.endPointer):                                # and shifts the rest items one step forward
                self.items[i] = self.items[i+1]
            self.items[self.endPointer] = None
            self.endPointer -= 1
        else :
            print("\n-> Queue is Empty, there is no element to pop")
    
    def printItems(self):                                                                           # Prints info regarding the Queue
        print(f"\n-> Queue Length : {self.size}, Items present : {self.endPointer + 1}, Queue:")
        for i in range(self.size):
            if self.items[i] != None :
                print(f"\t{self.items[i]}")
            else:
                print("\t.")

# Example Usage

Clients = Queue(5)

print("\n\n\n\nQueue (length 5) before anything is added to it")
Clients.printItems()
print("\nTry to pop an item")
Clients.pop()

print("\nQueue after adding 6 elements")
Clients.push("Umar")
Clients.push("Schrödinger")
Clients.push("Ahmad")
Clients.push("Umar")
Clients.push("Schrödinger")
Clients.push("Ahmad")
Clients.printItems()

print("\nQueue after removing 6 elements from the new Queue")
Clients.pop()
Clients.pop()
Clients.pop()
Clients.pop()
Clients.pop()
Clients.pop()
Clients.printItems()

print("\nQueue after adding a new element")
Clients.push("Schrödinger's Cat")
Clients.printItems()
print("\n\n\n\n")