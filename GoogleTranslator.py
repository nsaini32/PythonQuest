# This is a simple translator program in Python using the Google Translate API

# Import the necessary libraries
from googletrans import Translator

# Create a translator object
translator = Translator()

# Get the user input for the text to translate
text = input("Enter the text to translate: ")

# Get the source and target languages from the user
src_lang = input("Enter the source language: ")
dest_lang = input("Enter the destination language: ")

# Translate the text using the Google Translate API
translation = translator.translate(text, src=src_lang, dest=dest_lang)

# Display the translated text
print("Translated text:", translation.text)
