"""
Two functions that translate text from English to French and vice versa
"""
from deep_translator import MyMemoryTranslator
def english_to_french(english_text):
    '''function translates English Text to French Text'''
    french_text = MyMemoryTranslator(source="en-GB", target="fr-FR").translate(english_text)
    return french_text

def french_to_english(french_text):
    '''function translates French Text to English Text'''
    english_text = MyMemoryTranslator(source="fr-FR", target="en-GB").translate(french_text)
    return english_text
