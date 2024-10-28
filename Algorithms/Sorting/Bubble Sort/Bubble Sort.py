def BubbleSort(listToSort, listIsAlreadySorted):    # Use a recursive approach
    if listIsAlreadySorted:                         # The Exit Case
        return
    else:                                           # Run 1 bubble sort iteration
        flag = True                                 # The flag to determine when the recursion stops
        for i in range(len(listToSort) - 1):        # Systematically loop over each element excluding the last
            if listToSort[i] > listToSort[i+1]:     # Check and swap the current element with the next one if appropriate
                flag = False
                temp = listToSort[i]
                listToSort[i] = listToSort[i+1]
                listToSort[i+1] = temp
        BubbleSort(listToSort, flag)                # Call for the next iteration

# Example Usage
myList = [6, 39, 78, 27, 85, 4, 66, 92, 49]    # Test Data
print(myList)                                  # Print before sort
BubbleSort(myList, False)                      # Sort
print(myList)                                  # Print after sort