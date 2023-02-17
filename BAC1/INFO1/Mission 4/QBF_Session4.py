"""def positions(p,s):
    s,p=s.lower(),p.lower()
    i,j=0,1
    index=[]
    if "?" not in p:
        while j <len(s):
            if s[i]+s[j]==p:
                index.append(i)
            j+=1
            i+=1
    elif "??" in p:
        for i in range(len(s)-1):
            index.append(i)
    elif p[1]=="?":
        while j <len(s):
            if s[i]==p[0]:
                index.append(i)
            j+=1
            i+=1
    else:
        while j <len(s):
            if s[i]==p[1]:
                index.append(i-1)
            j+=1
            i+=1
    return index"""

#OU

def match(s1,s2):
    l=[]
    for i in range(len(s1)):
        if s1[i]!="?":
            if s1[i].lower()!=s2[i].lower():
               return False
    return True

def positions(p,s):
    l=[]
    for i in range(len(s)-1):
        if match(p,s[i:]):
            l.append(i)
    return l



print(positions("A?","CABAEACF"))








