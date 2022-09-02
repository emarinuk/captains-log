from translate import Translator

manual_input = False
console_output = False
my_line = ""
translated_line = ""
list_languages = ["en","ru","es","ja","it","zh"]

source = input("Which file do you want to translate? ")
if not source:
    manual_input = True
    print('Very well. You will be prompted for sentences')
else:
    try:
        source_file = open(source, mode="r")
    except FileNotFoundError as e:
        print(e)

output = input("Which file do you want to copy the translation? ")
if not output:
    console_output = True
    print('Very well. The translation will appear here')
else:
    try:
        translated_file = open(output, mode="a+", encoding="utf-8")
    except FileNotFoundError as e:
        print(e)

lang_in = input("Which language do you want to translate from [en,ru,es,ja,it,zh]? ")
if not lang_in:
    lang_in = "en"

lang_out = input("Which language do you want to translate to [en,ru,es,ja,it,zh]? ")
if not lang_out:
    lang_out = "ja"


translator = Translator(from_lang=lang_in, to_lang=lang_out)

def write(line):
    if not console_output:
        translated_file.write(line + "\n")
    else:
        print(line)

if not manual_input:
    while True:
        my_line = source_file.readline()
        if my_line != "":
            translated_line = translator.translate(my_line)
            write(translated_line)
            continue
        else:
            break
else:
    while True:
        my_line = input("What do you want to translate? ")
        if my_line != "END":
            translated_line = translator.translate(my_line)
            write(translated_line)
            continue
        else:
            break
