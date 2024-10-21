def BubbleSort(listToSort, listIsAlreadySorted):
    if listIsAlreadySorted:
        return
    else:
        flag = True
        for i in range(len(listToSort) - 1):
            if listToSort[i] > listToSort[i+1]:
                flag = False
                temp = listToSort[i]
                listToSort[i] = listToSort[i+1]
                listToSort[i+1] = temp
        BubbleSort(listToSort, flag)

# Example Usage
myList = [6, 39, 78, 27, 85, 4, 66, 92, 49]    # Test Data
print(myList)                                  # Print before sort
BubbleSort(myList, False)                      # Sort
print(myList)                                  # Print after sort