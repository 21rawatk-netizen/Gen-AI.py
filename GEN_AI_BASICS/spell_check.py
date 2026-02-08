# Perform the translation
translation = translator.translate(text)

# Print the translated text
print('Translated Text:', translation)
text = 'I love progamming and machine learnig.'
blob = TextBlob(text)
corrected_text = blob.correct()

# Print the corrected text
print('Original Text:', text)
print('Corrected Text:', corrected_text)
