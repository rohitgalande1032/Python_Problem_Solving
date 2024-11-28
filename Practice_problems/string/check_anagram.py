# def check_anagram(s1, s2):
#     return sorted(s1) == sorted(s2)

def check_anagram(s1, s2):
    s1_count = {}
    s2_count = {}

    for ch in s1:
        if ch in s1_count:
            s1_count[ch] += 1
        else:
            s1_count[ch] = 1

    for ch in s2:
        if ch in s2_count:
            s2_count[ch] += 1
        else:
            s2_count[ch] = 1
    
    for key in s1_count:
        if key not in s2_count or s1_count[key] != s2_count[key]:
            return False
    return True

result = check_anagram("listen", "silent")
print("anagram" if result else "Not anagram")