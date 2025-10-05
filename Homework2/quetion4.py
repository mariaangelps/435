# ======== NODO (súper simple) ========
class Node:
    def __init__(self, key):
        self.key = key          # la clave (entero)
        self.frequency = 1      # cuántas veces insertamos esta clave
        self.left = None        # hijo izquierdo
        self.right = None       # hijo derecho


# ======== BST con duplicados (beginner) ========
class BSTWithDuplicates:
    def __init__(self):
        self.root = None
        self._deleted = False   # banderita interna para saber si delete funcionó

    # ---------- INSERT ----------
    def insert(self, key):
        """
        Si la clave ya está: frequency += 1
        Si no está: creamos un nuevo nodo y lo colocamos como BST normal.
        (Iterativo para que sea fácil de leer)
        """
        if self.root is None:
            self.root = Node(key)
            return

        cur = self.root
        while True:
            if key == cur.key:
                cur.frequency += 1
                return
            elif key < cur.key:
                if cur.left is None:
                    cur.left = Node(key)
                    return
                cur = cur.left
            else:  # key > cur.key
                if cur.right is None:
                    cur.right = Node(key)
                    return
                cur = cur.right

    # ---------- SEARCH ----------
    def search(self, key):
        """
        Devuelve True si la clave existe (frequency >= 1), False si no.
        """
        cur = self.root
        while cur is not None:
            if key == cur.key:
                return True
            elif key < cur.key:
                cur = cur.left
            else:
                cur = cur.right
        return False

    # (Opcional) para ver cuántas veces está una clave
    def get_frequency(self, key):
        cur = self.root
        while cur is not None:
            if key == cur.key:
                return cur.frequency
            elif key < cur.key:
                cur = cur.left
            else:
                cur = cur.right
        return 0

    # ---------- DELETE ----------
    def delete(self, key):
        """
        Borra UNA ocurrencia de 'key'.
        - Si frequency > 1: solo frequency -= 1 (no se toca la forma del árbol).
        - Si frequency == 1: se elimina el nodo como en un BST normal:
            * 0 hijos  -> se quita el nodo.
            * 1 hijo   -> se reemplaza por su único hijo.
            * 2 hijos  -> se reemplaza por el sucesor (mínimo del subárbol derecho).
                           Copiamos (key, frequency) del sucesor y luego quitamos
                           el sucesor COMPLETO del subárbol derecho.
        Devuelve True si borró algo; False si la clave no estaba.
        """
        self._deleted = False
        self.root = self._delete_rec(self.root, key)
        return self._deleted

    def _delete_rec(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete_rec(node.left, key)
            return node
        elif key > node.key:
            node.right = self._delete_rec(node.right, key)
            return node
        else:
            # === encontramos la clave ===
            if node.frequency > 1:
                node.frequency -= 1
                self._deleted = True
                return node

            # frequency == 1 -> eliminar físicamente el nodo
            # caso 0 hijos
            if node.left is None and node.right is None:
                self._deleted = True
                return None

            # caso 1 hijo
            if node.left is None:
                self._deleted = True
                return node.right
            if node.right is None:
                self._deleted = True
                return node.left

            # caso 2 hijos:
            # 1) buscamos el sucesor (mínimo del subárbol derecho)
            succ = self._min_node(node.right)
            # 2) copiamos key y frequency del sucesor al nodo actual
            node.key = succ.key
            node.frequency = succ.frequency
            # 3) quitamos el sucesor COMPLETO del subárbol derecho
            node.right = self._delete_node_completely(node.right, succ.key)
            self._deleted = True
            return node

    # ---------- helpers chiquitos ----------
    def _min_node(self, node):
        """Devuelve el nodo con la clave mínima (ir todo a la izquierda)."""
        cur = node
        while cur.left is not None:
            cur = cur.left
        return cur

    def _delete_node_completely(self, node, key):
        """
        Elimina el nodo con 'key' IGNORANDO su frequency (o sea, borra el nodo entero de una).
        Se usa solo cuando ya copiamos (key, frequency) del sucesor.
        """
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete_node_completely(node.left, key)
            return node
        elif key > node.key:
            node.right = self._delete_node_completely(node.right, key)
            return node
        else:
            # borrar nodo completo (como BST normal sin duplicados)
            if node.left is None and node.right is None:
                return None
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # dos hijos: reemplazar por mínimo del subárbol derecho y seguir
            succ = self._min_node(node.right)
            node.key = succ.key
            node.frequency = succ.frequency
            node.right = self._delete_node_completely(node.right, succ.key)
            return node

def main():
    t = BSTWithDuplicates()
    for x in [5, 3, 7, 3, 7, 7, 2, 4, 6, 8]:
        t.insert(x)

    print(t.search(7))        # True
    print(t.get_frequency(7)) # 3
    print(t.get_frequency(3)) # 2

    t.delete(7)  # 7: 3 -> 2
    t.delete(7)  # 7: 2 -> 1
    t.delete(7)  # 7: 1 -> (nodo 7 eliminado físicamente)
    print(t.search(7))        # False
    print(t.get_frequency(7)) # 0

if __name__ == "__main__":
    main()