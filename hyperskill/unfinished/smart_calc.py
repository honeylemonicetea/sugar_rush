import collections
#re write the whole proj
operators = "+-*/"
stored_vars = dict()
keys = []


def sorting(line):
    new_list = []
    line = line.split()
    for item in range(len(line)):
        if item % 2 == 0:
            new_list.append(line[item])
        else:
            sign = sign_detector(line[item])
            new_list.append(sign)
    return calculator(new_list)


def calculator(numbers):
    try:
        total = int(numbers[0])

        for ind in range(len(numbers) - 2):
            if numbers[ind + 1] == "+":
                total += int(numbers[ind + 2])
            elif numbers[ind + 1] == "-":
                total -= int(numbers[ind + 2])

        return total
    except ValueError:
        return "Invalid expression"


def help():
    return "The program can add and subtract"


def sign_detector(sign):
    asters = sign.count("*")
    divs = sign.count("/")
    if "-" in sign:
        amount = sign.count("-")
        if amount % 2 == 0:
            return "+"
        else:
            return "-"
    elif "+" in sign:
        return "+"
    elif asters > 1 or divs > 1:
        return "Invalid expression"


def dict_check(pair):
    is_digit = any(k.isdigit() for k in pair)
    pair = pair.replace(" ", "", 100)
    pair = pair.split("=")

    if len(pair) == 2:
        if pair[0].isalpha() == False:
            print("Invalid identifier")
        elif pair[1].isdigit() == False and is_digit == True:  # a3ss like
            print("Invalid assignment")
        elif pair[1].isalpha() == True and pair[1] not in keys:
            print("Invalid assignment")
        else:
            stored_vars[pair[0]] = pair[1]
            keys.append(pair[0])
    else:
        print("Invalid assignment")


def word_check(word):  # there can be two ways, either just one ltter or word or an expression to calculate
    word = word.split()
    if len(word) == 1:
        if word[0] in keys:
            val = stored_vars.get(word[0])
            if val.isalpha() == True:
                nv = stored_vars.get(val)
                return nv
            else:
                return val
        else:
            return "Unknown variable"
    else:
        for i in range(len(word)):
            if word[i].isalpha() == True:
                new_val = stored_vars.get(word[i])
                word[i] = new_val
        word = " ".join(word)
        return sorting(word)


while True:
    user_command = input()
    if len(user_command) > 0:
        if "/" not in user_command and "*" not in user_command:
            if "=" in user_command:
                dict_check(user_command)
            elif user_command[0].isalpha() == False:  # just calculate as usual
                print(sorting(user_command))
            elif user_command[0].isalpha() == True:  # there are letters
                print(word_check(user_command))
            else:
                print("Unknown command")
        elif "*" in user_command or "/" in user_command:
            #check ()
            if "(" in user_command and ")" not in user_command or ")" in user_command and "(" not in user_command:
                print("Invalid expression")
            else:
                infix_to_postfix(user_command)
        else:
            if user_command == "/help":
                print(help())
            elif user_command == "/exit":
                print("bye")
                break
            else:
                print("Unknown command")
