import json
from datetime import datetime
from pathlib import Path
from flask import Flask, request, jsonify, render_template, url_for

app = Flask(__name__)

# ---------------------------------------------------------
# Загрузка фаз из внешнего файла phases.json
# ---------------------------------------------------------
PHASES_PATH = Path(__file__).parent / "phases.json"

def load_phases() -> dict:
    if not PHASES_PATH.exists():
        raise FileNotFoundError("phases.json not found. Add the file to project root.")
    with open(PHASES_PATH, "r", encoding="utf-8") as fp:
        data = json.load(fp)
    # преобразуем ключи из "0-5" в кортежи (0,5)
    converted = {}
    for interval, payload in data.items():
        start, end = map(int, interval.split("-"))
        converted[(start, end)] = payload
    return converted

phases = load_phases()

# ---------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")

# API для Ajax-запроса --------------------------------------------------------
@app.route("/api/phase", methods=["POST"])
def api_phase():
    payload = request.get_json(force=True)
    date_str = payload.get("date")
    try:
        birthdate = datetime.strptime(date_str, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

        for (start, end), info in phases.items():
            if start <= age < end:
                return jsonify(success=True, **info)
        return jsonify(success=False, error="Возраст вне диапазона 0–120 лет.")
    except Exception as exc:
        return jsonify(success=False, error=str(exc))

# ---------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
