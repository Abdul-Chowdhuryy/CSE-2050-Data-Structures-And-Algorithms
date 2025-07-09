import math
from enum import Enum

INVERSION_BOUND = 10  # pre-defined constant; independent of list input sizes

class MagicCase(Enum):
    GENERAL = 0
    SORTED = 1
    CONSTANT_NUM_INVERSIONS = 2
    REVERSE_SORTED = 3


def linear_scan(L):
    """
    Function that analyzes a list and returns the particular MagicCase that applies to it.
    """
    if sorted(L) == L:
        return MagicCase.SORTED
    elif sorted(L, reverse=True):
        return MagicCase.REVERSE_SORTED
    elif sum(L[i-1] > L[i] for i in range(1, len(L))) <= INVERSION_BOUND:
        return MagicCase.CONSTANT_NUM_INVERSIONS
    else:
        return MagicCase.GENERAL
    
    pass


def reverse_list(L, alg_set=None):
     """
    Function that efficiently reverses a list in-place.
    """
     midpoint = len(L) // 2
     for i in range(midpoint):
          L[i], L[-(i + 1)] = L[-(i + 1)], L[i]
pass


def magic_insertionsort(L, left, right, alg_set=None):
    """
    Function that uses insertion sort to sort (in-place) ONLY the sublist of a list.
    """
    for i in range(left+1, right):
        key = L[i]
        j = i - 1
        while j >= left and L[j] > key:
            L[j+1] = L[j]
            j -= 1
        L[j+1] = key
    pass


def magic_mergesort(L, left, right, alg_set=None):
    """
    Function that uses merge sort to sort ONLY the sublist of a list.
    """
    if right - 1 > 1:
        mid = (left + right) // 2
        magic_mergesort(L, left, mid)
        magic_mergesort(L, mid, right)
        temp = []
        i = left
        j = mid
        while i < mid and j < right:
            if L[i] <= L[j]:
                temp.append(L[i])
                i += 1
            else:
                temp.append(L[j])
                j += 1
        while i < mid:
            temp.append(L[i])
            i += 1
        while j < right:
            temp.append(L[j])
            j += 1
        
        for k in range(len(temp)):
            L[left+k] = temp[k]
    pass


def magic_quicksort(L, left, right, depth=0, alg_set=None):
    """
    Function that uses quick sort to sort ONLY the sublist of a list.
    """
    if right - left > 1:
        pivot_index = right - 1
        i = left - 1
        for j in range(left, right -1):
            if L[j] < L[pivot_index]:
                i += 1
                L[i], L[j] = L[j], L[i]
        L[i + 1], L[right - 1] = L[right - 1], L[i + 1]
        pivot_index = i + 1
        if depth > 2 * math.log2(right - left) + 1:
            magic_mergesort(L, left, right)
        else:
            magic_quicksort(L, left, pivot_index, depth + 1)
            magic_quicksort(L, pivot_index + 1, right, depth + 1)
    elif right - left == 1:
            if L[left] > L[right]:
             L[left], L[right] = L[right], L[left]
    pass



def magicsort(L):
    """
    Function that sorts an input list using a hybrid sorting algorithm (magicsort).
    """
    alg_set = set()
    case = linear_scan(L)
    if case == MagicCase.SORTED or case == MagicCase.REVERSE_SORTED:
        return alg_set
    elif case == MagicCase.CONSTANT_NUM_INVERSIONS:
        magic_insertionsort(L, 0, len(L))
        alg_set.add('magic_insertionsort')
    elif case == MagicCase.GENERAL:
        magic_quicksort(L, 0, len(L))
        alg_set.add('magic_quicksort')
    return alg_set

