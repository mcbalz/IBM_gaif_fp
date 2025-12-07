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
    emotions = data["emotionPredictions"]["emotions"]
    high_item = [None, 0]
    for item in emotions:
        if item[1] > high_item[1]:
            high_item[0], high_item[1] = item[0], item[1]
    emotions["dominant_emotion"] = high_item[0]

    return emotions

# TO DO: take a screenshot of the code written and save it as 2a_emotion_detection.png

# TO DO: test out the function in python3, using "I love this new technology" string 

# TO DO: screenshot the terminal with all three steps included in it including final output 
# name the screenshot 2b_application_creation.png

