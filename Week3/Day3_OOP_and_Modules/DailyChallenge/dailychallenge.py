from googletrans import Translator


def translate(words):
    translator = Translator()
    translations = {}
    for word in words:
        translations[word] = translator.translate(word, src='fr',dest="en").text
    return translations


translation = translate(["Bonjour", "Au revoir", "Bienvenue", "A bientôt"])
print(translation)
