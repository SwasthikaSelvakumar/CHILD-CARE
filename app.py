from flask import Flask, render_template, request
import joblib
from util import get_counseling_tips

# Initialize Flask
app = Flask(__name__)

# Load ML model and label encoder
model = joblib.load("model/emotion_model.pkl")
label_encoder = joblib.load("model/label_encoder.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/emotion')
def emotion_page():
    return render_template("emotion.html")

@app.route('/quiz')
def quiz_page():
    return render_template("quiz.html")

@app.route('/counsel', methods=['POST'])
def counsel():
    source = request.form.get('source')  # "manual" or "quiz"

    if source == "manual":
        # Emotion selected by user manually
        emotion = request.form.get("emotion")

    elif source == "quiz":
        # Collect inputs from quiz (6 real, 2 padded for model compatibility)
        input_data = [
            int(request.form.get("q1")),
            int(request.form.get("q2")),
            int(request.form.get("q3")),
            int(request.form.get("q4")),
            int(request.form.get("q5")),
            int(request.form.get("q6")),
            0,  # q7 default
            0   # q8 default
        ]

        # Predict emotion and decode label
        prediction = model.predict([input_data])[0]
        emotion = label_encoder.inverse_transform([prediction])[0]

    else:
        emotion = "Numb"

    # Get text-based counseling tips
    tips = get_counseling_tips(emotion)

    return render_template("counseling.html", emotion=emotion, tips=tips)

if __name__ == '__main__':
    app.run(debug=True)
