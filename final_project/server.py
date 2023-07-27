from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    text_to_translate = request.args.get('text_to_translate')
    def english_to_french(englishtext):
        translated = MyMemoryTranslator(source="en-GB",target="fr-FR").translate(english_text)
        return translated
    return "Translated text to French"

@app.route("/frenchToEnglish")
def french_english():
    text_to_translate = request.args.get('text_to_translate')
    def french_to_english(french_text):
        translated = MyMemoryTranslator(source="fr-FR",target="en-GB").translate(french_text)
        return translated
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
