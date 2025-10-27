def download_transcript(transcript, filename="meeting_transcript.txt"):
    with open(filename, "w") as f:
        f.write(transcript)
