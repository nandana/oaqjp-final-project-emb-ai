import requests
import json

EMOTION_DETECTION_API = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

def emotion_detector(text_to_analyze: str) -> dict:
    """A method to detect the emotions of a given text using NLP techniques.

    Args:
        text_to_analyze (str): input text to anaylze

    Returns:
        dict: the scores for different emotions (anger, disgust, fear, joy, sadness) and dominant_emotion
    """
    input_headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_data = {"raw_document": {"text": text_to_analyze }}

    response = requests.post(EMOTION_DETECTION_API, data=json.dumps(input_data), headers=input_headers)
    if response.status_code == 400:
        # in case of HTTP 400 error, we return an empty dictionary
        keys = ["anger", "disgust", "dominant_emotion", "fear", "joy", "sadness"]
        emotions = {key: None for key in keys}
    else:  
        output = response.json()
        # selecting the emotions part of the response
        emotions = response.json()['emotionPredictions'][0]['emotion']
        # detecting the emotion with the highest score
        dominant_emotion = max(emotions, key=emotions.get)
        # extending the ouput with the dominant emotion
        emotions['dominant_emotion'] = dominant_emotion

    return emotions
