#! /usr/bin/env python3

import requests
import json

'''In this file, we will write the function to run emotion detection.'''

# TO DO: write function emotion_detector
def emotion_detector(text_to_detect):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
      "grpc-metadata-mm-model-id": 
      "emotion_aggregated-workflow_lang_en_stock"
    }
            
    myobj = { "raw_document": { "text": text_to_detect} }
    response = requests.post(url, json=myobj, headers=headers)
    data = json.loads(response.text)
    emotions = data["emotionPredictions"][0]["emotion"]
    emotions_sorted = sorted(list(emotions.items()), key=lambda x: x[1], reverse=True)
    dominant = emotions_sorted[0]
    emotions["dominant_emotion"] = dominant[0]
    return emotions

if __name__ == "__main__":
    test = "I am so happy I am doing this!"
    print(emotion_detector(test))
