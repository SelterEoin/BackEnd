from owlready2 import *
slowo="rifle"
onto = get_ontology("file://D:/INZ/guns.owl").load()
onto_list_classes_raw=list(onto.classes())
onto_list_classes=[]
onto_list_classes=list(onto_list_classes_raw)
onto_list_individuals_raw=list(onto.individuals())
onto_list_individuals=[]
onto_list_individuals=list(onto_list_individuals_raw)
onto_list=[]
onto_list.extend(onto_list_classes)
onto_list.extend(onto_list_individuals)
print(onto_list)
one_word_list=[]

for i in onto_list_classes:
    IS_A_LIST=(eval("onto.search(is_a= onto." + onto_list_classes(i) + ")"))
    for j in IS_A_LIST:
        if IS_A_LIST(j)==slowo:
             one_word_list.append(IS_A_LIST)
one_word_list=set(one_word_list)


