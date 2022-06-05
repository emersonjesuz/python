


from distutils.log import debug
from unicodedata import name
from flask import Flask, flash, request, render_template



app = Flask(__name__)

@app.route('/')
def cadastrar(): 
    return 'p'





if __name__=='__main__':
    app.run(debug=True)