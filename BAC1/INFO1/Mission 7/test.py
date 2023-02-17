import search
def test_readfile():
    assert search.readfile("filename.txt")==['Pour reussir , il faut travailler!',"N'est-ce pas en travaillant que tu deviennes plus fort?"]
    assert search.readfile("file.txt")==["THREEPIO\tDid you hear that?  They've shut down the main reactor.", "THREEPIO\tWe're doomed!"]                                

def test_get_words():
    assert search.get_words("Pour réussir , il faut travailler!!!!")==["pour","réussir","il","faut","travailler"]
    assert search.get_words("Turmoil has engulfed the Galactic.")==["turmoil", "has", "engulfed", "the", "galactic"]
    
def test_create_index():
    assert search.create_index("file.txt")=={'threepio': {0: 1, 1: 1}, 'did': {0: 1}, 'you': {0: 1}, 'hear': {0: 1}, 'that': {0: 1}, 'theyve': {0: 1}, 'shut': {0: 1}, 'down': {0: 1}, 'the': {0: 1}, 'main': {0: 1}, 'reactor': {0: 1}, 'were': {1: 1}, 'doomed': {1: 1}}
    assert search.create_index("filename.txt")=={'pour': {0: 1}, 'reussir': {0: 1}, 'il': {0: 1}, 'faut': {0: 1}, 'travailler': {0: 1}, 'nest-ce': {1: 1}, 'pas': {1: 1}, 'en': {1: 1}, 'travaillant': {1: 1}, 'que': {1: 1}, 'tu': {1: 1}, 'deviennes': {1: 1}, 'plus': {1: 1}, 'fort': {1: 1}}
    
def test_get_lines():
    assert search.get_lines(["pour","faut"],"filename.txt")==[0]
    assert search.get_lines(["threepio","you","the","did"],"file.txt")==[0]
    
test_get_lines()    
test_create_index()  
test_readfile()   
test_get_words()


