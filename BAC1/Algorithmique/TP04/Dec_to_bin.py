from TAD_File import Queue
#Faire une classe Stack pour que ça fonctionne 
def dec_to_bin(n):
    """
    pre: `n` > 0
    post: renvoie la représentation binaire de `n`.
        Le premier élément de la file renvoyée est le bit de poids fort.
        Le nombre de bits renvoyé est le plus petit possible.
    """
    file= Queue()
    f= Stack()
    while n>0:
        reste = n%2
        f.push(reste)
        n//=2
    while not f.is_empty():
        file.enqueue(f.pop())
    return file

print(dec_to_bin(42))