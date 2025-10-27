def fallback_if_low_confidence(response, threshold=0.4):
    score = score_response(response)
    return response if score >= threshold else "Let me rephrase that for clarity."
