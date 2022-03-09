# pylint: disable=no-member

from flask import (Flask, redirect, render_template)
from flask_talisman import Talisman

app = Flask('charneira')
app.config.from_object('config.BaseConfig')
talisman = Talisman(app, content_security_policy=app.config['CSP'])

@app.route('/')
def index():
    return render_template('index.html', title='Charneira')

@app.route('/programacao')
def programacao():
    return render_template('programacao.html', title='Charneira - Programação')

@app.route('/convidados')
def convidados():
    return render_template('convidados.html', title='Charneira - Convidados')

@app.route('/apoiadores')
def apoiadores():
    return render_template('apoiadores.html', title='Charneira - Apoiadores')

@app.route('/faq')
def faq():
    return render_template('faq.html', title='Charneira - FAQ')

@app.route('/contato')
def contato():
    return redirect("mailto:contato@charneira.com.br")

@app.route('/email-parceria')
def email_parceria():
    return redirect("mailto:parceria@charneira.com.br")