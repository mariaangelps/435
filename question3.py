
#part a 
class Node:
    def __init__(self, key):
        self.key = key
        self.children = []
        #each node will save its value key in 4 spots each
        for i in range(4):
            self.children.append(None)

class FourAryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = Node(key)

        # check if root is empty
        if self.root is None:
            self.root = new_node
        else:
            listed_nodes = [self.root]
            inx = 0

            while inx < len(listed_nodes):
                current = listed_nodes[inx]
                inx += 1

                for i in range(4):
                    if current.children[i] is None:
                        current.children[i] = new_node
                        return
                    else:
                        listed_nodes.append(current.children[i])

    def delete(self, key):
    # Verificar si la raíz está vacía
        if self.root is None:
            return

        # Verificar si la raíz es el nodo a eliminar
        if self.root.key == key:
            no_children = True
            for child in self.root.children:
                if child is not None:
                    no_children = False
                    break

            if no_children:
                self.root = None
            return
        # Recorrer el árbol en nivel para encontrar el nodo a eliminar
        listed_nodes = [self.root]
        inx = 0
        while inx < len(listed_nodes):
            current = listed_nodes[inx]
            inx += 1

            for i in range(4):
                child = current.children[i]
                if child is not None:
                    if child.key == key:
                        no_children = True
                        for grandchild in child.children:
                            if grandchild is not None:
                                no_children = False
                                break

                        if no_children:
                            current.children[i] = None
                        return
                    else:
                        listed_nodes.append(child)
            inx += 1

    def search(self, key):
        if self.root is None:
            return False
        listed_nodes = [self.root]
        inx = 0
        while inx < len(listed_nodes):
            current = listed_nodes[inx]
            inx += 1
            if current.key == key:
                return True
            for i in range(4):
                child = current.children[i]
                if child is not None:
                    listed_nodes.append(child)
        return False
        

    
            
def main():
    tree = FourAryTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)
    tree.insert(8)

    print(tree.search(5))  # Output: True
    print(tree.search(10)) # Output: False

    tree.delete(5)
    print(tree.search(5))  # Output: False

    tree.delete(1)  # Trying to delete root with children
    print(tree.search(1))  # Output: True


if __name__ == "__main__":
    main()
    "trying "