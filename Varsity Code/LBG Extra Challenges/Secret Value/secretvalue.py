def secret_value(SortedArray, SecretValue):
    low = 0
    high = len(SortedArray) - 1
    while low <= high:
        middle = low + (high - low) // 2
        if SortedArray[middle] == SecretValue:
            return str(middle)
        elif SortedArray[middle] < SecretValue:
            low = middle + 1
        else:
            high = middle - 1
    return '-1'

