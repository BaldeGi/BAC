def extract(code):
    l=[]
    vowel_low=['a','e','i','o','u','y']
    vowel_up=['A','E','I','O','U','Y']
    for i in range(len(code)):
        if code[i] in vowel_low:
            l.append("vowel-low")
        elif code[i] in vowel_up:
            l.append("vowel-up")
        elif code[i].isdigit():
            l.append("number")
        elif code[i] not in vowel_low and code[i] not in vowel_up and code[i].isdigit()==False and code[i]==code[i].lower() and code[i]!=" ":
            l.append("consonant-low")
        else:
            l.append("consonant-up")
    return " ".join(l)
    
print(extract(" "))