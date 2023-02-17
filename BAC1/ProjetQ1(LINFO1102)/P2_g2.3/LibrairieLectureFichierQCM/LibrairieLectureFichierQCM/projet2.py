import qcm
from random import*

score=0
nombre_de_questions=0

reponse = []

if __name__ == '__main__':
    filename = "QCM.txt"
    
    questions = qcm.build_questionnaire(filename)
    
    #mettre les réponse dans un ordre aléatiore
    def melange_list(questions):
        questions3 = []
    
        while len(questions) != 0:
            r = randint(0,len(questions)-1)
            questions3.append (questions[r])
            questions.remove(questions[r])
        return questions3
    #fin fonction
    
    list3 = []
    for i in range(0,len(questions)):
        list4 = (melange_list(questions[i][1]))
        questions[i][1] = list4

    #pose les question
    for q in range(len(questions)) :
        print()
        print("\tQuestion " + str(q+1) + ": \"" + questions[q][0] + "\"")
        for r in range(len(questions[q][1])) :
        #affichage des reponse
            print("\t\t\tRéponse: \"" + questions[q][1][r][0] + "\"")
        #repondre a la question
        g = int(input("\t\tQuel est la bonne réponse ?(entrer 4 pour ne rien répondre)"))
        if g > 4 or g < 1:
            while g > 4 or g < 1:
                print("cette réponse n'existe pas")
                g = int(input("\t\tQuel est la bonne réponse ?(entrer 4 pour ne rien répondre)"))
        for a in range(len(questions[q])):
            if g == 1 :
                g = questions[q][1][a][1]
                reponse.append(g)
            elif g ==2 :
                g = questions[q][1][a+1][1]
                reponse.append(g)
            elif g == 3 :
                g = questions[q][1][a+2][1]
                reponse.append(g)
            elif g == 4 :
                g = ""
                reponse.append(g)
        print(reponse)
        #variable pour faire la cotation    
        o = 0
        j = 0
        t = 0
        p = 0
        choix_mode = 0
        choix_mode = int(input("\t\tQuel mode de cotation (1 = facile, 2 = difficile, 3 = anti=aléatoire, 4 = comparatif)"))
        while choix_mode > 4 or choix_mode < 0 :
            if choix_mode == 1 :
                for c in range(len(reponse)) :
                    if reponse[c] == False:
                        o += 0
                    elif reponse[c] == True:
                        o += 1
                    else :
                        o += 0
            elif choix_mode == 2 :
                for d in range(len(reponse)) :
                    if reponse[c] == "False":
                        o -= 1
                    elif reponse[c] == "True":
                        o += 1
                    else :
                        o += 0
            elif choix_mode == 3:
                for d in range(len(reponse)) :
                    if reponse[c] == "False":
                        o -= 1
                    elif reponse[c] == "True":
                        o += 1
                    else :
                        o += 0
            