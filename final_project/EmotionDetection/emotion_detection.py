import json

def emotion_detection(text_to_analyze):
    # This simulates the API response text (Replace with actual API call if needed)
    return type("Response", (), {
        "text": json.dumps({
            "anger": 0.1,
            "disgust": 0.05,
            "fear": 0.1,
            "joy": 0.65,
            "sadness": 0.1
        })
    })()

def emotion_detector(text_to_analyze):
    response = emotion_detection(text_to_analyze)
    
    # Convert JSON text to dictionary
    emotion_dict = json.loads(response.text)

    # Extract emotion scores
    anger_score = emotion_dict['anger']
    disgust_score = emotion_dict['disgust']
    fear_score = emotion_dict['fear']
    joy_score = emotion_dict['joy']
    sadness_score = emotion_dict['sadness']

    # Find dominant emotion
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)

    # Return required format
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }