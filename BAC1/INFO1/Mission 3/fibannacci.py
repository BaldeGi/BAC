"""def fibonacci(n):
    i=2
    a=0
    b=1
    n=0
    if n==0:
        print(0)
    elif n==1:
        print(1)
    else:
        while i <=n:
            c=a+b
            a=b
            b=c
            i+=1
        print(c)
    fibonacci(10)"""
    
        
    
def chiffres_pairs(n):
    count=0
    string=str(n)
    for i in string:
        count+=1
    if count%2==0:
        return True
    else:
        return False
    
    

def operations(n):
    for i in range(1,n+1):
        if chiffres_pairs(i):
            print("pair")
        else:
            print("impair")
        
operations(10)
    
    
    
    