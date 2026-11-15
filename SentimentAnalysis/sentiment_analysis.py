''' Module for running sentiment analysis using the Watson NLP BERT Sentiment Analysis function
'''
import json
import requests

def sentiment_analyzer(text_to_analyse):
    ''' This function sends text_to_analyse to NLP BERT Sentiment Analysis
    and returns the results (label and score)
    '''
    url = "https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = {"raw_document": { "text": text_to_analyse }}
    response = requests.post(url, json = myobj, headers=header, timeout=5)

    if response.status_code == 200:
        response_str = response.text
        json_response = json.loads(response_str)
        label = json_response["documentSentiment"]["label"]
        score = json_response["documentSentiment"]["score"]
    else:
        label = None
        score = None
        print(label, score)

    new_resp = {"label": label, "score": score}
    return new_resp
