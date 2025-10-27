from elevenlabs import generate, play, save

def synthesize_voice(text, voice_id="ayush_voice", style="neutral"):
    audio = generate(text=text, voice=voice_id, model="eleven_monolingual_v1", style=style)
    save(audio, "output.wav")
    return "output.wav"
