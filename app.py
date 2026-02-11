from flask import Flask, render_template

app = Flask(__name__)

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta dinámica (ejemplo: reserva de turno)
@app.route('/reserva/<cliente>')
def reserva(cliente):
    return f"Bienvenido, {cliente}. Tu reserva está confirmada para hoy."

if __name__ == '__main__':
    app.run(debug=True)
