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

    
    
        
            
    def get_reverse(self):
        "Retourne la liste dans le sens inverse"
        node = self.first()
        txt=""
        while node != None:
            txt += str(node.get_value())+""
            node = node.get_next()
        return txt
    
    
  
                
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

    def get_value(self):
        """
        Returns the value of the cargo contained in this node.
        @pre:  -
        @post: Returns the value of the cargo contained in this node, or None if no cargo  was put there.

        """
        return self.__cargo

    def get_next(self):
        return self.__next

    
   
        
if __name__ == '__main__':
    l = LinkedList()
    l.add("first")
    l.add("second")
    l.add("third")
    print(l.get_reverse())
        
            
            
            
            
            
        