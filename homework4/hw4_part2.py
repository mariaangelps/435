class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def count_n(root):
    if root is None:
        return 0
    left_count = count_n(root.left)
    right_count = count_n(root.right)
    return left_count + 1 + right_count

def inorder(root, out_array, pos_ref):
    if root is None:
        return
    inorder(root.left, out_array, pos_ref)
    idx = pos_ref[0]
    out_array[idx] = root.key
    pos_ref[0] = idx + 1
    inorder(root.right, out_array, pos_ref)

def merge_arr(arr, na, b, nb, c):
    i = 0
    j = 0
    k = 0
    while i < na and j < nb:
        if arr[i] <= b[j]:
            c[k] = arr[i]
            i = i + 1
        else:
            c[k] = b[j]
            j = j + 1
        k = k + 1
    while i < na:
        c[k] = arr[i]
        i = i + 1
        k = k + 1
    while j < nb:
        c[k] = b[j]
        j = j + 1
        k = k + 1

def build_balanced(arr, left, right):
    if left > right:
        return None
    mid = (left + right) // 2
    root = Node(arr[mid])
    root.left = build_balanced(arr, left, mid - 1)
    root.right = build_balanced(arr, mid + 1, right)
    return root

def merge_two_avls(t1, t2):
    n1 = count_n(t1)
    n2 = count_n(t2)
    a = [0] * n1
    b = [0] * n2
    pos_a = [0]
    pos_b = [0]
    inorder(t1, a, pos_a)
    inorder(t2, b, pos_b)
    c = [0] * (n1 + n2)
    merge_arr(a, n1, b, n2, c)
    return build_balanced(c, 0, (n1 + n2) - 1)
