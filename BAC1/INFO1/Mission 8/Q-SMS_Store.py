class SMSStore:
    def __init__(self):
        self.my_inbox=[]

    def add_new_arrival(self,from_number,time_arrived,text_of_SMS):
        self.my_inbox.append((False,from_number,time_arrived,text_of_SMS))
        return self.my_inbox
        
    def message_count(self):
        return len(self.my_inbox)
    
    def get_unread_indexes(self):
        unread_indexes=[]
        for i in range(len(self.my_inbox)):
            if self.my_inbox[i][0]==False:
                unread_indexes.append(i)
        return unread_indexes
    
    def get_message(self,i):
        if self.my_inbox==[] or len(self.my_inbox)<=i:
            return None
        if self.my_inbox[i][0]==False:
            self.my_inbox[i]=(True,self.my_inbox[i][1],self.my_inbox[i][2],self.my_inbox[i][3])
        return self.my_inbox[i][1:]
    
    def delete(self,i):
        del self.my_inbox[i]
        
    def clear(self):
        del self.my_inbox[:]
     
my_inbox=SMSStore()
print(my_inbox.add_new_arrival(12, 11, "Salut ça va"))
print(my_inbox.message_count())
print(my_inbox.get_unread_indexes())
print(my_inbox.get_message(1))
print(my_inbox.delete(0))




