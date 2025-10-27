def score_response(response):
    # Dummy confidence scoring based on length
    return min(1.0, len(response) / 100)
