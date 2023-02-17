def prime(n):
    count=0
    for i in range(2,n):
        if n%i==0:
            count+=1
    if count==0:
        return n
    else:
        return 0
      


def primes(maximum):
    l=[]
    for i in range(2,maximum+1):
        if prime(i)!=0:
            l.append(i)
    print(l)
    
(primes(18))