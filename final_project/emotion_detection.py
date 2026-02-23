def emotion_detector(text_to_analyze):
    response = emotion_detection(text_to_analyze)
    return response.text
