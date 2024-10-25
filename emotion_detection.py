import requests, json

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
def json_template(text:str):
    return {"raw_document": {"text": text}}

def emotion_detector(text_to_analyze:str):
    ''' Runs the Watson NLP Emotion Predict function on `text_to_analyze`
    '''
    response = requests.post(URL, headers=HEADERS, json=json_template(text_to_analyze))
    return response.text