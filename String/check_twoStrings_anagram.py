def chackAnagram(s1, s2):
    str1 = {}
    str2 = {}

    if len(s1) != len(s2):
        return False
    
    for ch in s1:
        if ch in str1:
            str1[ch] += 1
        else:
            str1[ch] = 1

    for ch in s2:
        if ch in str2:
            str2[ch] += 1
        else:
            str2[ch] = 1
    
    for key in str1:
        if key not in str2 or str1[key] != str2[key]:
            return False
    return True

#using inbuilt sorted() function
def chckAnagrams(s1,s2):
    return sorted(s1) == sorted(s2)

if __name__ == "__main__":
    s1 = "rohitgalande"
    s2 = "galanderohit"

    # Using dictionary -- preferred in interview
    print("Anagrams" if chackAnagram(s1, s2) else "Not Anagrams")

    # Using inbuilt sorted() function
    print("Anagram" if chckAnagrams(s1, s2) else "Not Anagram")