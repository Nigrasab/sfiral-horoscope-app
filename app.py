from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

phases = {
    (50, 55): {
        "title": "50–55 лет",
        "text": "Фаза разрыва. Переформатирование цели.",
        "mantra": "Отпускаю прежние формы. Слышу новый зов. Становлюсь собой заново."
    },
    # Добавь остальные фазы по аналогии
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/phase", methods=["POST"])
def get_phase():
    data = request.get_json()
    date_str = data.get("date")

    try:
        birthdate = datetime.strptime(date_str, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

        for (start, end), content in phases.items():
            if start <= age < end:
                return jsonify({
                    "success": True,
                    "title": content["title"],
                    "text": content["text"],
                    "mantra": content["mantra"]
                })

        return jsonify({"success": False, "error": "Возраст вне диапазона."})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
