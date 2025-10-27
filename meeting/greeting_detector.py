GREETING_KEYWORDS = ["hello", "hi", "good morning", "good afternoon", "hey"]

def detect_greeting(transcript):
    return any(word in transcript.lower() for word in GREETING_KEYWORDS)
