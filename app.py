from flask import Flask, render_template, make_response , jsonify, request, url_for, json
from nltk_main import click_event_processing2
from owlready2 import *
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/slownik_info')
def slownik_info():
    onto = get_ontology("file://D:/INZ/pizza.xml").load()
    dane1 = list(onto.classes())
    dane2 = [str(i) for i in dane1]
    return jsonify(res = dane2)

# funkcja wywolywana po kliknieciu  i zwracajaca synonim klikneitego slowa
# oraz czesci mowy kliknietego zdania

@app.route('/click_event=')
def click_event():
    kursor_id = request.args.get('ID', 1, type=str)
    text = request.args.get('content', 1, type=str)
    res =  click_event_processing2(kursor_id, text)
    #word = Model().Add_Synonyms(res[0])
    #speech_part = return_speech_parts(res[1])
    #return jsonify(synonims = word, speech_parts = speech_part)

if __name__ == "__main__":
    app.run()


