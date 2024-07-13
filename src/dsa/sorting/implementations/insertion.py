from src.helpers.custom_typevars import NumberType


def insertion_sort(arr: list[NumberType]) -> list[NumberType]:
    for i in range(1, len(arr)):
        # Now the left part from i is considered sorted and we have to put the next element which is incoming
        # to the left in the proper place in the sorted array
        # Save the value to be  inserted
        key = arr[i]
        j = i - 1
        # Move the j'th element to i -1 to 0 until the j'th element is greater than the value to be inserted
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        print(j)
        # Once the proper place is found for the element in the left sorted array we add the element
        arr[j + 1] = key
    return arr


print(insertion_sort([10, 5, 8, 20, 2, 18, 2]))
