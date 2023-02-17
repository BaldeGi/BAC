def merge(first_list,second_list):
    l=[]
    liste_triee=[]
    index=1
    index_name=0
    for i in range(len(first_list)):
        l.append(first_list[i][index])
    for i in range(len(second_list)):
        l.append(second_list[i][index])
    l.sort()
    for i in l:
        for j in range(len(first_list)):
            if first_list[j] not in liste_triee:
                if first_list[j][index]==i:
                    liste_triee.append(first_list[j])
        for j in range(len(second_list)):
            if second_list[j] not in liste_triee:
                if second_list[j][index]==i:
                    liste_triee.append(second_list[j])
    return liste_triee
            
    
print(merge([["kAm",22],["olivier",20],["kim",2],["kim",2]],[["kim",22],["olivia",200],["Daby",15],["OUs",1]]))