from src.helpers.custom_typevars import NumberType


def selection_sort(arr: list[NumberType]) -> list[NumberType]:
    for i in range(len(arr)):
        minInd = i
        # Loop on the array after the current i'th element and find the element with min index
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minInd]:
                minInd = j
        # Once the min index is found swap it with the i'th element to get sorted array
        arr[i], arr[minInd] = arr[minInd], arr[i]
    return arr
