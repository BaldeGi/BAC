class Command:
    
    command_total=0
    prix_total=0
    
    def __init__(self,id_buyer,id_item,quantity,price):
        self.id_buyer=id_buyer
        self.id_item=id_item
        self.price=price
        self.quantity=quantity
        Command.command_total+=1
        Command.prix_total+=self.get_price()
   
    def get_price(self):
        return self.price*self.quantity
    
    
    def __str__(self):
        return "{}, {} : {} * {} = {}".format(self.id_buyer,self.id_item,self.price,self.quantity,self.get_price())
    
    @classmethod
    def get_number_total_command(cls):
        return cls.command_total
    
    @classmethod
    def get_total_price(cls):
        return cls.prix_total
    
    
    
    
    
command=Command(23, 94, 72, 40)
print(command)
print()
commands=Command(5,32,10,5)
print(commands)
print()
print(Command.get_total_price())
print()
print(Command. get_number_total_command())
        
    