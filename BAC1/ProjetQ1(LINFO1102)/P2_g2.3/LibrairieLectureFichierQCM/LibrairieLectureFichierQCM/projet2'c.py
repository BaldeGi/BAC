import qcm
import ast
from random import*



choix_mode = 0
list = ["1","2","3","4"]
list2 = []
score2 = 0
reponse = []
moyenne = 0
p = 0
list_phrase = ["NON !!! je refuse.","essayez encore ;)","vous êtes vachement tétus vous !!!","pfff","allez je vous aide, la réponse est 10/10","vous le faites exprès??","ne m'obligez pas a répondre à votre place"]



    #mettre les réponse dans un ordre aléatiore

def melange_list(questions):
    questions3 = []
    
    while len(questions) != 0:
        r = randint(0,len(questions)-1)
        questions3.append (questions[r])
        questions.remove(questions[r])
    return questions3
    #fin fonction

def clear():
    for s in range(100):
        print("\n")

clear()
nom_utilisateur = input("quel est votre nom d'utilisateur ? : ")

clear()
choix_QCM = int(input("\nquel QCM voulez vous ? : "))
if choix_QCM == 1:
    filename = "QCM.txt"
    
if choix_QCM == 2:
    filename = "QCM2.txt"
    
if choix_QCM == 3:
    filename = "QCM3.txt"
questions = qcm.build_questionnaire(filename)

while list.count(choix_mode) == 0 :
    clear()
    print("\nchoisissez votre mode : ")
    print("\n1 = facile")
    print("2 = difficile")
    print("3 = anti-aléatoire")
    print("4 = comparatif")
    choix_mode = input("\nréponse : ")
    
    if list.count(choix_mode) == 0 :
        print("réponse non valide, esseyez encore")
choix_mode = int(choix_mode)

for i in range(0,len(questions)):
    list4 = (melange_list(questions[i][1]))
    questions[i][1] = list4

    #pose les question
for q in range(len(questions)) :
    clear()
    list2 = []
    print("\nQuestion ",str(q+1),":  ",questions[q][0],"\n")
    for r in range(len(questions[q][1])) :
        #affichage des reponse
        print("\t", str(r+1), ": ", questions[q][1][r][0],)
        #repondre a la question
    print("\t",str(len(questions[q][1])+1) ,":  je ne sais pas")
    g = input("\nréponse = ")
    for i in range(len(questions[q][1])+1):
        i = str(i+1)
        list2.append(i)
    while list2.count(g) == 0 :
        print("cette réponse n'existe pas")
        g = input("réponse = ")
        
    g = int(g)
    while choix_QCM == 3 and q == 2 and questions[q][1][g-1][1] != True:
        if p > len(list_phrase):
            p = 0
        print("\n",list_phrase[p],"\n")
        g = input("réponse = ")
        g = int(g)
        p += 1
        
    c = int(g)
    if c != len(questions[q][1])+1:
        a = questions[q][1][c-1][1]
    else:
        a = []
    reponse.append(a)
    


if choix_mode == 1 :
    score = reponse.count(True)
    
elif choix_mode == 2 :
    score = reponse.count(True)
    scoref = reponse.count(False)
    score -= scoref
    if score < 0:
        score = 0
    
elif choix_mode == 3:
    hasard = []
    for q in range(len(questions)) :    
        hasard.append((len(questions[q][1])))
    score = reponse.count(True)
    reponse2= reponse[:]
    hasard2 = hasard[:]
    while reponse2.count(False)!= 0:
        a = reponse2.index(False)
        score -=1/hasard2[a]
        hasard2.remove(hasard2[a])
        reponse2.remove(reponse2[a])
    if score < 0:
        score=0
    score = round(score,1) 
    if score*10%10 == 0:
        score = int(score)
    
elif choix_mode == 4:
    score = reponse.count(True)
    scoref = reponse.count(False)
    score2 = score - scoref
    if score2 < 0:
        score2 = 0
    
    hasard = []
    for q in range(len(questions)) :    
        hasard.append((len(questions[q][1])))
    score3 = reponse.count(True)
    reponse2= reponse[:]
    hasard2 = hasard[:]
    while reponse2.count(False)!= 0:
        a = reponse2.index(False)
        score3 -=1/hasard2[a]
        hasard2.remove(hasard2[a])
        reponse2.remove(reponse2[a])
    if score3 < 0:
        score3=0
    score3 = round(score3,1) 
    if score3*10%10 == 0:
        score3 = int(score3)
    
clear()

if choix_mode == 1:
    print("vous avez fait :",score,"/",len(questions),"en mode facile")
    score = score/len(questions)
    
if choix_mode == 2:
    print("vous avez fait :",score,"/",len(questions),"en mode difficile")
    score = score/len(questions)
    
if choix_mode == 3:
    print("vous avez fait :",score,"/",len(questions),"en mode aléatoire")
    score = score/len(questions)

    
if choix_mode == 4:
    print("vous avez fait :",score,"/",len(questions),"en mode facile\n")
    print("vous avez fait :",score2,"/",len(questions),"en mode difficile\n")
    print("vous avez fait :",score3,"/",len(questions),"en mode aléatoire\n")
    score = score/len(questions)

f = open("enregistrement.py", "r")

matrix = []
donnee = []
caractere = ''

lines = f.readline()
matrix = ast.literal_eval(lines)
f.close()


for i in range(len(matrix)):
    if matrix[i].count(nom_utilisateur):
        matrix[i].append(score)
        for j in range(len(matrix[i])-1):
            moyenne += matrix[i][j+1]
        moyenne = moyenne/(len(matrix[i])-1)*10
        moyenne = round(moyenne,1)
        print("\nutilisateur",matrix[i][0],", vous avez une moyenne de ",moyenne,"/10\n")
        if 0 <= moyenne <= 3:
            print("j'en connais un qui n'a pas étudié")
        if 3 < moyenne <= 5:
            print("c'est pas follichon tout ça")
        if 5 < moyenne <= 7:
            print("y a pas de quoi etre fier hein")
        if 7 < moyenne <= 10:
            print("bravo !!!")
        break
    elif i == len(matrix)-1:
        matrix.append([nom_utilisateur])
        matrix[len(matrix)-1].append(score)



f = open("enregistrement.py", "w")

matrix2 = str(matrix)
f.write(matrix2)
element = ""
f.close()