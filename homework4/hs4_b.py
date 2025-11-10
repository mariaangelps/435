class StackNode:
    def __init__(self, amount, prev=None):
        self.amount = amount
        self.prev = prev

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.count = 1
        self.height = 1
        self.left = None
        self.right = None

def get_height(node):
    if node is None:
        return 0
    return node.height

def update_height(node):
    lh = get_height(node.left)
    rh = get_height(node.right)
    if lh >= rh:
        node.height = lh + 1
    else:
        node.height = rh + 1

def balance_factor(node):
    return get_height(node.left) - get_height(node.right)

def rotate_right(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    update_height(y)
    update_height(x)
    return x

def rotate_left(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    update_height(x)
    update_height(y)
    return y

def rebalance(node):
    update_height(node)
    bf = balance_factor(node)

    if bf > 1:
        if balance_factor(node.left) < 0:
            node.left = rotate_left(node.left)
        return rotate_right(node)

    if bf < -1:
        if balance_factor(node.right) > 0:
            node.right = rotate_right(node.right)
        return rotate_left(node)
    return node

def avl_find(node, key):
    while node is not None:
        if key == node.key:
            return node
        elif key < node.key:
            node = node.left
        else:
            node = node.right
    return None

def avl_insert(node, key):
    if node is None:
        return AVLNode(key)

    if key == node.key:
        node.count = node.count + 1
        return node
    elif key < node.key:
        node.left = avl_insert(node.left, key)
    else:
        node.right = avl_insert(node.right, key)
    return rebalance(node)

def min_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def avl_delete_all(node, key):
    if node is None:
        return None

    if key < node.key:
        node.left = avl_delete_all(node.left, key)
        if node is not None:
            node = rebalance(node)
        return node
    elif key > node.key:
        node.right = avl_delete_all(node.right, key)
        if node is not None:
            node = rebalance(node)
        return node
    else:
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left

        s = min_node(node.right)
        node.key = s.key
        node.count = s.count
        node.right = avl_delete_all(node.right, s.key)
        node = rebalance(node)
        return node

def avl_delete_one(node, key):
    if node is None:
        return None

    if key == node.key:
        if node.count > 1:
            node.count = node.count - 1
            return node
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left

        s = min_node(node.right)
        node.key = s.key
        node.count = s.count
        node.right = avl_delete_all(node.right, s.key)
        node = rebalance(node)
        return node

    elif key < node.key:
        node.left = avl_delete_one(node.left, key)
        if node is not None:
            node = rebalance(node)
        return node
    else:
        node.right = avl_delete_one(node.right, key)
        if node is not None:
            node = rebalance(node)
        return node


class Transaction_Un:
    def __init__(self, num_accounts):
        self.id = num_accounts
        self.top = []
        self.tree = []
        i = 0
        while i < num_accounts:
            self.top.append(None)
            self.tree.append(None)
            i = i + 1

    def _push(self, account, amount):
        new_node = StackNode(amount, self.top[account])
        self.top[account] = new_node

    def _peek(self, account):
        if self.top[account] is None:
            return None
        return self.top[account].amount

    def _pop(self, account):
        if self.top[account] is None:
            return None
        x = self.top[account].amount
        self.top[account] = self.top[account].prev
        return x

    def insert(self, account, amount):
        if account < 0 or account >= self.id:
            return
        self._push(account, amount)
        self.tree[account] = avl_insert(self.tree[account], amount)

    def search(self, account, amount):
        if account < 0 or account >= self.id:
            return False
        node = avl_find(self.tree[account], amount)
        if node is None:
            return False
        return True

    def most_recent(self, account):
        if account < 0 or account >= self.id:
            return None
        return self._peek(account)

    def delete_most_recent(self, account):
        if account < 0 or account >= self.id:
            return
        x = self._pop(account)
        if x is None:
            return
        self.tree[account] = avl_delete_one(self.tree[account], x)
