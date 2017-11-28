from owlready2 import *
import rdflib
g=rdflib.Graph()
g.load('https://protege.stanford.edu/ontologies/pizza/pizza.owl')
r = list(graph.query("""SELECT o?,?v,?p WHERE {
  o? v? ?p.
}"""))
 print(r)