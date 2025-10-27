# fastapi_app.py
from fastapi import FastAPI, Request
from voice.tts_engine import synthesize_voice
from llm.prompt_preprocessor import clean_prompt

app = FastAPI()

@app.post("/transcribe")
async def transcribe(request: Request):
    data = await request.json()
    prompt = clean_prompt(data["text"])
    response_path = synthesize_voice(prompt)
    return {"audio_path": response_path}
