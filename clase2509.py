from flask import Flask, render_template 
from flask import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired

class MiFormulario(FlakForm):
    name= StringField('name',validators=[DataRequired()])
    submit=SubmitField('validar')


app =Flask(__name__)
app.config['SECRET_KEY']='un string muy dificil de adivinar'

@app.route('/')
@app.route('/index')
def index ():
    return "hello"

@app.route('/users')
def user():
    users=[{'nik':'Titi','name':'Thiago'},{'nik':'Fer','name':'Fernando'},{'nik':'Leo','name':'Leonardo'}]
    value=12
    return render_template('users.html',users=users,value=value)

@app.route('/formulario',methods=['GET','POST']):
# SI SOLO agrego Post .. solo puedo conectarme a ese .. y llamo a solo a esa funcion...
# si solo get ..
def formulario():
    mi_formulario=MiFormulario()
    #return mi_formulario
    return render_template('formulario.html',form=mi_formulario)
    #copiar el template de la documentacion ..
    # el tempplate va a funcionar si la variable vale form.. rederiza a la plantilla y crea el formulario mi_formulario.
#la platilla necesita un form ... y le paso mi_formulario



if (__name__=='__main__'):
    app.run(debug=True,host='0.0.0.0')


