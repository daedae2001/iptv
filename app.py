from flask import Flask,  render_template, request, session #, redirect, url_for,jsonify # pip install Flask
#from flask_mysqldb import MySQL,MySQLdb # pip install Flask-MySQLdb
from os import path 
#from notifypy import Notify #pip install notify-py

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("contenido.html")    

@app.route('/layout', methods = ["GET", "POST"])
def layout():
    session.clear()
    return render_template("contenido.html")

@app.route('/tv', methods = ["GET", "POST"])
def tv():
    act = request.args.get('act', default = 0, type = int)
    if act == 0:
        return render_template('tv.html')
    else:
        import descarga
        import crea_guia_html
        descarga.ejecuta_descarga()
        crea_guia_html.crea_grilla()
        return render_template('tv.html')
   
if __name__ == '__main__':
    app.secret_key = "PFEh8!YR7C&xL4"
    app.run(debug=False)