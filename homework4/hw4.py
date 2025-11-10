class Node:
    __slots__ = ("t", "prev")
    def __init__(self, t, prev=None):
        self.t = t
        self.prev = prev

class Transaction:
    def __init__(self, id: int, T: int):
        self.id = id
        self.T = T
        self.head = [None] * id                   
        self.count = [[0] * T for _ in range(id)]   


    #Insert: Time Complexity --> O(1)
    def insert(self, account, t) -> None:
        if account < 0 or account >= self.id:
            return  
        if t < 0 or t >= self.T:
            return
        new_node = Node(t, self.head[account])
        self.head[account] = new_node
        self.count[account][t] += 1
    # Search: Time Complexity --> O(1)
    def search(self, account, t):
        if account < 0 or account >= self.id:
            return False
        if t < 0 or t >= self.T:
            return False
        
        if self.count[account][t] > 0:
            return True
        else:
            return False
        
    #O(1)
    def most_recent(self, a: int):
        if a < 0 or a >= self.id: 
            return None
        top = self.head[a]
        return None if top is None else top.t
     # O(1)
    def delete_most_recent(self, account: int) -> None:
        if account < 0 or account >= self.id: 
            return
        amount_on_top = self.head[account]
        if amount_on_top is None:
            return
        x = amount_on_top.t
        self.head[account] = amount_on_top.prev
        self.count[account][x] -= 1