from flask import Flask, render_template, request
from code4b import create_presentation

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
    nos = request.form['nos']

    print(f"Value of nos: {nos}")  # Add this line to print the value

    nmos_values = [request.form.get(f'nmos_{i}', '') for i in range(int(nos))]

    create_presentation(lang, qwsb, plos, doc, aut, mng, plc, year, vot, nos, nmos_values)
    
    return "Presentation generated successfully!"


if __name__ == '__main__':
    app.run(debug=True)
