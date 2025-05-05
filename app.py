from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Sfiral Horoscope is running!"
# Placeholder for web app interface using Flask
