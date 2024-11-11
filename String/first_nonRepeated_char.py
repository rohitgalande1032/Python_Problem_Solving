def firstNonRepeatChar(string):
    char_count = {}
    #Traverse the string and use a dictionary to store the count of each character.
    for ch in string:
        if ch in char_count:
            char_count[ch] +=1
        else:
            char_count[ch] = 1
    
    #Traverse the string again, and for each character, check its count in the dictionary. 
    # The first character with a count of 1 is the first non-repeated character.
    for ch in string:
        if char_count[ch] == 1:
            return ch
    return None

if __name__ == "__main__":
    string = "roohiitt"
    print(f"First non repeated character is {firstNonRepeatChar(string)}")