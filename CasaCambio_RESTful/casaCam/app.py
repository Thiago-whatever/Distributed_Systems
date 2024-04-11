import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
modelo = pickle.load(open('modelo.pkl','rb'))

@app.route('/cambio', methods=['POST'])
def cambio():
    presentCurrency = str(request.form["presentCurrency"])
    futureCurrency = str(request.form["futureCurrency"])
    amount = int(request.form["presentAmount"])

    if(futureCurrency == "Mexico"):
        resultado = amount *2
    elif(futureCurrency == "Britain"):
        resultado = amount *0.75
    elif(futureCurrency == "Canada"):
        resultado = amount *1.5
    else:
        resultado = amount *0.3

    return render_template('index.html', cambio=resultado)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=90)