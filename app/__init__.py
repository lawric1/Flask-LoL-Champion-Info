from flask import Flask, render_template, request, url_for, redirect
import requests

app = Flask(__name__)
app.debug = True

link = "https://ddragon.leagueoflegends.com/cdn/10.25.1/data/en_US/champion.json"

db = requests.get(link).json()['data']

@app.route('/search', methods=['POST','GET'])
def search():
    if request.method == 'POST':
        data = {}
        req = request.form['SearchField'].lower().capitalize()
        if not req: 
            return redirect(url_for('index'))

        try:
            champion = db[req]
            data[champion['id']] = champion
            return render_template('index.html', db=data.values())
        except:
            return render_template('index.html', db='')

@app.route('/',  methods=['POST', 'GET'])
def index():
    return render_template('index.html', db=db.values())
