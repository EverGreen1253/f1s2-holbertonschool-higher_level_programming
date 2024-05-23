#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/items')
def items():
    itemslist = ["Book", "Mug", "Sticker", "Card", "Spoon"]
    return render_template('items.html', items=itemslist)

# Set debug=True for the server to auto-reload when there are changes
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
