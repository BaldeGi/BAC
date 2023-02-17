class LinkedList :

    def __init__(self):
        self.__length = 0
        self.__head = None


    def first(self):
        return self.__head

    def add(self, cargo):
        node = Node(cargo,self.__head)
        self.__head = node
        self.__length += 1

    def print(self):
        print("[", end=" ")
        if self.__head is not None:
            self.__head.print_list()
        print("]")

   
    def insert(self,s):
        node=self.first()
        string = Node(s,self)
        node.set_text(string)
    
   
        
                
           
class Node:

    def __init__(self, cargo=None, next=None):

        self.__cargo = cargo
        self.__next  = next

    def value(self):
        return self.__cargo

    def next(self):
        return self.__next

    def __str__(self):
        return str(self.value())

    def print_list(self):
        print(self, end=" ")  
        tail = self.__next    
        if tail is not None : 
            tail.print_list()
            
    def get_text(self):
        return str(self.value())
        
    def set_text(self,node):
        self.__next = node


        
if __name__ == '__main__':
    l = LinkedList()
    l.add("first")
    l.add("second")
    l.add("third")
    print(l.insert("fifth"))
    print(l.first())
    
        
            
            
            