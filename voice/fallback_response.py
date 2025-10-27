def generate_fallback(error_type="generic"):
    responses = {
        "generic": "I'm sorry, I couldn't process that.",
        "empty_input": "Please provide some text to speak.",
        "engine_failure": "The voice engine encountered an issue."
    }
    return responses.get(error_type, responses["generic"])

