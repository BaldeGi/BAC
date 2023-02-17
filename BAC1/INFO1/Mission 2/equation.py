"""solutions = 0
a = int(input("Entrez la valeur du coefficient a : "))
b = int(input("Entrez la valeur du coefficient b : "))
c = int(input("Entrez la valeur du coefficient c : "))
max = int(input("Entrez la valeur maximale pour x et y : "))

for x in range(1,max):
    for y in range(1,max):
        for z in range(1,max):
            if x**a+y**b == z**c:
                print("x =", x, " y =", y , "z =" , z)
                solutions += 1
                
if solutions == 0:
    print("Aucune solution trouvee")
else:
    print(solutions, "solutions trouvees")"""

"""a=15
b=30
while(a%b):
    r=a%b
    a=b
    b=r
print(b)"""


actual_speed=60
authorized_speed=50
interval=actual_speed-authorized_speed
if actual_speed<=authorized_speed:
    amende=0
    print( amende)
elif interval>10:
    amende=interval*5*2
    print( amende)
elif 1<=interval<=2:
    amende=12.5
    print( amende)
elif interval<=10:
    amende=interval*5
    print( amende)

        
    

    
    
    
















                    
                    
                
                    
            