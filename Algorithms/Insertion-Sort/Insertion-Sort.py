def InsertionSort(listToSort):
    for i in range(len(listToSort)):                                    # Grab a value to compare
        for i2 in range(i):                                             # Compare against elements before the value being compared
            if listToSort[i] < listToSort[i2]:                          # Find the earliest element that is smaller than the value being compared
                temp = listToSort[i]                                    # Store the grabbed value in a buffer variable
                for i3 in range(i - i2):                                # Move all items between the value(excl.) location and the element(incl.)
                    listToSort[i - i3] = listToSort[i - i3 - 1]         # Move them one place to the right, one at a time
                listToSort[i2] = temp                                   # Import the buffer contents to the point of insertion
                break                                                   # Begin Sorting next element


myArray = [8, 7, 6, 5, 4, 3, 2, 1]  # Test Data
print(myArray)                      # Print before sort
InsertionSort(myArray)              # Sort
print(myArray)                      # Print after sort