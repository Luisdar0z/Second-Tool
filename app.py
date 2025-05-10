from flask import Flask, render_template, request, jsonify
import random
import threading
import webview

app = Flask(__name__)

def convertir_a_hh_mm_ss(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    return f"{horas:02}:{minutos:02}:{segundos_restantes:02}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    segundos = data.get('segundos', 0)
    try:
        segundos = int(segundos)
    except ValueError:
        return jsonify({'error': 'Entrada inválida'}), 400

    resultado = convertir_a_hh_mm_ss(segundos)
    return jsonify({'resultado': resultado})

# Convertir formato HH:MM:SS a segundos
@app.route('/to_seconds', methods=['POST'])
def to_seconds():
    data = request.get_json()
    tiempo = data.get('tiempo', '00:00:00')
    try:
        h, m, s = map(int, tiempo.split(':'))
    except ValueError:
        return jsonify({'error': 'Formato inválido'}), 400
    total = h * 3600 + m * 60 + s
    return jsonify({'segundos': total})

# Generar múltiples valores aleatorios
@app.route('/randoms', methods=['POST'])
def randoms():
    data = request.get_json()
    segundos = data.get('segundos', 0)
    cantidad = data.get('cantidad', 1)
    try:
        segundos = int(segundos)
        cantidad = int(cantidad)
    except ValueError:
        return jsonify({'error': 'Entrada inválida'}), 400
    if segundos < 1 or cantidad < 1:
        return jsonify({'error': 'Valores deben ser >= 1'}), 400
    valores = [random.randint(1, segundos) for _ in range(cantidad)]
    return jsonify({'valores': valores})

# Punto de entrada
if __name__ == "__main__":
    # Ejecuta Flask en hilo en segundo plano
    t = threading.Thread(target=lambda: app.run(host="127.0.0.1", port=5000, debug=False))
    t.daemon = True
    t.start()
    # Abre ventana nativa con WebView
    webview.create_window("Conversor de Segundos", "http://127.0.0.1:5000", width=510, height=870)
    webview.start()
