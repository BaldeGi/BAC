def treatment(data) :
    data=data.split()
    count=0
    string=""
    first=data[0]
    i=0
    while i<len(data):
        if data[i]==first:
            count+=1
            i+=1
        elif data[i]!=first:
            string+=first+"*"+str(count)+" "
            first=data[i]
            count=0
            i=i
    string+=first+"*"+str(count)
    return string
    

