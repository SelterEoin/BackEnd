from owlready2 import *
onto = get_ontology("http://www.lesfleursdunormal.fr/static/_downloads/pizza_onto.owl").load()
Zmienna="Topping"
print(onto.search(iri = "*" + Zmienna))
print(onto.search(is_a = onto.Topping))