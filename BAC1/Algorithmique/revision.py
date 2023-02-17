def test(l): # Tri à Bulle
    count,count2=0,0
    for i in range(len(l)-1,0,-1):
        for j in range(1,i+1):
            count+=1
            if l[j-1]>l[j]:
                count2+=1
                l[j-1],l[j]=l[j],l[j-1]
    return l , count , count2
                
    
print(test([65, 97, 43, 12, 29, 14, 99]))



def test(l): #Tri par selection
    count,count2=0,0
    for i in range(len(l)):
        mini=i
        for j in range(i+1,len(l)):
            count+=1
            if l[j] < l[mini]:
                mini=j
        if mini!=i:
            count2+=1
            l[i],l[mini]=l[mini],l[i]
    return l ,count , count2

print(test([65, 97, 43, 12, 29, 14, 99]))
print("\n")

class List:
    def __init__(self, elem=None):
        """
        pre:  -
        post: initialize a new List with `elem` as first element,
              if `elem` is None, this is interpreted as an empty List
        """
        self.first_elem = elem   # Element in first position
        if elem is not None:
            self.tail_list = List()  # Tail list of the current List
        else:
            self.tail_list = None

    def head(self):
        """
        pre: current List is not empty
        post: return the first element of the current List
        """
        if self.is_empty():
            raise RuntimeError('Cannot get first element from an empty List')
        return self.first_elem

    def tail(self):
        """
        pre: current List is not empty
        post: return the tail List of the current List
        """
        if self.is_empty():
            raise RuntimeError('Cannot get tail List from an empty List')
        return self.tail_list

    def is_empty(self):
        """
        pre: -
        post: return True if the List is empty, False otherwise
        """
        return self.first_elem is None

    def concat(self, elem):
        """
        pre: `elem` is not None
        post: return a new List with `elem` in first position
              and the current List as tail
        """
        if elem is None:
            raise RuntimeError('Cannot concat a None element')
        newlist = List(elem=elem)
        newlist.tail_list = self
        return newlist

    def __str__(self):
        """
        pre: -
        post: return the List content as a string
        """
        if self.is_empty():
            return '[]'
        return '['+ str(self.head()) + str(self.tail()) +']'
    
def find_in_list(l, e, k): #Examen Blanc : Faux car fallait faire une recusrion
    """
    pre: `l` est une `List`
    pre: `e` est un élément éventuellement présent dans la liste `l` et différent de `None`
    pre: `k` est un entier tel que `k` > 0
    post: renvoie la sous-liste de `l` débutant à la `k`-ième occurrence de `e`dans `l`.
          Si `e` apparaît moins de `k` fois dans la liste `l`, renvoie `None`
    """
    
    def countocc(l, e, k, acc):
        if l.is_empty():
            return None
        elif e == l.head():
            acc += 1
            if k == acc:
                return l
        return countocc(l.tail(),e,k,acc)
    return countocc(l, e, k, 0)
    
    
    
    """if l.is_empty():
        return List()
    count=0
    if l.head() == e and k==1:
        return l
    if l.head() == e:
        count+=1
    while not l.tail_list.is_empty():
        if l.tail_list.head()==e:
            count+=1
            if count==k:
                return l.tail()
        l.tail_list= l.tail_list.tail()
    if count<k:
        return None"""
        
          
l=List()
l1=List()
l2=List()
l3=List()
l2=l2.concat(3)
l2=l2.concat(2)
l2=l2.concat(1)
print(find_in_list(l2,1,1))
print("\n")
l=l.concat(3)
l=l.concat(5)
l=l.concat(2)
l=l.concat(3)
l=l.concat(4)
l=l.concat(3)
l=l.concat(2)
print(l)
print(find_in_list(l,3, 2))
print("\n")
l1=l1.concat(5)
l1=l1.concat(3)
l1=l1.concat(-2)
print("\n")
print(find_in_list(l1,0, 1))
print("\n")
print(find_in_list(l3,0, 1))
























