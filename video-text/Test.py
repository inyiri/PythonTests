import speech_recognition as sr

# Példányosítunk egy felismerőt (recognizer)
recognizer = sr.Recognizer()

# Megnyitjuk az audiófájlt (például 'audio_file.wav')
with sr.AudioFile('film10.wav') as source:
    # Hallgatjuk meg az audióforrást és felvesszük az audiót
    audio_data = recognizer.record(source)

    # Megpróbáljuk átalakítani az audiót szöveggé a Google Web Speech API segítségével
    try:
        print("Eddig elértem")
        text = recognizer.recognize_google(audio_data, language="en-EN")  # Használja a megfelelő nyelvi kódot
        print(f"A felismert szöveg: {text}")
    except sr.UnknownValueError:
        # Ha a felismerő nem tudja értelmezni az audiót
        print("A Google Web Speech API nem tudta értelmezni az audiót.")
    except sr.RequestError as e:
        # Ha valami hiba történt a kérés során
        print(f"A kérés során hiba történt; {e}")
