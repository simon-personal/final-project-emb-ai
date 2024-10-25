import requests, json

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
def json_template(text:str):
    return {"raw_document": {"text": text}}

def find_dominant_emotion(emotions:dict):
    ''' Finds the emotion with the highest score in `emotions` and returns its name
    '''
    max_emotion = ""
    max_val = -1
    for key in emotions.keys():
        if emotions[key] > max_val:
            max_emotion = key
            max_val = emotions[key]
    return max_emotion

def emotion_detector(text_to_analyze:str):
    ''' Runs the Watson NLP Emotion Predict function on `text_to_analyze`
    '''
    response = requests.post(URL, headers=HEADERS, json=json_template(text_to_analyze))
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        response_dict = {
            'anger': formatted_response['emotionPredictions'][0]['emotion']['anger'],
            'disgust': formatted_response['emotionPredictions'][0]['emotion']['disgust'],
            'fear': formatted_response['emotionPredictions'][0]['emotion']['fear'],
            'joy': formatted_response['emotionPredictions'][0]['emotion']['joy'],
            'sadness': formatted_response['emotionPredictions'][0]['emotion']['sadness']
        }

        response_dict['dominant_emotion'] = find_dominant_emotion(response_dict)

    elif response.status_code == 400:
        response_dict = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None
        }

        response_dict['dominant_emotion'] = None
    
    return response_dict