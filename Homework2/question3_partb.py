
#part b
class Node:
    def __init__(self, key):
        self.key = key
        self.children = []
        #each node will save its value key in 4 spots each
        for i in range(4):
            self.children.append(None)

class FourAryTree:
    def __init__(self):
        self.arr = []

    def insert(self,key):
        print(f"[INSERT] Agregando '{key}' al final del arreglo...")
        self.arr.append(key)
        print(f"         Estado actual del árbol: {self.arr}\n")

    def delete(self,key):
        print(f"[DELETE] Intentando borrar '{key}'...")
        if len(self.arr) == 0:
            return False

        # buscar la primera posición donde esté la clave
        looking_idx = -1        # -1 = no encontrado
        for j in range(len(self.arr)):
            if self.arr[j] == key:
                looking_idx = j
                break

        # si no lo encontramos
        if looking_idx == -1:
            print(f"         '{key}' no encontrado en el árbol.\n")
            return False
        
        print(f"         '{key}' encontrado en posición {looking_idx}.")
        # reemplazar con el último elemento y eliminar el último
        last_value = self.arr[-1]
        print(f"         Último elemento (deepest/rightmost) = '{last_value}'.")
        self.arr[looking_idx] = last_value
        self.arr.pop()
        return True

    def search(self,key):
        for i in self.arr:
            return True
        return False

    def children_indices(self, i):
        return [4*i + 1, 4*i + 2, 4*i + 3, 4*i + 4]
def main():
        
    tb = FourAryTree()
    for x in [1,2,3,4,5,6,7]:
        tb.insert(x)
    assert tb.search(6) is True
    tb.delete(3)         # swap con 7 y pop
    assert tb.arr == [1,2,7,4,5,6]  # compacto y en nivel
    print("All tests passed")
    print(tb.arr)
if __name__ == "__main__":
    main()