from flask import Flask, render_template_string, request, send_from_directory
from datetime import datetime
import os
from diagram import plot_phase_diagram

app = Flask(__name__)
os.makedirs("static", exist_ok=True)

FORM_HTML = '''
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

RESULT_HTML = '''
<!DOCTYPE html>
<html>
<head><title>Ваш гороскоп</title></head>
<body>
  <h1>Ваш гороскоп</h1>
  <p>Дата рождения: {{ birthdate }}</p>
  <p>Возраст: {{ age }}</p>
  <p>Сфиральный прогноз: {{ phase }}</p>
  <img src="/static/diagram.png" alt="Диаграмма фазы" width="400">
  <p><a href="/">Назад</a></p>
</body>
</html>
'''

def get_phase(age):
    phase_map = ["фаза зарождения 🌑", "фаза роста 🌱", "фаза расцвета 🌻", "фаза убывания 🍂"]
    return phase_map[age % 4]

@app.route("/", methods=["GET"])
def index():
    return FORM_HTML

@app.route("/horoscope", methods=["POST"])
def horoscope():
    birth_str = request.form["birthdate"]
    birth_date = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    phase = get_phase(age)
    plot_phase_diagram(age)
    return render_template_string(RESULT_HTML, birthdate=birth_date.strftime("%d.%m.%Y"), age=age, phase=phase)

@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("static", filename)
