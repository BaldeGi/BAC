def portrait(right_password, entered_password):
    if len(right_password)==len(entered_password):
        l=[]
        for i in range(len(right_password)):
            if right_password[i]==entered_password[i]:
                l.append(right_password[i])
            
        if len(l)==len(right_password):
            return True
        else:
            return False
    else:
        return False
    
           
    
print(portrait("wTyPnVUYvJ", "wTyPnVUYvJ"))