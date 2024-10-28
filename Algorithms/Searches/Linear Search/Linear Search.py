def LinearSearch(listToSearchFrom, valueToSearch):
    for i in range(len(listToSearchFrom)):              # Check every element
        if listToSearchFrom[i] == valueToSearch:
            return i                                    # Return the coordinate as soon as the element is found
    return None                                         # If the loop finishes (no returns previously made) return a null value as the element was not found
        
# Example Usage
myList = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"Value found at index : {LinearSearch(myList, int(input("Enter the value to search : ")))}")