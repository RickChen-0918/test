from flask import Flask, render_template
from random import randint
import finnhub

app = Flask(__name__)
fh_client = finnhub.Client(api_key='c4tdapqad3icjlrouek0')

@app.route("/<ticker>")
def home(ticker):
    quote = fh_client.quote(ticker)
    peers = fh_client.company_peers(ticker)
    return render_template("home.html",quote=quote['c'], ticker=ticker, peers=peers)

app.run()
