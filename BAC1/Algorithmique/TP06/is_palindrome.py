def is_palindrome(s):
    """
    pre: `s` est un str
    post: détermine itérativement si `s` est un palindrome ou non
    """
    j=1
    for i in range(len(s)):
        if s[i]!=s[-j]:
            return False
        j+=1
    return True
    



print(is_palindrome("kayak"))
print(is_palindrome("radar"))
print(is_palindrome("rada"))
print(is_palindrome("bonjour"))