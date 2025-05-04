# THIS VERSION IS NOT A PART OF A LEVEL SYLLABUS
# THIS IS NOT A BST
# I MADE THIS BECAUSE I DID NOT KNOW THE SYLLABUS AT THE TIME


# IN THIS VERSION I HAVE FITTED ALL OF THE DATA INTO A SINGULAR ARRAY WITHOUT USING ANY NODES ETC.
# THIS IS ARRANGED IN A LINEAR HIERARCHY IN SUCH A WAY THAT LINEAR SEARCH BECOMES BFS, INVERTED LINEAR SEARCH BECOMES DFS
# THIS IS A BEAUTIFUL PIECE OF ABOMINATION WHICH I COULD NOT THROW AWAY, HENCE IT WILL STAY
# PLEASE LEAVE - YOU DO NOT WANT THIS



class BinaryTree:
    def __init__(self, levels, rootVal):
        self.levels = levels
        self.data = [None]*(pow(2, levels) - 1)
        self.data[0] = rootVal
    
    def offset(self, level, node):
        return (pow(2, level - 1) - 1) + node - 1
    
    def insert(self, level, node, Value):
        self.data[self.offset(level, node)] = Value
    
    def ValueAt(self, level, node):
        return self.data[self.offset(level, node)]

    def TraceNode(self, offset):
        node = 0
        level = 0
        while(offset - (pow(2, level) - 1) >= 0):
            level+= 1
        node = offset - (pow(2, level - 1) - 1) + 1
        location = [level, node]
        return location


    def PrintTree(self):
        for i in range(1, self.levels + 1):
            print("\t"*(pow(2, (self.levels - i)) - 1), end="")
            for i2 in range(int(pow(2, i-1))):
                print(self.ValueAt(i, i2 + 1), end="\t"*(pow(2, (self.levels - i + 1))))
            print()


myBT = BinaryTree(4, 50)
myBT.insert(2, 1, 51)
myBT.insert(2, 2, 52)
myBT.insert(3, 1, 53)
myBT.insert(3, 2, 54)
myBT.insert(3, 3, 55)
myBT.insert(3, 4, 56)
myBT.insert(4, 1, 57)
myBT.insert(4, 2, 58)
myBT.insert(4, 3, 59)
myBT.insert(4, 4, 60)
myBT.insert(4, 5, 61)
myBT.insert(4, 6, 62)
myBT.insert(4, 7, 63)
myBT.insert(4, 8, 64)

#print(myBT.ValueAt(4,5))

myBT.PrintTree()
print(myBT.data)