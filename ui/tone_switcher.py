def switch_tone(current_tone):
    tones = ["formal", "casual", "friendly"]
    next_tone = tones[(tones.index(current_tone) + 1) % len(tones)]
    return next_tone
