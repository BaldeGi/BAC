from projet import*

def lexer(chn):
    chn = token(chn)
    l = []
    i=0
    if chn == [] :
        raise ValueError
    while i <= len(chn)-1:
        if lexers(chn[i]) == "OPEN":
            l.append(lexers(chn[i]))
            i+=1
        elif lexers(chn[i]) != "NUM":
            raise ValueError
        elif lexers(chn[i])== "NUM" :
            l.append(chn[i])
            if lexers(chn[i+1]) != "NUM" and lexers(chn[i+1]) != "VALUE":
                raise ValueError
            else:
                while lexers(chn[i+1]) == "VALUE" or lexers(chn[i+1]) == "NUM":
                    l.append(chn[i+1])
                    i+=1
                if lexers(chn[i+1]) != "CLOSE":
                    raise ValueError
                else:
                    while lexers(chn[i+1]) == "CLOSE":
                        l.append(lexers(chn[i+1]))
                        i+=1
                        if i >= len(chn)-1:
                            if chn.count("(")!= chn.count(")"):
                                raise ValueError
                            return l
                    if lexers(chn[i+1]) != "OPEN":
                        raise ValueError
                    i+=1
    if chn.count("(")!= chn.count(")"):
        raise ValueError
    return l




def lexers(t):
    if t == "(":
        return  "OPEN"
    elif t  == ")":
        return "CLOSE"
    elif t.isdigit():
        return "NUM"
    else:
        return "VALUE"
    
    
    
    
def token(chn):
    l,l1=[],[]
    mot=" "
    chn = chn.strip()
    chn=chn.split(" ")
    for i in range(len(chn)):
        for j in range(len(chn[i])):
            if chn[i][j].strip()!="(" and chn[i][j].strip()!=")" :
                mot+=chn[i][j]
                if j == len(chn[i])-1:
                    l.append(mot.strip())
                    mot =" "
            else:
                if mot != " " :
                    l.append(mot)
                    mot = " "
                l.append(chn[i][j].strip())
    for i in l:
        l1.append(i.strip())
    return l1




def valid_list(l):
    liste,l = [], lexer(l)
    value =" "
    for i in range(len(l)):
        if l[i].isdigit() and l[i-1]== "OPEN"  or l[i]=="OPEN":
            liste.append(l[i])
        else:
            if l[i]!="CLOSE":
                value+=l[i]+" "
            if l[i]=="CLOSE" and value!= " ":
                liste.append(value)
                value=" "
        if l[i]=="CLOSE":
            liste.append("CLOSE")
    return liste




def creer_arbre_aux(valid_str):
    if valid_str.pop(0) != "OPEN":
        raise ValueError
    if valid_str[0].isdigit():
        valid_str.pop(0)
        l = ArbreBinaire(valid_str.pop(0).strip())
    else:
        left = creer_arbre_aux(valid_str)
        right = creer_arbre_aux(valid_str)
        l = ArbreBinaire(None, left, right)
    if valid_str.pop(0) != "CLOSE":
        raise ValueError
    return l






















