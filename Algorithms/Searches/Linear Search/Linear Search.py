def LinearSearch(listToSearchFrom, valueToSearch):
    for i in range(len(listToSearchFrom)):
        if listToSearchFrom[i] == valueToSearch:
            return i
    return None
        
# Example Usage
myList = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"Value found at index : {LinearSearch(myList, int(input("Enter the value to search : ")))}")