from flask import Flask, render_template

app = Flask(__name__)  # nuevo objeto


@app.route('/')  # wrap o un decorador
def home():
    # return 'Hello, World!'
    # Nos regresa un string o una pagina HTML
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    # Nos permite escuchar todos los cambios que hagamos en el código
    app.run(debug=True)
