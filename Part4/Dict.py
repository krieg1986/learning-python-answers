def copyDict(dict):
    new = {}
    for x in dict.keys():
        new[x] = dict[x]
    return new

def addDict(dict1, dict2):
    new = {}
    for x in dict1.keys():
        new[x] = dict1[x]
    for x in dict2.keys():
        new[x] = dict2[x]
    return new