#Marcela Moura, Maria Angel Palacios, Assaf ... -> 

#Activity A:
def frequency_table(st):
    
    frequency={}
    for char in st:
        if char in frequency:
            frequency[char] = frequency[char]+1
        else:
            frequency[char]=1

    #printing
    for char in frequency:
        if char ==" ":
            print ("spaces:",frequency[char])
        else:
            print (char,":",frequency[char])


# Activity B:
def huffman_code(st):
    #in case the string is empty 
    if len(st) ==0:
        return {}
    for char in st:
        frequency={}
        for char in st:
            if char in frequency:
                frequency[char] = frequency[char]+1
            else:
                frequency[char]=1

    class Node:
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

    nodes=[]
    for char in frequency:
        node= Node(char,frequency[char])
        nodes.append(node)

    if len(nodes) ==1:
        root=nodes[0]
    else:
        while len (nodes) >1:
            for i in range(len(nodes)):
                for j in range (i+1,len(nodes)):
                    if nodes[i].freq > nodes[j].freq:
                        nodes[i],nodes[j]=nodes[j],nodes[i]
            
            small_node1=nodes.pop(0)
            small_node2=nodes.pop(0)

            total_freq= small_node1.freq + small_node2.freq
            parent=Node(None,total_freq)
            parent.left=small_node1
            parent.right=small_node2

            nodes.append(parent)

        root=nodes[0]

    save_code={}

    def traverse(node,path):
        if node is None:
            return
        if node.char is not None:
            if path == "":
                path = "0"
            save_code[node.char]=path

        else:
            traverse (node.left, path + "0")
            traverse (node.right, path + "1")
    traverse (root,"")
        
    #printing
    for char in frequency:
        if char ==" ":
            print ("spaces:",save_code[char])
        else:
            print (char,":",save_code[char]) 
    return save_code


#Activity C:
            
def huffman_encode(st,codes):
    if len(st)==0:
        print("empty")
        return
    
    encoded_str=""
    for char in st:
        if char in codes:
            encoded_str = encoded_str+ codes[char]
        else:
            encoded_str= encoded_str + char
    print("Encoded string:\n", encoded_str)

#Activity D:

def huffman_tree(L):
    if len(L) ==0:
        return None
    
    class Node:
        def __init__(self, char=None):
            self.char = char
            self.left = None
            self.right = None
    root=Node()

    for char,code in L:

        curr=root
        for num in code:
            if num =='0':
                if curr.left is None:
                    curr.left=Node()
                curr=curr.left
            else:
                if curr.right is None:
                    curr.right=Node()
                curr=curr.right

        curr.char=char
    return root









# Activity e: 






#main function

def main():
    print("Activity A: Frequency Table")
    st=input("Enter a string: ")
    frequency_table(st)

    print("\nActivity B: Huffman_code(st)")
    codes = huffman_code(st)

    print("\nActivity C: Huffman_encode(st)")
    huffman_encode(st,codes)

    print("\nActivity D: Huffman_tree(L)")
    tree_root = huffman_tree(list(codes.items()))


main()

