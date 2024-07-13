from typing import List

def naive_get_max_subarr_sum(arr: List[int],k: int):
    """
    
    """
    max_sum = 0
    for i in range(0,len(arr)-k):
        subarr_sum = 0
        for j in range(i,i+k):
            subarr_sum += arr[j]
        max_sum = max(max_sum,subarr_sum)
    return max_sum

def get_max_subarr_sum(arr: List[int],k: int):
    """
    Sliding window
    TIme Complexity = O(n) 
    """
    subarr_sum = 0
    for i in range(0,k):
        subarr_sum += arr[i]
    max_sum = subarr_sum
    for i in range(k,len(arr)):
        subarr_sum = subarr_sum - arr[i-k] + arr[i]
        max_sum = max(subarr_sum,max_sum)
    return max_sum