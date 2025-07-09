def bubble_sort(arr, n=None, num_swaps=0):
    """
    Sorts an array using the recursive Bubble Sort algorithm.

    Parameters:
        arr (list): The unsorted list to be sorted.
        n (int, optional): The length of the unsorted portion of the array. 
            Defaults to None, which implies the entire array length.
        num_swaps (int): The number of swaps made during the sorting process.

    Returns:
        tuple: A tuple containing the sorted array and the number of swaps.

    """
    if n is None:
        n = len(arr)

    if n == 1:
        return arr, num_swaps

    unsorted = False 
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            num_swaps += 1
            unsorted = True  

    if not unsorted:
        return arr, num_swaps

    return bubble_sort(arr, n - 1, num_swaps)



def selection_sort(arr, end=None, num_swaps=0):
    """
    Sorts an array using the recursive Selection Sort algorithm based on the largest element each time.

    Parameters:
        arr (list): The unsorted list to be sorted.
        end (int): The index up to which the sorting process is done.
        num_swaps (int): The number of swaps made during the sorting process.

    Returns:
        tuple: A tuple containing the sorted array and the number of swaps.

    """
    if end is None:
        end = len(arr)

    if end <= 1:
        return arr, num_swaps

    max_index = 0
    for i in range(1, end):
        if arr[i] > arr[max_index]:
            max_index = i

    if max_index != end - 1:
        arr[max_index], arr[end - 1] = arr[end - 1], arr[max_index]
        num_swaps += 1

    return selection_sort(arr, end - 1, num_swaps)

def insertion_sort(arr, n=None, num_swaps=0):
    """
    Sorts an array using the recursive Insertion Sort algorithm.

    Parameters:
        arr (list): The unsorted list to be sorted.
        n (int, optional): The length of the unsorted portion of the array. 
            Defaults to None, which implies the entire array length.
        num_swaps (int): The number of swaps made during the sorting process.

    Returns:
        tuple: A tuple containing the sorted array and the number of swaps.

    """
    if n is None:
        n = len(arr)

    if n <= 1:
        return arr, num_swaps

    sorted_arr, num_swaps = insertion_sort(arr, n - 1, num_swaps)
    l = arr[n - 1]
    j = n - 2

    while j >= 0 and sorted_arr[j] > l:
        sorted_arr[j + 1] = sorted_arr[j]
        j -= 1
        num_swaps += 1

    sorted_arr[j + 1] = l

    return sorted_arr, num_swaps
