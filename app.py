from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

# Таблица фаз по пятилеткам (пример с одной записью, далее можно расширить)
phases = {
    (50, 55): "Фаза разрыва. Переформатирование цели."
    # Добавьте остальные интервалы
}

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        date_str = request.form.get("birthdate")
        try:
            birthdate = datetime.strptime(date_str, "%Y-%m-%d")
            today = datetime.today()
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

            for (start, end), msg in phases.items():
                if start <= age < end:
                    result = f"""
                        <div class="result">
                            <h3>{start}–{end} лет</h3>
                            <p>{msg}</p>
                            <div class="mantra">Медитативная формула:<br><em>Отпускаю прежние формы. Слышу новый зов. Становлюсь собой заново.</em></div>
                        </div>
                    """
                    break
            if not result:
                result = "<p>Возраст вне диапазона.</p>"
        except Exception as e:
            result = f"<p>Ошибка: {e}</p>"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
