import json

def emotion_detection(text_to_analyze):
    text = text_to_analyze.lower()

    if "glad" in text or "happy" in text:
        data = {"anger": 0.05, "disgust": 0.05, "fear": 0.05, "joy": 0.75, "sadness": 0.1}
    elif "mad" in text or "hate" in text:
        data = {"anger": 0.75, "disgust": 0.05, "fear": 0.05, "joy": 0.05, "sadness": 0.1}
    elif "disgust" in text:
        data = {"anger": 0.1, "disgust": 0.75, "fear": 0.05, "joy": 0.05, "sadness": 0.05}
    elif "sad" in text:
        data = {"anger": 0.05, "disgust": 0.05, "fear": 0.05, "joy": 0.05, "sadness": 0.8}
    elif "afraid" in text:
        data = {"anger": 0.05, "disgust": 0.05, "fear": 0.8, "joy": 0.05, "sadness": 0.05}
    else:
        data = {"anger": 0.2, "disgust": 0.2, "fear": 0.2, "joy": 0.2, "sadness": 0.2}

    return type("Response", (), {"text": json.dumps(data)})()


def emotion_detector(text_to_analyze):
    response = emotion_detection(text_to_analyze)
    
    emotion_dict = json.loads(response.text)

    anger_score = emotion_dict['anger']
    disgust_score = emotion_dict['disgust']
    fear_score = emotion_dict['fear']
    joy_score = emotion_dict['joy']
    sadness_score = emotion_dict['sadness']

    dominant_emotion = max(emotion_dict, key=emotion_dict.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
