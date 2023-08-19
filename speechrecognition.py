import speech_recognition as sr
A=("./static/audio.wav")
r=sr.Recognizer()
with sr.AudioFile(A) as source:
    audio=r.record(source)
try:
    print(r.recognize_google(audio))
except sr.UnknownValueError:
    print("couldn't understand the audio")
except sr.RequestError:
    print("couldn't get the results")
    