from flask import Flask, render_template, jsonify, request
from nltk_main import click_event_processing2
from owlready2 import *
from nltk_main import delete_stopwords_for_one_word,OWLlist_to_NAMESlist
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/OWL_DATA_LIB_button1")
def OWL_DATA_LIB_button1():
    global onto
    onto = get_ontology("file://D:/INZ/places.owl").load()

@app.route("/OWL_DATA_LIB_button2")
def OWL_DATA_LIB_button2():
    global onto
    onto = get_ontology("file://D:/INZ/guns.owl").load()

@app.route("/OWL_DATA_LIB_button3")
def OWL_DATA_LIB_button3():
    global onto
    onto = get_ontology("file://D:/INZ/people.owl").load()

@app.route('/OWL_DATA_CLASSES')
def OWL_DATA_CLASSES():
    data1 = list(onto.classes())
    data2 = [str(i) for i in data1]
    return jsonify(dataCLASSESback = data2)

@app.route('/OWL_DATA_INDIVIDUALS')
def OWL_DATA_INDIVIDUALS():
    data1 = list(onto.individuals())
    data2 = [str(i) for i in data1]
    return jsonify(dataINDIback = data2)

@app.route('/OWL_DATA_OBJECT_PROPERTIES')
def OWL_DATA_OBJECT_PROPERTIES():
    data1 = list(onto.object_properties())
    data2 = [str(i) for i in data1]
    return jsonify(dataPROPERTIESback = data2)

# funkcja wywolywana po kliknieciu  i zwracajaca synonim klikneitego slowa
# oraz czesci mowy kliknietego zdania

@app.route('/one_word')
def one_word():
    #kursor id oraz text jest wysyłany przez front tak by wydobyc z tekstu klikniete slowo
    kursor_id = request.args.get('ID', 1, type=str)
    text = request.args.get('content', 1, type=str)
    res =  click_event_processing2(kursor_id, text)
    #click zwraca zdanie i slowo , klikniete slowo jest pod res[0]
    slowo = res[0]
    #usuwamy , oraz . z kliknietego slowa
    slowo = delete_stopwords_for_one_word(slowo)
    #budujemy sobie listy classes oraz instancje i dodajemy je do siebie
    onto_list_classes_raw = list(onto.classes())
    onto_list_classes = list(onto_list_classes_raw)
    onto_list_individuals_raw = list(onto.individuals())
    onto_list_individuals = list(onto_list_individuals_raw)
    onto_list_raw = []
    onto_list_raw.extend(onto_list_classes)
    onto_list_raw.extend(onto_list_individuals)
    onto_list = []
    onto_list.extend(onto_list_raw)
    #przerabiamy kazdy elemnent w liście na stringa
    onto_list = [str(i) for i in onto_list]
    #przerabiamy onto_list na nazwy czyli z [guns.bow] na [bow]
    one_word_resp =(OWLlist_to_NAMESlist(onto_list))
    #DLA KAZDEGO ELEMENTU W LISCIE onto_word_resp
    #is_a szuka pod class danego elementu
    #wywołujemy IS_A_LIST=(eval("onto.search(is_a= onto." + onto_word_resp[i] + ")")) czyli
    #przypisujemy wynik czyli liste do IS_A_LIST z metody szukania po danym elemencie z onto_word_resp
    #nastepnie dla listy IS_A_LIST wywołujemy (OWLlist_to_NAMESlist(IS_A_LIST) i przypisujemy do np listX
    #nastpenie przechodzimy po kazdym elemencie listy listX i jeżeli jakiś element jest taki sam co słowo to dopisujemy element i po ktorym szukalismy
    #z one_word_resp do listy one_word_list2
    #i tak w kółko aż przejdzie przez wszykie elementy onto_word_resp
    #poźniej dodajemy wywowałnie na słowie metoda is_a jako lista IS_A_LIST2 do one_word_list2
    #poźniej usuwamy powtorzenia z one_word_list2 przez set i przerabimy na jej elementy na string
    #oraz uzywamy jsonify zeby zwrocic liste do Fronendu
    # front musi dostac response pod nazwa one_word_list
    # pseudo kod pod ponizej HELP !
""""
    for i in one_word_resp:
        IS_A_LIST=(eval("onto.search(is_a= onto." + one_word_resp[i] + ")"))
        listX =(OWLlist_to_NAMESlist(IS_A_LIST))
        for j in listX:
            if listX[j]==slowo:
                one_word_list2.extend(one_word_resp[i])
            else: sprawdz inne j z listX
    IS_A_LIST2=(eval("onto.search(is_a= onto." + slowo + ")"))
    one_word_list2.extend(IS_A_LIST2)
    one_word_list2=set(one_word_list2)
    one_word_list2 = [str(i) for i in one_word_list]
    return jsonify(one_word_list=one_word_list2)
"""

@app.route('/search_all')
def search_all():
    text = request.args.get('content', 0, type=str)
    text2 = text.replace(",", "")
    text3 = text2.replace('.', '')
    text4 = text3.split()
    onto_list_classes_raw = list(onto.classes())
    onto_list_classes = list(onto_list_classes_raw)
    onto_list_individuals_raw = list(onto.individuals())
    onto_list_individuals = list(onto_list_individuals_raw)
    onto_list_raw = []
    onto_list_raw.extend(onto_list_classes)
    onto_list_raw.extend(onto_list_individuals)
    onto_list = []
    onto_list.extend(onto_list_raw)
    onto_list = [str(i) for i in onto_list]
    search_all_resp = (OWLlist_to_NAMESlist(onto_list))
    search_all_resp2 = list(set(text4).intersection(search_all_resp))
    response_search_all_list2 = []
    response_search_all_list2.extend(search_all_resp2)
    response_search_all_list2 = [str(i) for i in response_search_all_list2]
    return jsonify(response_search_all_list=response_search_all_list2)

if __name__ == "__main__":
    app.run()


