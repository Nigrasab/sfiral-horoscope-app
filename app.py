from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

# Фазы Сфирали по пятилеткам
phases = [
    {"start": 0, "end": 5, "text": "Зачатие импульса. Формирование основы телесности.", "formula": "Я есмь движение зарождающее."},
    {"start": 5, "end": 10, "text": "Формирование восприятия. Впитывание мира.", "formula": "Я есмь чистота восприятия."},
    {"start": 10, "end": 15, "text": "Индивидуализация. Сборка контуров Я.", "formula": "Я есмь образ становящийся."},
    {"start": 15, "end": 20, "text": "Рост воли. Поиск ориентации.", "formula": "Я есмь вектор напряжения."},
    {"start": 20, "end": 25, "text": "Консолидация личного центра.", "formula": "Я есмь точка осознания."},
    {"start": 25, "end": 30, "text": "Экспансия. Выход в реализацию.", "formula": "Я есмь действие развёрнутое."},
    {"start": 30, "end": 35, "text": "Стабилизация и пересмотр намерений.", "formula": "Я есмь напряжение выбора."},
    {"start": 35, "end": 40, "text": "Финал витка. Предельная форма.", "formula": "Я есмь граница расширения."},
    {"start": 40, "end": 45, "text": "Вход в S-петлю. Снятие внешнего импульса.", "formula": "Я есмь начало разворота."},
    {"start": 45, "end": 50, "text": "Дуга. Смещение ориентации внутрь.", "formula": "Я есмь дуга раскрытия."},
    {"start": 50, "end": 55, "text": "Центральная точка поворота.", "formula": "Я есмь ось отражения."},
    {"start": 55, "end": 60, "text": "Антидуга. Сбор пережитого в новый порядок.", "formula": "Я есмь возвращающее движение."},
    {"start": 60, "end": 65, "text": "Выход из петли. Вхождение в антивиток.", "formula": "Я есмь разворот витка."},
    {"start": 65, "end": 70, "text": "Обратное движение. Осознание прожитого.", "formula": "Я есмь внутренняя ось."},
    {"start": 70, "end": 75, "text": "Переоценка и сжатие смысла.", "formula": "Я есмь концентрированное знание."},
    {"start": 75, "end": 80, "text": "Углубление и отпускание.", "formula": "Я есмь проникающее созерцание."},
    {"start": 80, "end": 85, "text": "Прозрачность и равновесие.", "formula": "Я есмь центр покоя."},
    {"start": 85, "end": 90, "text": "Подготовка к завершению цикла.", "formula": "Я есмь итог формы."},
    {"start": 90, "end": 95, "text": "Сжатие. Переход в тонкие слои.", "formula": "Я есмь незримое присутствие."},
    {"start": 95, "end": 100, "text": "Завершение антивитка. Снятие фигуры.", "formula": "Я есмь круг завершённый."},
    {"start": 100, "end": 105, "text": "Пунктир. Порог внешнего.", "formula": "Я есмь след уходящий."},
    {"start": 105, "end": 110, "text": "Разрешение остаточного импульса.", "formula": "Я есмь неуловимое."},
    {"start": 110, "end": 115, "text": "Слияние с фоном. Растворение.", "formula": "Я есмь свет без образа."},
    {"start": 115, "end": 120, "text": "Исчезновение различий. Покой полного разворота.", "formula": "Я есмь ничто различающее."}
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/horoscope", methods=["POST"])
def horoscope():
    date_str = request.form.get("birthdate")
    if not date_str:
        return "Дата не указана."

    try:
        birthdate = datetime.strptime(date_str, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

        for phase in phases:
            if phase["start"] <= age < phase["end"]:
                return render_template("result.html", age=age, phase=f"{phase['start']}–{phase['end']} лет", text=phase["text"], formula=phase["formula"])

        return render_template("result.html", age=age, phase="Вне диапазона", text="Фаза не определена.", formula="")
    except Exception as e:
        return f"Ошибка: {e}"

if __name__ == "__main__":
    app.run(debug=True)
