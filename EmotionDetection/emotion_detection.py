import requests
import json

def emotion_detector(text_to_analyse):
   url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
   myobj = { "raw_document": { "text": text_to_analyse } }
   header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
   response = requests.post(url, json = myobj, headers=header)
   formatted_response = json.loads(response.text)
   if response.status_code == 200:
      emotion = formatted_response['emotionPredictions'][0]['emotion']
      dominant_emotion = max(emotion, key=emotion.get)
   elif response.status_code == 400:
       emotion = None
       dominant_emotion = None
       
   return {'emotion': emotion, 'dominant_emotion': dominant_emotion}
