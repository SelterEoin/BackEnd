"""from owlready2 import *
onto = get_ontology("file://D:/INZ/3w1.owl").load()
zmienna=input()
#print(onto.search(subclass_of= onto.gun))
kod = "onto.search(is_a= onto." + zmienna + ")"
wynik=(eval(kod))
print(wynik)
#print(onto.search(is_a= onto.gun))
#print(list((onto.search(is_a= onto.Zmienna))))"""

def kropka_na_przecinek(text):
    new_list = []
    res = []
    for word in text:
        word = [l for l in word]
        for l in range(len(word)):
            if word[l] == '.':
                word[l] = ','
        word = ''.join(word)
        word = word.split(',')
        new_list.append(word)
        for i in new_list:
            for j in i:
                res.append(j)
    return res

def SplitLIST_to_TEXT(text):
    new_list = []
    res = []
    for word in text:
        word = [l for l in word]
        for l in range(len(word)):
            if word[l] == "'":
                word[l] = ' '
        word = ''.join(word)
        word = word.split(',')
        new_list.append(word)
        for i in new_list:
            for j in i:
                res.append(j)
    return res

text = ['3w1.Magnum', '3w1.calliber', '3w1.44']
print(SplitLIST_to_TEXT(text))