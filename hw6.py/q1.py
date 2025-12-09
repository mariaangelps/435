#Marcela Moura, Maria Angel Palacios, Assaf ... -> 

#Atcivity A
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


# Activity B












#main function

def main():
    print("Activity A: Frequency Table")
    st=input("Enter a string: ")
    frequency_table(st)
    print("\nActivity B: Huffman_code(st)")

main()

