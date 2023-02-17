lan={'test': 'prueba', 'i': 'yo', 'you': 'te', 
'elephant': 'elefante', 'this': 'esta', 'is': 'es',
 'a': 'un', 'shot': 'disparo', 'an': 'un', 'in': 'en',
  'my': 'mi', 'pajama': 'pijama'}


def translate(data,lan):
    data=data.lower().split(" ")
    traduction=""
    for i in data:
        if i in lan:
            traduction+=lan[i]
            traduction+=" "
        else:
            traduction+=i
            traduction+=" "
    return traduction.strip()
print(translate("This is a shame",lan))