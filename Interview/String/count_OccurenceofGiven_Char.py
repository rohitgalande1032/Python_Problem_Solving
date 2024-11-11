# Using a Dictionary to Count All Characters (for Multiple Characters)
def countOccurenceOfChar(string, char):
    char_occurences = {}

    for ch in string:
        if ch in char_occurences:
            char_occurences[ch] += 1
        else:
            char_occurences[ch] = 1

    for ch in char_occurences:
        return char_occurences[char]
    

#count using inbuilt Count() method
def countOccurence(string, char):
    return string.count(char)

# Count occurence for single Character
def singleCharCount(string, char):
    count = 0
    for ch in string:
        if ch in char:
            count +=1
    return count
    
if __name__ == "__main__":
    string = "rohitgalande"
    character = 'a'
    print(f"For multiple Characters : occurences of {character} is {countOccurenceOfChar(string, character)}")

    print(f"Using Inbuild Count() function : occurences of {character} is {countOccurence(string, character)}")

    print(f"For single character : occurence of {character} is {singleCharCount(string, character)}")
