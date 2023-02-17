def is_palindrome_rec(s):
    """
    pre: `s` est un str
    post: détermine récursivement si `s` est un palindrome ou non
    """
    
    if  len(s)<=1:
        return True
    if s[0]== s[-1]:
        return  is_palindrome_rec(s[1:-1])
    return False


print(is_palindrome_rec("kayak"))
print(is_palindrome_rec("kaya"))
