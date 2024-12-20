from flask import Flask, render_template, request, redirect, url_for

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key_here'

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/ask', methods=['GET', 'POST'])
    def ask():
        if request.method == 'POST':
            question = request.form['question']
            # Aquí podrías guardar la pregunta en una base de datos
            print(f"Pregunta: {question}")
            return redirect(url_for('home'))
        return render_template('ask.html')

    return app
