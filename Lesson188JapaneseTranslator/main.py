from translate import Translator

try:
    source_file = open("source_file.txt", mode="r")
except FileNotFoundError as e:
    print(e)

translated_file = open("translated_file.txt", mode="a+", encoding="utf-8")

my_line = ""
translated_line = ""

translator = Translator(to_lang="es")
while True:
    my_line = source_file.readline()
    if my_line != "":
        translated_line = translator.translate(my_line)
        print(translated_line)
        translated_file.write(translated_line+ "\n")
        continue
    else:
        break

