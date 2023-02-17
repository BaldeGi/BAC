def line_count(filename):
    """
    retourne, pour le nom dun fichier donné,
    le nombre de lignes dans le fichier.
    """
    with open("filename.txt","r") as file:
        lines=0
        for line in file.readlines():
            lines+=1
        return lines
print(line_count("filename.txt"))



def char_count(filename):
    """
    retourne, pour le nom d'un fichier donné,
    le nombre de caractères dans le fichier.
    """
    with open("filename.txt","r") as file:
        l=file.read()
    return (len(l))
            
print(char_count("filename.txt"))
        
        
def space(filenames,n):
    """
     crée un nouveau fichier filename
     qui se compose seulement de n espaces.
    """
    with open(filenames,"w") as file:
        l=file.write(" "*n)
        return l
print(space("filenames.txt",4))


def capitalize(filename_in,filename_out):
    """
    crée, pour le fichier filename_in, un nouveau fichier filename_out,
    dans lequel tous les caractères sont en majuscule.
    """
    with open("filename_in.txt","r") as file:
        with open("filename_out.txt","w") as file2:
            file2.write(file.read().upper())
            
    
print(capitalize("filename_in.txt","filename_out.txt"))





