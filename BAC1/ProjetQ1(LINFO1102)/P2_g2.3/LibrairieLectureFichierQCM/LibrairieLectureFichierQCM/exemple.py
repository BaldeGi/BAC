import qcm

"""
    Exemple d'utilisation de la librairie de lecture de fichiers QCM
"""


if __name__ == '__main__':
    filename = "QCM.txt"

    # Chargement du questionnaire
    questions = qcm.build_questionnaire(filename)
     #pose les question
    reponse=[]
    note=0
    mod_choice=0
    mod_choice=int(input("Votre mode (1=facile)"))
    for q in range(len(questions)) :
        print()
        print("\tQuestion " + str(q+1) + ": \"" + questions[q][0] + "\"")
        for r in range(len(questions[q][1])) :
        #affichage des reponse
            print("\t\t\tRéponse: \"" + questions[q][1][r][0] + "\"")
        g = int(input("\t\tQuel est la bonne réponse ?(entrer 4 pour ne rien répondre)"))
        if g > 4 or g < 1:
            while g > 4 or g < 1:
                print("cette réponse n'existe pas")
                g = int(input("\t\tQuel est la bonne réponse ?(entrer 4 pour ne rien répondre)"))
        for a in range(len(questions[q])):
            if g == 1 :
                g = questions[q][1][a][1]
                reponse.append(g)
                print(reponse)
            elif g ==2 :
                g = questions[q][1][a+1][1]
                reponse.append(g)
                print(reponse)
            elif g == 3 :
                g = questions[q][1][a+2][1]
                reponse.append(g)
                print(reponse)
            elif g == 4 :
                g = ""
                reponse.append(g)
                print(reponse)
        for c in range (len(reponse)):
            if reponse[c]=="True":
                note+=1
                print(note)
            else:
                note+=0
                print(note)
      
        
            
            

       
    
    

    
    
    

















    
    