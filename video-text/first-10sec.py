from pydub import AudioSegment

# Betöltjük a WAV fájlt
audio = AudioSegment.from_wav("film.wav")

# Az első 10 másodperc kivágása (10000 millisekundum, mivel a pydub milliszekundumban mér)
first_10_seconds = audio[:10000]

# Az első 10 másodperc exportálása egy új WAV fájlba
first_10_seconds.export("film10.wav", format="wav")
