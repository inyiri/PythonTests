from gtts import gTTS
tts = gTTS('Az én kedvesem egy aranyos hölgy, Ildikó', lang='hu')
tts.save('hello.mp3')
