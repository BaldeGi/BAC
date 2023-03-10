from resultat import Resultat
from coureur import Coureur
from temps import Temps
from orderedlinkedlist import OrderedLinkedList
####################
# LinkedList class #
####################
class Classement :
    
    def __init__(self,nom,age, lst=[]):
        """
        Initialises a new linked list object, with a given list of elements lst.
        @pre:  -
        @post: A new linked list object has been initialised.
               Its length is equal to the number of elements in lst.
               The data elements stored in the linked list's nodes correspond to those of the list lst,
               and appear in the same order as in that list.
               If no list lst is passed as argument, the newly created linked list
               will have 0 length, contain no nodes and its head will point to None. 
        """
        self.__length = 0          # current length of the linked list
        self.__head = None         # pointer to the first node in the list
        self.__last = None         # pointer to the last node in the list
        self.board=OrderedLinkedList()
        self.n=nom
        self.age=age
        self.cr=Coureur(self.n,self.age)
        self.t=Temps()
        self.c=Resultat(self.cr,self.t)
        lst.reverse()              # reverse to ensure elements will appear in same order
        for e in lst :             # add elements of input list lst one by one 
            self.add(e)
            
    def size(self):
        """
        Accessor method which returns the number of nodes contained in this linked list.
        @pre:  -
        @post: Returns the number of nodes (possibly zero) contained in this linked list.
        """
        return self.__length
    
    def inc_size(self):
        """
        Mutator method to increase the size count of this linked list by one.
        @pre:  -
        @post: 1 has been added to the size counter of the number of nodes contained in this linked list.
        """
        self.__length += 1

    def dec_size(self):
        """
        Mutator method to decrease the size count of this linked list by one.
        @pre:  -
        @post: 1 has been substracted from the size counter of the number of nodes contained in this linked list.
        """
        self.__length -= 1

    def first(self):
        """
        Accessor method which returns the first node of this linked list.
        @pre:  -
        @post: Returns a reference to the head of this linked list,
               or None if the linked list contains no nodes.
        """
        return self.__head
    
    def set_first(self,n):
        """
        Mutator method to reassign the head of this linked list to a new node.
        @pre:  -
        @post: The head of this linked list new refers to node n.
        """
        self.__head = n
        
    def add(self, cargo):
        """ 
        Adds a new Node with given cargo to the front of this linked list. 
        @pre:  self is a (possibly empty) LinkedList.
        @post: A new Node object is created with the given cargo.
               This new Node is added to the front of the linked list.
               The length counter has been incremented by 1.
               The head of the linked list now points to this new node.
        """
        node = self.Node(cargo,self.first())
        if self.first() == None :   # when this is the first element being added,
            self.__last = node     # set the last pointer to this new node
        self.set_first(node)
        self.inc_size()

    def print(self):
        """
        Prints the contents of this linked list and its nodes.
        @pre:  self is a (possibly empty) LinkedList
        @post: Has printed a space-separated list of the form "[ a b c ... ]",
               where "a", "b", "c", ... are the string representation of each 
               of the linked list's nodes.
               A space is printed after and before the opening and closing bracket,
               as well as between any two elements.
               An empty linked is printed as "[ ]".
        """
        self.print_avec_separateur()

    def print_avec_separateur(self, separateur=" "):
        """
        Auxiliary method to print the elements of this linked list,
        separated by a given separateur (by default: a space " ")
        """
        print("[", end=" ")
        if self.first() is not None:
            self.first().print_list_avec_separateur(separateur)
        print("]")
        
    def print_avec_virgule(self):
        """
        Method to print the elements of this linked list,
        separated by commas and a space: ", ".
        """
        self.print_avec_separateur(", ")    
    
    def print_backward(self):
        """
        Prints the contents of this linked list and its nodes, back to front.
        @pre:  self is a (possibly empty) LinkedList.
        @post: Has printed a space-separated list of the form "[ ... c b a ]",
               where "a", "b", "c", ... are the string representation of each 
               of the linked list's nodes. The nodes are printed in opposite order:
               the last nodes' value are printed first.
               A space is printed after and before the opening and closing bracket,
               as well as between any two elements.
               An empty linked is printed as "[ ]".
        """
        print("[", end=" ")
        if self.first() is not None:
            self.first().print_backward()
        print("]")

    def remove(self):
        """
        Removes the node at the start of the list. Leaves the list intact if already empty. 
        """
        if self.first() is not None:
            self.dec_size()
            self.set_first(self.first().next())
        if self.size() == 0:       # when there are no more elements in the list,
            self.__last = None       # remove the pointer to the last element
    
    def add_to_end(self, cargo):
        """
        Adds a node with given cargo to the end of this linked list.
        """
        if self.size() == 0 :        # si la liste est encore vide,
            self.add(cargo)            # ajouter ??  la fin correspond au ajouter au d????but
        else :                         # si la liste contient d????j??  au moins un noeud (et donc une dernier noeud)
            node = self.Node(cargo)
            self.__last.set_next(node) # make the current last node point to this new node
            self.__last = node         # set the last node reference to this new node
            self.inc_size()            # increment list size by one
            
            
    def insert(self,s):
        suivant =self.first()
        if suivant is None:
            self.__head = self.Node(s,suivant)
        elif s < suivant.value():
            self.__head = self.Node(s,suivant)
        else:
            element=suivant
            if element.next()!=None:
                while s > element.next().value():
                    element = element.next()
                    if element.next()==None:
                        break
            string = self.Node(s, element.next())
            element.set_next(string)
            self.__length += 1
            
            
    def size(self):
        """
        M??thode accesseur.
        Retourne la taille de ce classement.
        @pre:  -
        @post: Le nombre de r??sultats actuellement stock??s dans ce classement a ??t?? retourn??.
        """
        return self.__length
    
    def add(self,r):
        """
        Ajoute un r??sultat r dans ce classement.
        @pre:  r est une instance de la classe Resultat
        @post: Le r??sultat r a ??t?? ins??r?? selon l'ordre du classement.
               En cas d'ex-aequo, r est ins??r?? apr??s les autres r??sultats de m??me ordre.
        """
        self.board.insert(r)
        
    def __str__(self):
        """
        Retourne le r??sultat d'un coureur donn??.
        @pre c est un Coureur
        @post retourne le premier (meilleur) Resultat r du coureur c dans le
              classement. Retourne None si le coureur ne figure pas (encore)
              dans le classement.
        """
        return self.c.__str__()

    ##############
    # Node class #
    ##############

    class Node:

        def __init__(self, cargo=None, next=None):
            """
            Initialises a new Node object.
            @pre:  -
            @post: A new Node object has been initialised.
                   A node can contain a cargo and a reference to another node.
                   If none of these are given, the node is initialised with
                   empty cargo (None) and no reference (None).
            """
            self.__cargo = cargo
            self.__next  = next

        def value(self):
            """
            Returns the value of the cargo contained in this node.
            @pre:  -
            @post: Returns the value of the cargo contained in this node, 
                   or None if no cargo  was put there.
            """
            return self.__cargo

        def next(self):
            """
            Returns the next node to which this node links.
            @pre:  -
            @post: Returns the node to which this node is linked with its 
                   next pointer, or None if that pointer is None.
            """
            return self.__next

        def set_next(self,node):
            """
            Sets the next node to which this node links to a new node.
            @pre:  -
            @post: The node to which this node is linked next, 
                has been set to the new node passed as parameter.
                   Can also be set to None by passing None as parameter.
            """
            self.__next = node

        def __str__(self):
            """
            Returns a string representation of the cargo of this node.
            @pre:  self is a (possibly empty) Node object.
            @post: Returns a print representation of the cargo contained in this Node.
            """
            return str(self.value())

        def __eq__(self,other):
            """
            Comparator to compare two Node objects by their cargo. 
            """
            if other is not None :
                return self.value() == other.value()
            else :
                return False

        def print_list(self):
            """
            Prints the cargo of this node and then recursively of each node connected to this one.
            @pre:  self is a node (possibly connected to a next node).
            @post: Has printed a space-separated list of the form "a b c ... ",
                   where "a" is the string-representation of this node,
                   "b" is the string-representation of my next node, and so on.
                   A space is printed in-between the printed value.
            """
            head = self
            tail = self.__next       # go to my next node
            if tail is not None :    # as long as the end of the list has not been reached
                print(head, end=" ") # print my head 
                tail.print_list()    # recursively print remainder of the list
            else :                   # print the last element
                print(head, end=" ")

        def print_backward(self):
            """
            Recursively prints the cargo of each node connected to this node (in opposite order),
            and then prints the cargo of this node as last value.
            @pre:  self is a node (possibly connected to a next node).
            @post: Has printed a space-separated list of the form "... c b a",
                   where a is my cargo (self), b is the cargo of the next node, and so on.
                   The nodes are printed in opposite order: the last nodes' value is printed first.
            """
            head = self
            tail = self.__next        # go to my next node
            if tail is not None :     # as long as the end of the list has not been reached
                tail.print_backward() # recursively print remainder of the list backwards
            print(head, end = " ")    # print my head 

        def print_avec_separateur(self, separateur):
            print("[", end=" ")
            if self.first() is not None:
                self.head.print_list_avec_separateur(separateur)
            print("]")

        def print_list_avec_separateur(self,separateur):
            head = self
            tail = self.__next      # go to my next node
            if tail is not None : # as long as the end of the list has not been reached
                print(head, end=separateur)  # print my head, with separateur 
                tail.print_list_avec_separateur(separateur) # recursively print remainder of the list
            else:                 # print the last element
                print(head, end=" ") # print my head, with a space



if __name__ == '__main__':
    o = Classement("Egg",21)
    o.insert(Resultat(Coureur("Egg", 21), Temps(12, 0, 0)))
    o.insert(Resultat(Coureur("foo", 21), Temps(11, 0, 0)))
    print(o)
    