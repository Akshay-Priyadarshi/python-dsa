from src.helpers.custom_typevars import NumberType


def get_intersection(a: list[NumberType], b: list[NumberType]):
    """ """
    i = 0
    j = 0
    intersection = []
    while i < len(a) and j < len(b):
        if a[i] == a[i - 1]:
            i += 1
            continue
        if b[j] == b[j - 1]:
            j += 1
            continue
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            intersection.append(a[i])
            i += 1
            j += 1
    return intersection
