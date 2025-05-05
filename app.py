from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return '''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Sfiral Horoscope</title>
        </head>
        <body>
            <h2>Введите дату рождения:</h2>
            <form method="post" action="/horoscope">
                <input type="date" name="birthdate" required>
                <button type="submit">Построить гороскоп</button>
            </form>
        </body>
        </html>
    '''

@app.route("/horoscope", methods=["POST"])
def horoscope():
    birthdate_str = request.form.get("birthdate")
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
        return f'''
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <title>Результат</title>
            </head>
            <body>
                <h2>Фазовый гороскоп для: {birthdate.strftime("%d.%m.%Y")}</h2>
                <p>🜂 Солнце в знаке (примерная зона расчёта).</p>
                <p>🜄 Эфемериды и фазы будут добавлены позднее.</p>
                <a href="/">← Назад</a>
            </body>
            </html>
        '''
    except:
        return '''
            <p>Ошибка разбора даты. Пожалуйста, введите корректную дату.</p>
            <a href="/">← Назад</a>
        '''
