import whisper

model = whisper.load_model("base")
result = model.transcribe("afrikaans1.mp3")
print(result["text"])