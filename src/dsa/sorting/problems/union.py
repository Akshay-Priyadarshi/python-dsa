from src.helpers.custom_typevars import NumberType


def get_union(a: list[NumberType], b: list[NumberType]):
    i = 0
    j = 0
    unioned = []
    while i < len(a) and j < len(b):
        if a[i] == a[i - 1]:
            i += 1
            continue
        if b[j] == b[j - 1]:
            j += 1
            continue
        if a[i] > b[j]:
            unioned.append(b[j])
            j += 1
        elif a[i] < b[j]:
            unioned.append(a[i])
            i += 1
        else:
            unioned.append(a[i])
            i += 1
            j += 1
    while i < len(a):
        if a[i] == a[i - 1]:
            i += 1
            continue
        unioned.append(a[i])
        i += 1
    while j < len(b):
        if b[j] == b[j - 1]:
            j += 1
            continue
        unioned.append(b[j])
        j += 1
    return unioned
