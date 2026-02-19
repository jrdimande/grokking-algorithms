def binary_search(arr, target):
    """This function return the position of target using binary search"""
    # Low and high keep track of wich part of the list you'll search it
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2 # Check de middle element
        guess = arr[mid]

        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return None

my_list = [0, 1, 5, 8, 20]

print(binary_search(my_list, 20))

# Binary search will take at most 3 steps to return the position of the element