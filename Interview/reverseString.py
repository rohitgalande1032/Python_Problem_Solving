#reverse using another extra string
def reverse(string):
    revrsed_str = ""
    for ch in range(1, len(string)+1):
        revrsed_str += string[-ch]
    return revrsed_str

#Slicing method
def reverseSlicing(string):
    return string[::-1]

if __name__ == "__main__":
    string = input("Enter a string ")
    print(f"Reverse of {string} is {reverse(string)}")

    #reverse string using swapping elements
    print(f"reverse using swapping of {string} is {reverseSlicing(string)}")

   