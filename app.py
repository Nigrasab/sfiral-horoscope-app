from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

# Таблица фаз по пятилеткам (сокращённо, для примера)
phases = {
    (0, 5): "Зачатие импульса. Формирование основы телесности.",
    (5, 10): "Формирование восприятия. Впитывание мира.",
    (10, 15): "Ускорение. Индивидуализация начинается.",
    # ... до (115, 120)
    (115, 120): "Исчезновение границ. Я есмь полное растворение."
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/horoscope")
def horoscope():
    date_str = request.args.get("date")
    if not date_str:
        return "Дата не указана."

    try:
        birthdate = datetime.strptime(date_str, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

        # Найти фазу по возрасту
        text = ""
        for (start, end), msg in phases.items():
            if start <= age < end:
                text = f"<h3>{start}–{end} лет</h3><p>{msg}</p>"
                break

        if not text:
            text = "Возраст вне диапазона."

        return text
    except Exception as e:
        return f"Ошибка: {e}"

if __name__ == "__main__":
    app.run(debug=True)
