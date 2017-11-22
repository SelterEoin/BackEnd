from owlready2 import *
from nltk_main import OWLlist_to_NAMESlist
text="gun Rifle. xx xxx ..test1 test2 ,dos tres undo"
onto = get_ontology("file://D:/INZ/guns.owl").load()
onto_list_classes_raw=list(onto.classes())
onto_list_classes=[]
onto_list_classes=list(onto_list_classes_raw)
onto_list_individuals_raw=list(onto.individuals())
onto_list_individuals=[]
onto_list_individuals=list(onto_list_individuals_raw)
onto_list_raw=[]
onto_list_raw.extend(onto_list_classes)
onto_list_raw.extend(onto_list_individuals)
onto_list=[]
onto_list.extend(onto_list_raw)
text2 = text.replace(",", "")
text3 = text2.replace('.', '')
onto_list = [str(i) for i in onto_list]
search_all_res=(OWLlist_to_NAMESlist(onto_list))
text4=text3.split()
print(text4)
print(search_all_res)
search_all_resp2=list(set(text4).intersection(search_all_res))
response_search_all_list2=[]
response_search_all_list=[]
response_search_all_list2.extend(search_all_resp2)
response_search_all_list = [str(i) for i in response_search_all_list2]
#return jsonify(response_search_all_list=response_search_all_list2)
print(response_search_all_list2)
