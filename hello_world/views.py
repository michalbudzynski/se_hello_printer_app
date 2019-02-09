from hello_world import app
from formater import get_formatted
from formater import SUPPORTED, PLAIN
from flask import request

MOJE_IMIE = "Michal"
msg = "Witaj swiecie!"


@app.route('/')
def index():
    output = request.args.get('output')
    if not output:
        output = PLAIN
        imie = request.args.get('imie')
    if not imie:
        imie = MOJE_IMIE
    return get_formatted(msg, moje_imie,
                         output.lower())


@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)
