l = [{"City": "Bruxelles", "Country": "Belgium"}, \
    {"City": "Berlin", "Country": "Germany"}, \
    {"City": "Paris", "Country": "France"}]
def get_country(l, name):
    for i in l:
        if i["City"]==name:
            return i["Country"]
    return False
print(get_country(l, "Berlin"))