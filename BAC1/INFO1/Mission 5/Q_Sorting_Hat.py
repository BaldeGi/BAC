knowledge = [['Gryffindor', ['brave', 'strong', 'bold']],
             ['Ravenclaw', ['smart', 'wise', 'curious']],
             ['Hufflepuff', ['loyal', 'patient', 'hard-working']],
             ['Slytherin', ['cunning', 'wily', 'malignant']]]

def house_designation(student_qualities):
    liste=[['Gryffindor',0],['Ravenclaw',0],['Hufflepuff',0],['Slytherin',0]]
    liste_triee=[]
    liste_houses=[]
    for i in range(len(knowledge)):
        for k in range(len(student_qualities)):
            if student_qualities[k] in (knowledge[i][1]) :
                liste[i][1]+=1
    for i in range(len(liste)):
        liste_triee.append(liste[i][1])
    for i in range(len(liste_triee)):
        maximum_qualities=max(liste_triee)
        for j in range(len(liste)):
            if liste[j][1]==maximum_qualities:
                if liste[j][0] not in liste_houses:
                    liste_houses.append(liste[j][0])
        liste_triee.remove(maximum_qualities)
    return liste_houses
       
print((house_designation(['patient','brave','smart','loyal','cunning', 'bold', 'wily'])))




