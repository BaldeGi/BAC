from TAD_File import Queue

def bin_to_dec(n):
    """
    pre: `n` est une file renvoyant la représentation binaire
        d un nombre en commençant par le bit de poids fort
    post: renvoie la valeur de `n` dans sa forme décimale
        `n` est vide
    """
    lst=[i for i in range(len(n)-1,-1,-1)]
    val=0
    i=0
    while not n.is_empty():
        v = n.dequeue()
        val += v*(2)**lst[i]
        i+=1
    return val

#Test
q = Queue()
q.enqueue(1)
q.enqueue(1)
q.enqueue(1)
q.enqueue(0)
q.enqueue(1)
q.enqueue(1)
q.enqueue(1)
q.enqueue(1)
q.enqueue(1)
q.enqueue(1)
q.enqueue(0)
q.enqueue(0)
q.enqueue(1)
q.enqueue(0)

print(bin_to_dec(q))
