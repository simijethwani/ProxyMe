BAD_WORDS = ["damn", "hell"]

def filter_profanity(text):
    for word in BAD_WORDS:
        text = text.replace(word, "***")
    return text
