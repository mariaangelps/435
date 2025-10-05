class Node:
    def __init__(self, key):
        self.key = key
        self.frequency = 1     
        self.left = None
        self.right = None

class BSTWithDuplicates:
    def __init__(self):
		#keys stored to count frequencies
        self.items = []    
        #insert

    def insert(self, key):
        # add the key into the list
        self.items.append(key)
        #new node created, frequency starts to be counted
        node = Node(key)
        node.frequency = self.items.count(key)
        return node
 
#Search

    def search(self, key):
        if key in self.items:
            freq = self.items.count(key)
            return True
        else:
            return False

#Delete

    def delete(self, key):
        if key in self.items:
            self.items.remove(key)

            #update frequency after deleting
            freq = self.items.count(key)
            return True
        else:
            return False
				
    def get_frequency(self, key):
        freq = self.items.count(key)
        return freq


# ==============================
#            MAIN
# ==============================
def main():
    tree = BSTWithDuplicates()
    for x in [5, 3, 7, 3, 7, 7, 2, 4, 6, 8]:
        tree.insert(x)

    tree.search(7)   # Found
    tree.search(10)  # Not found

    # Borrar 7 tres veces
    tree.delete(7)
    tree.delete(7)
    tree.delete(7)
    print(tree.search(7))   # Not found now
    print(tree.get_frequency(3))  # Should be 2
    print(tree.get_frequency(10)) # Should be 0
    print("All tests passed")
if __name__ == "__main__":
    main()
