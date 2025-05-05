from flask import Flask, request, render_template_string, send_from_directory
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <!DOCTYPE html>
        <html>
        <head><title>Sfiral Horoscope</title></head>
        <body>
            <h2>Введите дату рождения:</h2>
            <form method="post" action="/horoscope">
                <input type="date" name="birthdate" required>
                <button type="submit">Построить гороскоп</button>
            </form>
        </body>
        </html>
    '''

@app.route('/horoscope', methods=['POST'])
def horoscope():
    birthdate_str = request.form['birthdate']
    birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    # Упрощённый расчёт фазы
    phase_names = ['фаза зарождения 🌱', 'фаза роста 🌿', 'фаза расцвета 🌻', 'фаза убывания 🍂']
    phase_index = age % 4
    phase = phase_names[phase_index]

    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head><title>Ваш гороскоп</title></head>
        <body>
            <h1>Ваш гороскоп</h1>
            <p>Дата рождения: {{ birthdate }}</p>
            <p>Возраст: {{ age }}</p>
            <p>Сфиральный прогноз: {{ phase }}</p>

            <h2>Сфираль</h2>
            <img src="/static/sfiral.png" alt="Сфираль" style="max-width: 300px;">

            <p><a href="/">Назад</a></p>
        </body>
        </html>
    ''', birthdate=birthdate.strftime('%d.%m.%Y'), age=age, phase=phase)

# Для локальной отладки (не нужно на Render)
if __name__ == '__main__':
    app.run(debug=True)
