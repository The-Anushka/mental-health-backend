from flask import Flask, request, jsonify
from flask_cors import CORS
from nlp_models.sentiment import analyze_sentiment
from nlp_models.emotion import analyze_emotion
from utils.distress_score import get_distress_score

app = Flask(__name__)
CORS(app)
@app.route("/", methods=["GET"])
def home():
    return "Mental Health Monitor API is running."

@app.route("/analyze", methods=["POST"])
def analyze_text():
    data = request.get_json()
    text = data.get("text", "")

    sentiment = analyze_sentiment(text)
    emotions = analyze_emotion(text)
    distress = get_distress_score(sentiment, emotions)

    return jsonify({
        "sentiment": sentiment,
        "emotions": emotions,
        "distress_score": distress
    })

if __name__ == "__main__":
    app.run(debug=True)
