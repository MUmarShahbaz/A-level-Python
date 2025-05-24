class Node:
    def __init__(self, val):
        self.Data = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, length):                 # Constructor
        self.items = [Node(None)] * length      # Container
        self.start = None                       # Root Pointer
        self.free = 0                           # Free Pointer
    
    def InsertNode(self, Val):
        if self.free == len(self.items):
            print("Binary Tree is already full")
            return
        
        self.items[self.free] = Node(Val)       # Place node at free pointer
        if self.start == None:                  # Special Case for Root Node
            self.start = self.free              # Root Pointer points to recently filled value
            self.free = self.free + 1           # Free Pointer points to next free
            return                              # Exit function after setting up Root
        

        currentNode = self.items[self.start]                    # Start at Root
        while True:                                             # Loop will be broken from inside

            if Val < currentNode.Data:
                if currentNode.left == None:                    # If Left pointer already empty
                    currentNode.left = self.free                # Left pointer points to recently filled value
                    break                                       # Exit loop after insertion

                else:
                    currentNode = self.items[currentNode.left]  # Go to node at Left pointer

            if Val > currentNode.Data:
                if currentNode.right == None:                   # If Right pointer already empty
                    currentNode.right = self.free               # Right pointer points to recently filled value
                    break                                       # Exit loop after insertion
                
                else:
                    currentNode = self.items[currentNode.right] # Go to node at Right pointer
        self.free = self.free + 1               # Free Pointer points to next free

    def PrintTreeByValues(self):
        for i in range(len(self.items)):
            if self.items[i].left == None:
                leftVal = None
            else:
                leftVal = self.items[self.items[i].left].Data
            if self.items[i].right == None:
                rightVal = None
            else:
                rightVal = self.items[self.items[i].right].Data
            print(f"[{i}]:\t {leftVal}\t<==\t {self.items[i].Data} \t==>\t{rightVal}")
    
    def Traverse(self, Node):
        if Node == None:
            Node = self.items[self.start]                   # Traverse relative to the ROOT
        if Node.left != None:
            self.Traverse(self.items[Node.left])            # Traverse relative to the left of the current node
        if Node.right != None:
            self.Traverse(self.items[Node.right])           # Traverse relative to the right of the current node
        print(Node.Data)


# Test
bt = BinaryTree(7)

bt.InsertNode(4)
bt.InsertNode(6)
bt.InsertNode(3)
bt.InsertNode(1)
bt.InsertNode(8)
bt.InsertNode(2)
bt.InsertNode(7)
bt.InsertNode(5)        # Adding 8th Node, expect full message

bt.PrintTreeByValues()
bt.Traverse(None)