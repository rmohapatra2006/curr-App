from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)
def to_get_currency(from_currency,to_currency,amt):

    url = "https://currency-converter13.p.rapidapi.com/convert"

    querystring = {"from":from_currency,"to":to_currency,"amount":amt}

    headers = {
    'x-rapidapi-key': "bbc4e72c95msh764d7107571c9ccp132292jsne000b3620c23",
    'x-rapidapi-host': "currency-converter13.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers,params=querystring )
    resp={}
    if response.status_code != 200:
        resp["API_error_msg"]=response.text
    else:
        resp = response.json()
        

    print(resp)
    
    return resp['amount']

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/convert",methods=["GET","POST"])
def convert_currency():
    if request.method == "POST":
        from_currency_country = request.form["from_currency_country"]
        to_currency_country = request.form["to_currency_country"]
        amount_currency = request.form["amount_currency"]
        try:
            amount_currency = float(amount_currency)
        except Exception as e:
            return render_template("error.html",data=e)
            
        result= round(to_get_currency(from_currency_country,to_currency_country,amount_currency),2)
    return  render_template("index.html",result=result,time=datetime.now().strftime("%m-%D-%Y %H-%M-%S"))

if(__name__)=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
