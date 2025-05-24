class Node:
    def __init__(self, Val, Ptr):
        self.Data = Val
        self.Pointer = Ptr
    
class LinkedList:
    def __init__(self, length):                     # Constructor
        self.items = [None] * length                # Container
        for i in range(length):
            self.items[i] = Node(-1, i+1)           # Fill container with nodes, each pointing to the next
        self.start = None                           # Start Pointer
        self.free = 0                               # Free Pointer
        self.nodes = 0                              # Number of nodes filled
    
    def InsertNode(self, value):
        if self.nodes == len(self.items):           # Check for space
            print("List is full")
            return                                  # Exit if no space
        
        new = self.free                             # Store index of where the new node will be placed
        self.free = self.items[self.free].Pointer   # Move Free Pointer to the next free node
        self.items[new] = Node(value, None)         # Place the new node

        if self.start == None:                      # Special Case for Root Node
            self.start = new                        # Start points to new node index
            self.nodes = self.nodes + 1             # Increase number of nodes filled
            return
        
        currentNode = self.items[self.start]
        while True:
            if currentNode.Pointer == None:         # If pointer is empty
                currentNode.Pointer = new           # Point to new
                self.nodes = self.nodes + 1         # Increase number of nodes filled
                break                               # Exit Loop

            currentNode = self.items[currentNode.Pointer]   # Go to the next node
    
    def PrintList(self):
        currentNode = self.items[self.start]        # Start at Root
        while True:
            print(currentNode.Data)                 # Print value
            if currentNode.Pointer == None:         # Exit loop if doesn't point to anything
                break
            currentNode = self.items[currentNode.Pointer]   # Go to next node
    
    def DeleteNode(self, index):
        if index == self.start:                             # Special Case for deleting Root Node
            self.start = self.items[self.start].Pointer     # Start pointer points to next node
            self.items[index] = Node(-1, self.free)         # Place empty node but point to current free pointer
            self.free = index                               # Free pointer points to new empty node
            return

        currentNode = self.items[self.start]                # Start at root
        while True:
            if currentNode.Pointer == index:                # Loop until you find the node that points to the delete node
                break
        currentNode.Pointer = self.items[index].Pointer     # Pointer of previous points to the one after
        self.items[index] = Node(-1, self.free)             # Place empty node but point to current free pointer
        self.free = index                                   # Free pointer points to new empty node
    
    def SearchFor(self, value):
        currentNode = self.items[self.start]                # Start at root
        if currentNode.Data == value:                       # Check if value is at root
            return self.start
        while True:
            nextNode = self.items[currentNode.Pointer]      # Get next Node
            if nextNode.Data == value:                      # if the next is the node we need
                return currentNode.Pointer                  # return the currentNode's pointer, which is index of the node we need
            if nextNode.Data == -1:                         # if next is last node
                return -1                                   # Return null
            currentNode = nextNode                          # Go to next Node

ll = LinkedList(12)
vals = [3, 5, 2, 4, 1, 6, 0]
print(vals)

for i in vals:
    ll.InsertNode(i)

ll.PrintList()