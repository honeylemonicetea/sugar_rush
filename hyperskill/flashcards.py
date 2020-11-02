import io
import random
import argparse
import sys
from nltk.tokenize import regexp_tokenize


parser = argparse.ArgumentParser()
parser.add_argument('--import_from')
parser.add_argument("--export_to")
args = parser.parse_args()

buf = io.StringIO()

# Write your code here
cards = dict() # term - definition
defs = dict() #definition - term
terms_list = []
definitions_list = []
errors = dict() #initialize with card - 0

def create_cards():
    global cards
    global terms_list
    global definitions_list
    print(f"The card:")
    card = input()
    while card in terms_list:
        print(f'The card "{card}" already exists')
        card = input()
    terms_list.append(card)
    print(f"The definition of the card:")
    definition = input()
    while definition in definitions_list:
        print(f'The definition "{definition}" already exists.')
        definition = input()
    definitions_list.append(definition)
    cards[card] = definition
    defs[definition] = card
    errors[card] = 0
    print(f"The pair (\"{card}\":\"{definition}\") has been added")

def remove_card():
    print("Which card?")
    remove_c = input()
    try:
        terms_list.remove(remove_c) #removes term from list
        del_def = cards.get(remove_c) #get definition
        definitions_list.remove(del_def)  # remove definition from list
        cards.pop(remove_c) # removes term - def from dictionary
        defs.pop(del_def) # removes def -  term from another dict
        print("The card has been removed.")
    except Exception:
        print(f"Can't remove \"{remove_c}\": there is no such card.")

def test_knowledge(times):
    global cards
    global errors
    try:
        for i in range(times):
            term = random.choice(terms_list)
            print(f"Print the definition of \"{term}\"")
            answer = input()
            value = cards.get(term)
            if answer == value:
                print("Correct!")
            elif answer in definitions_list:
                print(f"Wrong. The right answer is \"{value}\", but your definition is correct for \"{defs.get(answer)}\".")
                errors[term] += 1
            else:
                print(f"Wrong. The right answer is \"{value}\"")
                errors[term] += 1
    except Exception:
        pass

def import_card():
    print("File name:")
    file_name = input()
    try:
        with open(file_name, "r") as file:
            cards = file.readline()
        cards = cards.split(",")
        card_num = len(cards)
        print(f"{card_num} cards have been loaded.")
    except FileNotFoundError:
        print("File not found.")

def export_card():
    print("File name:")
    file_name = input()
    with open(file_name, "a") as file:
        file.write(str(cards))
    card_n = len(cards)
    print(f"{card_n} cards have been saved.")

def ask():
    print("How many times to ask?")
    times = int(input())
    test_knowledge(times)

def log():
    global buf
    print("File name:")
    file_name = input()
    with open(file_name, "w") as log:
        log.write(str(buf))
    print("The log has been saved.")

def hardest_card():
    global errors
    hardest = []
    try:
        keys = errors.values() #finding the larest number of mistakes
        max_n = max(list(keys))
        for key, value in errors.items():
            if value == max_n:
                hardest.append(key)
        if max_n == 0:
            print("There are no cards with errors.")
        else:
            if len(hardest) == 1:
                print(f"The hardest card is \"{hardest[0]}\". You have {max_n} errors answering it.")
            else:
                print("The hardest cards are", end="")
                for i in range(len(hardest) - 1):
                    print(f"\"{hardest[i]}\"", end=",")
                print(f"\"{hardest[-1]}\".  You have {max_n} errors answering them.")
    except Exception:
        print("There are no cards with errors.")

def reset_stats():
    global errors
    for key in errors.keys():
        errors[key] = 0
    print("Card statistics has been reset.")
    #clear the errors dict

if args.import_from != None:
    file_n = args.import_from
    try:
        with open(file_n, "r") as file:
            line = file.readline()
        line = regexp_tokenize(line, "[A-z]+")
        length = len(line) // 2
        ctr = 0
        for i in range(length):
            terms_list.append(line[ctr])
            definitions_list.append(line[ctr + 1])
            cards[line[ctr]] = line[ctr + 1]
            defs[line[ctr + 1]] = line[ctr]
            ctr += 2
        print(cards)
        print(f"{length} cards have been loaded.")
    except FileNotFoundError:
        pass

while True:
    print("Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):")
    action = input()
    if action == "add":
        create_cards()
    elif action == "remove":
        remove_card()
    elif action == "import":
        import_card()
    elif action == "export":
        export_card()
    elif action == "ask":
        ask()
    elif action=="log":
        log()
    elif action == "hardest card":
        hardest_card()
    elif action == "reset stats":
        reset_stats()
    elif action == "exit":
        print("Bye bye!")
        if args.export_to != None:
            file_name = args.export_to
            try:
                with open(file_name, "a") as file:
                    file.write(str(cards))
                card_n = len(cards)
                print(f"{card_n} cards have been saved.")
            except Exception:
                pass

        break
