#!/usr/bin/env python3
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # Obtener la fecha y hora actuales
    now = datetime.now()
    formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    # Renderizar la plantilla con el mensaje de bienvenida y la fecha y hora actuales
    return render_template('index.html', message='¡Bienvenidos!', date_time=formatted_date_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)