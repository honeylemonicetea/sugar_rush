import requests
from bs4 import BeautifulSoup
import sys

from urllib3.exceptions import NewConnectionError

args = sys.argv
languages = ['arabic', 'german', 'english', 'spanish', 'french', 'hebrew', 'japanese', 'dutch', 'polish',
                     'portuguese', 'romanian', 'russian', 'turkish']
headers={'User-Agent': 'Mozilla/5.0'}
try:
    if args[2] != 'all':
        source_lang = args[1]
        target_lang = args[2]
        word = args[3]
        trans = []
        examples = []
        final_t = []
        final_e = []
        index = 0
        r = requests.get(f"https://context.reverso.net/translation/{source_lang}-{target_lang}/{word}", headers=headers)
        if r:
            soup = BeautifulSoup(r.content, "html.parser")
            transl = soup.find_all("div", {"id": "translations-content"})
            exampl = soup.find_all('section', {'id': 'examples-content'})
            for i in exampl:
                i = i.text.replace("\n", " ", 10000).replace("[", "").replace("]", "").strip(' ').split("  ")
            for k in i:
                examples.append(k)
            for k in examples:
                if len(k) > 1:
                    final_e.append(k)
            for i in transl:
                trans.append(i.text)
            trans = " ".join(trans)
            trans = trans.replace("\n", "", 1000000)
            trans = trans.split(' ')
            for word in trans:
                if len(word) > 1:
                    final_t.append(word)
            print("Context examples:\n")
            print(f"{target_lang.title()} Translations:")
            for ind in range(5):
                print(final_t[ind])
            print(f"{target_lang.title()} Examples:")
            for i in range(5):
                print(f"{final_e[index]}:\n{final_e[index + 1].lstrip(' ')}")
                index += 2
        else:
            print(f"Sorry, unable to find {word}")
    elif args[2] == 'all':
        source_lang = args[1]
        word = args[3]

        languages.remove(source_lang)
        for lang in languages:
            trans = []
            examples = []
            final_t = []
            final_e = []
            index = 0
            target_lang = lang
            r = requests.get(f"https://context.reverso.net/translation/{source_lang}-{target_lang}/{word}",
                             headers=headers)
            if r:
                soup = BeautifulSoup(r.content, "html.parser")
                transl = soup.find_all("div", {"id": "translations-content"})
                exampl = soup.find_all('section', {'id': 'examples-content'})
                for i in exampl:
                    i = i.text.replace("\n", " ", 10000).replace("[", "").replace("]", "").strip(' ').split("  ")
                    for k in i:
                        examples.append(k)
                for k in examples:
                    if len(k) > 1:
                        final_e.append(k)
                for i in transl:
                    trans.append(i.text)
                trans = " ".join(trans)
                trans = trans.replace("\n", "", 1000000)
                trans = trans.split(' ')
                for w in trans:
                    if len(w) > 1:
                        final_t.append(w)
                print(f"{target_lang.title()} Translations:")
                print(final_t[0] + "\n")
                print(f"\n{target_lang.title()} Examples:")
                print(f"{final_e[0]}:\n{final_e[1].lstrip(' ')}\n")
                with open(f'{word.upper()}.txt', 'a') as file:
                    file.write(f"{target_lang.title()} Translations:")
                    file.write(final_t[0] + "\n")
                    file.write(f"\n{target_lang.title()} Examples:")
                    file.write(f"{final_e[0]}:\n{final_e[1].lstrip(' ')}\n")
                transl.clear()
                exampl.clear()
                trans.clear()
                examples.clear()
                final_e.clear()
                final_t.clear()
            else:
                print(f"Sorry, unable to find {word}")
except NameError:
    if args[1] not in languages:
        print(f"Sorry, the program doesn't support {args[1]}")
    elif args[2] not in languages:
        print(f"Sorry, the program doesn't support {args[2]}")
except Exception:
    if 400 <= r.status_code < 500:
        print(f"Sorry, unable to find {args[3]}")
    elif r.status_code >=500:
        print("Something wrong with your internet connection")
