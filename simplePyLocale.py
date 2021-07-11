import json
from pathlib import Path

language = 'en'
translates = None
langfile = None

def set_language(lang):
    global language
    language = lang

def set_language_file(file):
    global langfile
    langfile = Path(Path(__file__).parents[1].resolve(), file)

def read_translates():
    global translates
    with open(langfile, 'r', encoding='utf-8') as f:
        try:
            translates = json.loads(f.read())
        except json.JSONDecodeError as e:
            print('The translation file contains invalid JSON')
            exit()

def translate(text, dict = 'general'):
    if translates == None:
        read_translates()
    if language in translates:
        lang_dict = translates[language][dict]
        if text in lang_dict:
            return lang_dict[text]

    return text