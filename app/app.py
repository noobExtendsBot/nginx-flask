from flask import Flask, request, render_template
import requests
import os
import json
import random
import socket

QUOTE_URL = "https://type.fit/api/quotes"

app = Flask(__name__)


@app.route(
    "/",
    methods=[
        "GET",
    ],
)
def get_quote():
    error = None
    quote_data = None
    if request.method == "GET":
        try:
            r = requests.get(url=QUOTE_URL)
            if r.status_code == 200:
                try:
                    quote_data = random.choice(json.loads(r.text)).get("text")
                except json.JSONDecodeError as e:
                    error = f"Error decoding JSON: {e}"
        except requests.exceptions.RequestException:
            raise "Network Issue"
    else:
        error = "Method not allowed"
    return render_template("index.html", error=error, quote_data=quote_data, id=socket.gethostname())

if __name__ == "__main__":
    app.run(debug=True)