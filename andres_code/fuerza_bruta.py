def descifrar(message):
    LETTERS = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
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
        print("Descifrando con key #%s: %s" % (key, translated))

def main():
    message = input("Mensaje Cifrado: ")
    message = message.upper()
    descifrar(message)

if __name__ == '__main__':
    main()
    input()