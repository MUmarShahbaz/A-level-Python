class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, length):
        self.items = [Node(None)] * length
        self.numberOfNodes = 0

    def InsertNode(self, Node):
        if self.numberOfNodes == len(self.items):
            print(f"All {len(self.items)} nodes are full and contain data")
            return False
        else:
            if self.numberOfNodes == 0:
                print("Creating the first node")
            else:
                currentNodeIndex = 0
                lastNodeIndex = 0
                while currentNodeIndex != None:
                    lastNodeIndex = currentNodeIndex
                    if Node.value <= self.items[currentNodeIndex].value:
                        currentNodeIndex = self.items[currentNodeIndex].left
                    else:
                        currentNodeIndex = self.items[currentNodeIndex].right
                if Node.value <= self.items[lastNodeIndex].value:
                    self.items[lastNodeIndex].left = self.numberOfNodes
                else:
                    self.items[lastNodeIndex].right = self.numberOfNodes
            self.items[self.numberOfNodes] = Node
            self.numberOfNodes = self.numberOfNodes + 1
            return True
    
    def PrintTreeByValues(self):
        for i in range(len(self.items)):
            if self.items[i].left == None:
                leftVal = None
            else:
                leftVal = self.items[self.items[i].left].value
            if self.items[i].right == None:
                rightVal = None
            else:
                rightVal = self.items[self.items[i].right].value
            print(f"[{i}]:\t {leftVal}\t<==\t {self.items[i].value} \t==>\t{rightVal}")
    
    def PrintTreeByMemory(self):
        count = 0
        for i in self.items:
            print(f"[{count}]:\t{i.left}\t<== {i.value} ==>\t{i.right}")
            count = count + 1


myTree = BinaryTree(10)

myTree.InsertNode(Node(4))
myTree.InsertNode(Node(3))
myTree.InsertNode(Node(2))
myTree.InsertNode(Node(1))
myTree.InsertNode(Node(5))
myTree.InsertNode(Node(6))
myTree.InsertNode(Node(7))

myTree.PrintTreeByValues()
print("\n"*5)
myTree.PrintTreeByMemory()