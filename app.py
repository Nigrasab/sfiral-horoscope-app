import json
from pathlib import Path
from datetime import datetime
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# ───────────────────────────────────────────────────
# Загрузка фаз из phases.json
# ───────────────────────────────────────────────────
PHASES_PATH = Path(__file__).parent / "phases.json"

def load_phases() -> dict:
    with open(PHASES_PATH, "r", encoding="utf-8") as fp:
        raw = json.load(fp)
    phases = {}
    for interval, payload in raw.items():
        start, end = map(int, interval.split("-"))
        phases[(start, end)] = payload
    return phases

phases = load_phases()

# ───────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")

# ─ маршру для Ajax ------------------------------------------------------------
@app.route("/api/phase", methods=["POST"])
def api_phase():
    date_str = request.json.get("date")
    try:
        bd   = datetime.strptime(date_str, "%Y-%m-%d")
        now  = datetime.today()
        age  = now.year - bd.year - ((now.month, now.day) < (bd.month, bd.day))

        for (start, end), data in phases.items():
            if start <= age < end:
                return jsonify(success=True, **data)
        return jsonify(success=False, error="Возраст вне диапазона 0–120 лет.")
    except Exception as exc:
        return jsonify(success=False, error=str(exc))

# ─ страница «О проекте» -------------------------------------------------------
@app.route("/info")
def info():
    return render_template("info.html")

# ───────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)
