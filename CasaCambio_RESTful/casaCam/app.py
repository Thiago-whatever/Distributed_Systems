import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
modelo = pickle.load(open('modelo.pkl','rb'))

@app.route('/exchange', methods=['GET'])
def exchange():
    presentCurrency = str(request.args["currency1"])
    futureCurrency = str(request.args["currency2"])
    amount = int(request.args["presentAmount"])

    exchange_rates_USD = {
        "USA": 1.0,
        "Mexico": 16.0,
        "Britain": 0.8,
        "Canada": 1.38
    }

    if(presentCurrency == "USA"):
        resultado = amount * exchange_rates_USD[futureCurrency]
    else:
        presentCurrencyUSD = amount / exchange_rates_USD[presentCurrency]
        resultado = presentCurrencyUSD * exchange_rates_USD[futureCurrency]

    return str(resultado)

@app.route('/cambio', methods=['POST'])
def cambio():
    presentCurrency = str(request.form["presentCurrency"])
    futureCurrency = str(request.form["futureCurrency"])
    amount = int(request.form["presentAmount"])

    exchange_rates_USD = {
        "USA": 1.0,
        "Mexico": 16.0,
        "Britain": 0.8,
        "Canada": 1.38
    }

    if(presentCurrency == "USA"):
        resultado = amount * exchange_rates_USD[futureCurrency]
    else:
        presentCurrencyUSD = amount / exchange_rates_USD[presentCurrency]
        resultado = presentCurrencyUSD * exchange_rates_USD[futureCurrency]
    

    return render_template('index.html', newAmount=resultado,
                           presentCurrency=presentCurrency,
                           futureCurrency=futureCurrency,
                           presentAmount=amount)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=90)