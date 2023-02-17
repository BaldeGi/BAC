def write(letter_template, name):
    try:
        with open(letter_template,"r") as file:
            string=file.read().replace("#",name)
            
        with open(letter_template,"w") as fiche:
            fiche.write(string)
        
    except OSError:
        return -1
    
    
print(write("admission.txt", "Lamarana"))