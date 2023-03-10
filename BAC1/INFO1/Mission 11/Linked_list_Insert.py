class LinkedList :

    def __init__(self):
        """
        Initialises a new linked list object.
        @pre:  -
        @post: A new empty linked list object has been initialised.
               It has 0 length, contains no nodes and the head points to None.
        """
        self.__length = 0
        self.__head = None

    def size(self):
        """
        Returns the number of nodes contained in this linked list.
        @pre:  -
        @post: Returns the number of nodes (possibly zero) contained in this linked list.
        """
        return self.__length

    def first(self):
        return self.__head

    def add(self, cargo):
        """
        Adds a new Node with given cargo to the front of this linked list.
        @pre: self is a (possibly empty) LinkedList
        @post: A new Node object is created with the given cargo.
               This new Node is added to the front of the linked list.
               The length counter has been incremented.
               The head of the list now points to this new node.
        """
        node = Node(cargo,self.__head)
        self.__head = node
        self.__length += 1

    def print(self):
        """
        Prints the contents of this linked list and its nodes.
        @pre:  self is a (possibly empty) LinkedList
        @post: Has printed a space-separated list of the form "[ a b c ... ]",
               where "a", "b", "c", ... are the string representation of each
               of the linked list's nodes.
               A space is printed after and before the opening and closing bracket,
               as well as between any two elements.
               An empty linked is printed as "[ ]"
        """
        print("[", end=" ")
        if self.__head is not None:
            self.__head.print_list()
        print("]")

    def print_backward(self):
        """
        Prints the contents of this linked list and its nodes, back to front.
        @pre:  self is a (possibly empty) LinkedList
        @post: Has printed a space-separated list of the form "[ ... c b a ]",
               where "a", "b", "c", ... are the string representation of each
               of the linked list's nodes. The nodes are printed in opposite order:
               the last nodes' value are printed first.
               A space is printed after and before the opening and closing bracket,
               as well as between any two elements.
               An empty linked is printed as "[ ]"
        """
        print("[", end=" ")
        if self.__head is not None:
            self.__head.print_backward()
        print("]")
        
    #Fonctions ajout??es   
    def insert(self,s):
        """
        @pre  s est un string ?? ins??rer dans la liste chain??e;
          self est une liste cha??n??e dont les noeuds contiennent des strings;
          les noeuds de la liste sont ordonn??es en ordre croissant selon les valeurs (strings)
          qu'ils contiennent.
        @post Un noeud contenant le String s a ??t?? ins??r?? dans la liste de fa??on
          ?? ce qu'apr??s l'insertion celle-ci soit toujours en ordre croissant.
        """
        node=self.first()
        if node==None:
            self.add(s)
        elif s<node.value():
            self.add(s)
        else:
            while node.next()!=None:
                if s<node.next().value():
                    nod=Node(s,node.next())
                    node.set_next(nod)
                    self.__length+=1
                    break
                node=node.next()
            if node.next()==None:
                nodes=Node(s,None)
                node.set_next(nodes)
                self.__length+=1
                
    #Fonctions implement??e
    def __str__(self):
        node = self.first()
        txt = "[ "
        while node != None:
            txt += str(node)+" "
            node = node.next()
        return txt+"]"
    
    
    #Fonctions Implement??e
    def remove_from_end(self):
        node=self.first()
        if self.__length==1:
            self.__head=None
            self.__length-=1
        elif node!=None:
            while node.next().next()!=None:
                node=node.next()
            node.set_next(None)
            self.__length-=1
        else:
            pass
        
    #Fonctions implement??es  
    def get_reverse(self):
        mot=""
        node=self.first()
        while node.next()!=None:
            mot+=node.value()
            node=node.next()
        mot+=node.value()
        return mot
            
                    
                    
           
           
class Node:

    def __init__(self, cargo=None, next=None):
        """
        Initialises a new Node object.
        @pre:  -
        @post: A new Node object has been initialised.
               A node can contain a cargo and a reference to another node.
               If none of these are given, a node with empty cargo (None) and no reference (None) is created.
        """
        self.__cargo = cargo
        self.__next  = next

    def value(self):
        """
        Returns the value of the cargo contained in this node.
        @pre:  -
        @post: Returns the value of the cargo contained in this node, or None if no cargo  was put there.

        """
        return self.__cargo

    def next(self):
        return self.__next

    def __str__(self):
        """
        Returns a string representation of the cargo of this node.
        @pre:  self is possibly empty Node object.
        @post: returns a print representation of the cargo contained in this Node.
        """
        return str(self.value())

    def print_list(self):
        """
        Prints the cargo of this node and then recursively of each node connected to this one.
        @pre:  self is a node (possibly connected to a next node).
        @post: Has printed a space-separated list of the form "a b c ... ",
               where "a" is the string-representation of this node,
               "b" is the string-representation of my next node, and so on.
               A space is printed after each printed value.
        """
        print(self, end=" ")   # print my head
        tail = self.__next    # go to my next node
        if tail is not None : # as long as the end of the list has not been reached
            tail.print_list() # recursively print remainder of the list

    def print_backward(self):
        """
        Recursively prints the cargo of each node connected to this node (in opposite order),
        and then prints the cargo of this node as last value.
        @pre:  self is a node (possibly connected to a next node).
        @post: Has printed a space-separated list of the form "... c b a",
               where a is my cargo (self), b is the cargo of the next node, and so on.
               The nodes are printed in opposite order: the last nodes' value is printed first.
        """
        tail = self.__next        # go to my next node
        if tail is not None :     # as long as the end of the list has not been reached
            tail.print_backward() # recursively print remainder of the list backwards
        print(self, end = " ")    # print my head
        
        
    def set_next(self,node):
        self.__next = node
        
        
        
l = LinkedList()
l2=LinkedList()
l.print()
l.print_backward()
print(l.size())
l.add(3)
l.add(2)
l.add(1)
l.print()
l.print_backward()
print(l.size())
l.insert(15)
l.insert(0)
print(l)
l.remove_from_end()
print(l)
l2.add("first")
l2.add("second")
l2.add("third")
print(l2.get_reverse())

