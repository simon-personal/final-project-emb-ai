from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    ''' Renders the main application page
    '''
    return render_template("index.html")

@app.route('/emotionDetector')
def get_emotion_detector():
    ''' Runs EmotionDetection.emotion_detection.emotion_detector() on 
        the request argument textToAnalyze. The output is a string description
        of the function result
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if not response['dominant_emotion']:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is 'anger': {response['anger']}, \
        'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} \
        and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)