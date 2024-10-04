from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_route():
    input_text = request.args.get('textToAnalyze', 'Guest')
    emotion_output = emotion_detector(input_text)

    if emotion_output['dominant_emotion'] == None:
        output_text = "Invalid text! Please try again!"
    else:
        output_text = f"For the given statement, the system response is 'anger': {emotion_output['anger']}, \
'disgust': {emotion_output['disgust']}, 'fear': {emotion_output['fear']}, 'joy': {emotion_output['joy']} \
and 'sadness': {emotion_output['sadness']}. The dominant emotion is {emotion_output['dominant_emotion']}."

    return output_text
