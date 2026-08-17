# Binary Search Implementation
def binary_search(list_of_numbers, item):
    low = 0
    high = len(list_of_numbers) - 1
    checks = 0
    while low <= high:
        checks += 1
        mid = (low + high) // 2
        guess = list_of_numbers[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1
    print("Number of checks:", checks)
    return None

print(binary_search([1, 2, 3, 4, 5, 7, 91, 105], 91))  # Output: 1