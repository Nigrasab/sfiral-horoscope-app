from flask import Flask, request, render_template_string
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def form():
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
def result():
    birthdate_str = request.form.get("birthdate")
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

        return render_template_string(f"""
            <h2>Ваш гороскоп</h2>
            <p>Дата рождения: {birthdate.strftime('%d.%m.%Y')}</p>
            <p>Возраст: {age}</p>
            <p>Сфиральный прогноз: фаза обновления 🌱</p>
            <a href="/">Назад</a>
        """)
    except Exception as e:
        return f"Ошибка обработки даты: {e}"
