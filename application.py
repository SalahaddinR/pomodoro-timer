from flask import Flask, render_template, jsonify, request
from config import DEVELOPMENT_CONFIGURATIONS

app = Flask(
    __name__,
    template_folder=DEVELOPMENT_CONFIGURATIONS.TEMPLATES_FOLDER,
    static_folder=DEVELOPMENT_CONFIGURATIONS.STATICS_FOLDER
)
app.config.from_object(DEVELOPMENT_CONFIGURATIONS)

@app.route('/countdown-time', methods=('POST', 'GET', 'PUT'))
def countDownTime():
    if request.method == 'GET':
        return jsonify({
            "focus_minutes": DEVELOPMENT_CONFIGURATIONS.TEMP_COUNTDONW_FOCUS_MINUTES, 
            "focus_seconds": DEVELOPMENT_CONFIGURATIONS.TEMP_COUNTDOWN_FOCUS_SECONDS,
            "shortrest_minutes": DEVELOPMENT_CONFIGURATIONS.TEMP_COUNTDONW_SHORTREST_MINUTES,
            "shortrest_seconds": 0,
            "longrest_minutes": DEVELOPMENT_CONFIGURATIONS.TEMP_COUNTDONW_LONGREST_MINUTES,
            "longrest_seconds": 0,
            "laps": DEVELOPMENT_CONFIGURATIONS.TEMP_COUNTDOWN_LAPS
        })
    

@app.route('/')
def countDown():
    return render_template('index.html')

app.run()