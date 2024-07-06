import openai
import os

'

def translate(text):
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=f"Translate the following English text to Hungarian: '{text}'",
      max_tokens=60
    )
    return response.choices[0].text.strip()

# Próbáljuk ki a fordítót
english_text = "Hello, how are you?"

english_text = input('Please a sentence:')

hungarian_translation = translate(english_text)
print(hungarian_translation)

