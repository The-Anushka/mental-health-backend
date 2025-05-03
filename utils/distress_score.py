def get_distress_score(sentiment, emotions):
    score = 0
    if sentiment == 'negative':
        score += 1
    if 'sadness' in emotions:
        score += 1
    if 'anger' in emotions or 'fear' in emotions:
        score += 1
    return score  # 0 (low risk) → 3 (high risk)
def get_distress_score(sentiment, emotions):
    score = 0
    if sentiment == 'negative':
        score += 1
    if 'sadness' in emotions:
        score += 1
    if 'anger' in emotions or 'fear' in emotions:
        score += 1
    return score  # 0 (low risk) → 3 (high risk)
