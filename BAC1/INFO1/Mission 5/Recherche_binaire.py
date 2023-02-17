def binary_search (course, list_of_courses ):
    first = 0
    last = len(list_of_courses)-1
    found = False
    liste_etudiant=[]
    index=1
    while first<=last and not found:
        middle = (first + last)//2
        if list_of_courses[middle][index-1] == course:
            found = True
            liste_etudiant=list_of_courses[middle][index]
        else:
            if course < list_of_courses[middle][index-1]:
                last = middle-1
            else:
                first = middle+1
        
    return liste_etudiant 

print(binary_search ("LINFO1112",[('LINFO1101', ['Jean', 'Pierre']),('LINFO1110', ['Jean']), ('LINFO1111', ['Jean']), ('LINFO1112', ['Jacques', 'Pierre']), ('LINFO1113', ['Pierre'])]))







