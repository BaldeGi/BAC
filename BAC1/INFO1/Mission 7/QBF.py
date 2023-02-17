words=[" while " , "the" , " congress " , "of" , " the" , " republic ", " endlessly " ,
            " debates " , " this " , " alarming " , " chain " , "of" , " events " , "the" ,
            " supreme " , " chancellor " , "has" , " secretly " , " dispatched " , "two" ,
            " jedi " , " knights "
            ]


def count(words):
    d={}
    for i in words:
        d[i]=d.get(i,0)+1
    return d



def tuples(words):
    liste=[]
    for i in count(words):
        liste.append((count(words)[i],i))
    liste=sorted(liste,reverse=True)
   
#OU

def tuples(words):
    liste=[]
    d=count(words)
    for i in d:
        liste.append((d[i],i))
    liste=sorted(liste,reverse=True)
    return liste



def top_k(words,k):
    lst=[]
    for i in range(k):
        lst.append(tuples(words)[i])
    while i<len(tuples(words))-k:
        if tuples(words)[i][0]==tuples(words)[i+1][0]:
            lst.append(tuples(words)[i+1])
            i+=1
        else:
            return lst
    return lst
print(top_k(words,1))
    


