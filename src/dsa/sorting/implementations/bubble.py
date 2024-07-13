from src.helpers.custom_typevars import NumberType


def bubble_sort(arr: list[NumberType]) -> list[NumberType]:
    for i in range(len(arr)):
        # Loop over each element in array after i'th element and swap it until we get the largest on the right
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        # After completion of the loop the right most elements will be the largest
        # and this will keep happening until the last pass when all will be sorted
    return arr
