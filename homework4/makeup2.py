class _Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class FirstUnique:
    def __init__(self, nums=None):
        self.count = {}
        self.nodePtr = {}
        self.head = None
        self.tail = None

        if nums is not None:
            self.initialize(nums)

    def initialize(self, nums):
        for num in nums:
            self.add(num)

    def add(self, num):
        #first appearance
        if num not in self.count:
            self.count[num] = 1
            self._append(num)
        else:
            self.count[num] += 1
            #remove from unique list
            if self.count[num] == 2:
                node = self.nodePtr.get(num)
                if node is not None:
                    self._remove(node)
                    self.nodePtr[num] = None
            # third or more → already non-unique, do nothing

    def showFirstUnique(self):
        #Returns the first unique number in the stream, or -1 if none exist.
        if self.head is None:
            return -1
        return self.head.value


    def _append(self, num):
        #append num to endd
        node = _Node(num)

        if self.tail is None:
           
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.nodePtr[num] = node

    def _remove(self, node):
        #remove node and update previous node
        if node.prev is not None:
            node.prev.next = node.next
        else:
            # poin curr node as head
            self.head = node.next

        #points to next and updates to curr
        if node.next is not None:
            node.next.prev = node.prev
        else:
            #node gets tail
            self.tail = node.prev
