'''Server for a flask app version of the Emotion detection project.'''

from flask import Flask, request, url_for, redirect, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/'):
def index():
    return render_template('index.html')

@app.route('/emotionDetector'):
def emotional():
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    response = f"""For the given statement the system response is: 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']}, and 'sadness': {result['sadness']}. The dominant emotion is <strong>{result['dominant_emotion']}</strong>."""
    return response

if __name__ == "__main__":
    app.run()