borrowed_money= {}

def give_money(borrowed_money, from_person, to_person, amount):
    if (type(amount) != float and type(amount) != int)\
    or type(from_person) != str or type(to_person) != str\
    or type(borrowed_money) != dict or from_person == to_person:
        raise ValueError("mauvais arguments")
    if borrowed_money.get(from_person, -1) == -1:
        borrowed_money[from_person] = {}
        borrowed_money[from_person][to_person] = -amount
    elif borrowed_money[from_person].get(to_person, -1) == -1:
        borrowed_money[from_person][to_person] = -amount
    else:
        borrowed_money[from_person][to_person] += -amount
    if borrowed_money.get(to_person, -1) == -1:
        borrowed_money[to_person] = {}
        borrowed_money[to_person][from_person] = amount
    elif borrowed_money[to_person].get(from_person, -1) == -1:
        borrowed_money[to_person][from_person] = amount
    else:
        borrowed_money[to_person][from_person] += amount
    return borrowed_money

print(give_money(borrowed_money,"John","Paul",0.5))
print(give_money(borrowed_money,"John","Georges",12))
print(give_money(borrowed_money,"Ringo","Georges",3))
print(give_money(borrowed_money,"Paul","Ringo",0.25))
 
def total_money_borrowed(borrowed_money):
    total=0
    if type(borrowed_money)!=dict:
        raise ValueError
    for keys,values in borrowed_money.items():
        for key,amount in values.items():
            if amount>0:
                total+=amount
    return total
    
print(total_money_borrowed(borrowed_money))
