from PyPDF2 import PdfReader
from gtts import gTTS

# PDF fájl megnyitása
f = input('Please give me the pdf name:')
#pdf_file = open(f, 'rb')
pdf_reader = PdfReader( f  )

# Összes oldal szövegének összegyűjtése
text = ""
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages(page_num)
    text += page.extract_text()

# Szöveg felolvasása
tts = gTTS(text, lang='hu')
tts.save('output.mp3')

