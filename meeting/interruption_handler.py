def detect_interruption(speaker_segments):
    # Analyze overlapping timestamps
    return [seg for seg in speaker_segments if seg['overlap']]
