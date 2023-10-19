from __future__ import print_function
import nltk

nltk.download("words")
nltk.download("punkt")

from nltk.corpus import words

def is_english_word(word):
    english_words = set(words.words())
    return word.lower() in english_words

def is_spanish_word(word):
    # Agregar un conjunto de palabras en español aquí o usar una biblioteca similar
    spanish_words = {"hola", "adiós", "gracias", "por favor"}  # Ejemplo de algunas palabras en español
    return word.lower() in spanish_words

def analyze_translations(translations):
    for key, translated in translations:
        words_in_translation = translated.split()
        meaningful_words = []

        for word in words_in_translation:
            if is_english_word(word) or is_spanish_word(word):
                meaningful_words.append(word)

        if meaningful_words:
            print(f"Descifrando con Key #{key}: {' '.join(meaningful_words)}")

def descifrar(message):
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    translations = []
    for key in range(len(LETTERS)):
        translated = ""
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + symbol
        translations.append((key, translated))
    
    analyze_translations(translations)

def main():
    message = input("Mensaje Cifrado: ")
    message = message.upper()
    descifrar(message)

if __name__ == '__main__':
    main()
    input()
