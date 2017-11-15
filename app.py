from flask import Flask, render_template, jsonify, request
from nltk_main import click_event_processing2
from owlready2 import *
app = Flask(__name__)
onto = get_ontology("file://D:/INZ/3w1.owl").load()
#onto = get_ontology("file://D:/INZ/pizza.xml").load()

@app.route("/")
def index():
    return render_template('index.html')

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

@app.route('/click_event=')
def click_event():
    kursor_id = request.args.get('ID', 1, type=str)
    text = request.args.get('content', 1, type=str)
    res =  click_event_processing2(kursor_id, text)
    #word = Model().Add_Synonyms(res[0])
    #speech_part = return_speech_parts(res[1])
    slowo = res[0]
    dataforword1 = list(onto.search(iri="*" + slowo))
    dataforword2 = [str(i) for i in dataforword1]
    return jsonify(dataforword=dataforword2)

if __name__ == "__main__":
    app.run()


