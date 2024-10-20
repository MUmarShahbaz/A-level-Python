def BinarySearch(SearchFor, SearchFrom):
    up = 0
    down = len(SearchFrom) - 1
    while up <= down:
        mid = int((up + down)/2)
        if SearchFrom[mid] == SearchFor:
            return mid
        elif SearchFrom[mid] > SearchFor:
            down = mid - 1
        elif SearchFrom[mid] < SearchFor:
            up = mid + 1

myList = [1, 2, 3, 4, 5, 6, 7, 8]
print(BinarySearch(7, myList))