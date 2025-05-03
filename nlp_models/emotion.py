from transformers import pipeline

emotion_pipeline = pipeline("text-classification", 
                            model="bhadresh-savani/distilbert-base-uncased-emotion", 
                            return_all_scores=True)

def analyze_emotion(text):
    raw_scores = emotion_pipeline(text)[0]
    sorted_scores = sorted(raw_scores, key=lambda x: x['score'], reverse=True)
    top_emotions = {item['label']: round(item['score'], 3) for item in sorted_scores[:3]}
    return top_emotions
