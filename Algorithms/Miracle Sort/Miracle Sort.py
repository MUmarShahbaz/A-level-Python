import time

def CheckList(listToCheck):
    for i in range(len(listToCheck)):
        for i2 in range(i):
            if listToCheck[i] < listToCheck[i2]:
                return False
    return True

def MiracleSort(listToCheck):
    while(True):
        Sorted = CheckList(listToCheck)
        print(Sorted)
        if Sorted :
            break
        time.sleep(1)

myList = []

for i in range(int(input("Enter the number of elements in the list : "))):
    myList.append(int(input(f"Enter the item at index {i} : ")))

MiracleSort(myList)