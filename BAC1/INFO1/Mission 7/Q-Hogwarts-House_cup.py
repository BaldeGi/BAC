students = {'gryffindor': ['Harry', 'Hermione', 'Ron', 'Ginny', 'Fred', ' Georges', 'Neville'],
            'ravenclaw': ['Cho', 'Luna', 'Sybill', 'Marcus', 'Marietta', 'Terry', 'Penelope'],
            'hufflepuff': ['Pomona', 'Zacharias', 'Teddy', 'Cedric', 'Nymphadora', 'Newton', 'Justin'],
            'slytherin': ['Malfoy', 'Severus', 'Dolores', 'Horace', 'Blaise', 'Pansy', 'Bellatrix']}

def winning_house(scroll):
    d={'gryffindor': 0,'ravenclaw': 0,'hufflepuff' :0 ,'slytherin': 0}
    l,resultats=[],[]
    try:
        with open(scroll,"r") as file:
            lst=file.readlines()
        for i in range(len(lst)):
            lst[i]=lst[i].strip().split()
        for i in lst:
            for k,v in students.items():
                if i[0] in v:
                    d[k]+=int(i[1])
        for i in d:
            l.append(d[i])
        l.sort(reverse=True)
        for j in d:
            if max(l)==d[j] and j not in resultats:
                    resultats.append(j)
        if len(resultats)>1:
            return resultats
        return resultats[0]
    except OSError:
        raise OSError()
    except KeyError:
        raise KeyError()

print(winning_house("cup.txt"))


