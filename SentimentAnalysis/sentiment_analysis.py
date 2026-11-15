import requests
import json

def sentiment_analyzer(text_to_analyse):
    url = "https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = {"raw_document": { "text": text_to_analyse }}
    response = (requests.post(url, json = myobj, headers=header)).text
    
    jsonResponse = json.loads(response)
    label = jsonResponse["documentSentiment"]["label"]
    score = jsonResponse["documentSentiment"]["score"]

    if request.response_code != 200:
        label = "None"
        score = "None"

    newResp = {"label": label, "score": score}
    return newResp