def BinarySearch(SearchFor, SearchFrom):
    up = 0                                      # Initialize the upper and lower limits
    down = len(SearchFrom) - 1
    while up <= down:                           # Create an exit condition in case element is not present
        mid = int((up + down)/2)                # Find the middle value of the list
        if SearchFrom[mid] == SearchFor:        # Compare and update the lower and upper limits appropriately
            return mid                          # Return the coordinate and exit as soon as the element is found
        elif SearchFrom[mid] > SearchFor:
            down = mid - 1
        elif SearchFrom[mid] < SearchFor:
            up = mid + 1
    return None                                 # If loop finishes, element was not found so return a null value

# Example Usage
myList = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"Value found at index : {BinarySearch(int(input("Enter the value to search : ")), myList)}")