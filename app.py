from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML-шаблон из index.html
form_html = """
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
"""

@app.route("/")
def index():
    return render_template_string(form_html)

@app.route("/horoscope", methods=["POST"])
def horoscope():
    birthdate = request.form.get("birthdate")
    return f"<h2>Фазовый гороскоп для даты: {birthdate}</h2><p>🜁 Обработка данных будет здесь.</p>"

