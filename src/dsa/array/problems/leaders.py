from typing import List


def get_leaders(arr: List[int]):
    leaders = []
    leader = 0
    for i in range(len(arr)-1,-1,-1):
        if arr[i] > leader:
            leader = arr[i]
            leaders.append(leader)
    return leaders