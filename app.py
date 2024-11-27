from flask import Flask, render_template, request,url_for, session, flash,redirect,jsonify

app = Flask(__name__)
app.secret_key = 'marianokpo'

#simula un usuario para el ejemplo
USUARIO_VALIDO = {'username':'admin','licence':'1234'}

#Ruta principal
@app.route('/')
def home():
    return render_template('home.html')

#Ruta que recibe datos de un formulario

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        licence = request.form['licence']
        
        
        if username == USUARIO_VALIDO['username'] and licence == USUARIO_VALIDO['licence']:
            session['user'] = username #Guarda el usuario en la sesion
            flash('Inicio de sesion exitoso','success')
            return redirect(url_for('protected'))
        else:
            flash('Credenciales incorrectas','error')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user',None) #Elimina al usuario de la sesion
    flash('Cerraste sesion','info')
    return redirect(url_for('home'))


# Función simple de chatbot
def get_bot_response(user_input):
    responses = {
        'hola': '¡Hola! ¿Cómo puedo ayudarte?',
        'adios': '¡Adiós! Hasta luego.',
        'como estas': 'Estoy bien, gracias por preguntar. ¿Y tú?',
        'default': 'Lo siento, no entendí tu mensaje. ¿Puedes repetir?'
    }
    return responses.get(user_input.lower(), responses['default'])

# Ruta para interactuar con el chatbot
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if user_input:
        bot_response = get_bot_response(user_input)
        return jsonify({'response': bot_response})
    else:
        return jsonify({'response': 'Por favor, ingresa un mensaje.'}), 400



@app.route('/protected')
def protected():
    if 'user' in session:
        return render_template('protected.html', user = session['user'])
    flash('Debes iniciar sesion para acceder a esta pagina','error')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host= '0.0.0.0' ,port = 5000,debug=True)