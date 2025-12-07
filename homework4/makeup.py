def find_peak(arr):
    #returns index
    
    low, high = 0, len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < arr[mid + 1]:
            # estamos en la parte creciente
            low = mid + 1
        else:
            # parte decreciente o justo en el pico
            high = mid
    return low  # low == high


def binary_search_increasing(arr, low, high, target):
    """Búsqueda binaria en segmento creciente."""
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


def binary_search_decreasing(arr, low, high, target):
    """Búsqueda binaria en segmento decreciente."""
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        if arr[mid] > target:   # ojo: al revés porque es decreciente
            low = mid + 1
        else:
            high = mid - 1
    return False


def bitonic_search(arr, target):
    """
    Devuelve True si target está en el arreglo bitónico arr, False si no.
    Usa ~3 log n comparaciones en el peor caso.
    """
    if not arr:
        return False

    peak = find_peak(arr)

    if arr[peak] == target:
        return True

    # buscar en la parte creciente [0..peak-1]
    if binary_search_increasing(arr, 0, peak - 1, target):
        return True

    # buscar en la parte decreciente [peak+1..n-1]
    if binary_search_decreasing(arr, peak + 1, len(arr) - 1, target):
        return True

    return False

