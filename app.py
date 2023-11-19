from flask import Flask, render_template, request
from pptx import Presentation
from pptx.util import Inches
from presentationcode import create_presentation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_presentation', methods=['POST'])
def generate_presentation():
    lang = request.form['lang']
    qwsb = request.form['qwsb']
    plos = request.form['plos']
    doc = request.form['doc']
    aut = request.form['aut']
    mng = request.form['mng']
    plc = request.form['plc']
    year = request.form['year']
    vot = request.form['vot']
    
    # Check the value of vot and handle it accordingly in your presentation generation logic
    
    create_presentation(lang, qwsb, plos, doc, aut, mng, plc, year, vot, ...)
    
    return "Presentation generated successfully!"

if __name__ == '__main__':
    app.run(debug=True)
