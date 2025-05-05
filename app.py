from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

#  ▶ сюда постепенно внесёте все интервалы; пока одна запись достаточно, чтобы проверить логику
phases = {
    (50, 55): {
        "title": "50–55 лет",
        "text": "Фаза разрыва. Переформатирование цели.",
        "mantra": "Отпускаю прежние формы. Слышу новый зов. Становлюсь собой заново."
    }
}

# ─────────────────────────────────────────────
@app.route("/")                          # главная – только GET
def index():
    return render_template("index.html")
# ─────────────────────────────────────────────
@app.route("/api/phase", methods=["POST"])        # AJAX‑маршрут
def api_phase():
    date_str = request.json.get("date")
    try:
        bd = datetime.strptime(date_str, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - bd.year - (
            (today.month, today.day) < (bd.month, bd.day)
        )

        for (start, end), data in phases.items():
            if start <= age < end:
                return jsonify(success=True, **data)

        return jsonify(success=False, error="Возраст вне диапазона 0‑120.")
    except Exception as e:
        return jsonify(success=False, error=str(e))
# ─────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)
