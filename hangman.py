import random
import string
print("H A N G M A N")
while True:
    user_action = input('Type "play" to play the game, "exit" to quit:')
    print()
    if user_action == "play":
        words = ['python', 'java', 'kotlin', 'javascript']
        w = random.choice(words)
        lw = len(w)
        repl = lw * "-"
        wrongs = set()
        finding = list(repl)
        alphabet_l = string.ascii_lowercase
        tries = 8
        print("{}".format(repl))
        user_letter = input("Input a letter:")
        while tries > 0:
            if len(user_letter) == 1 and user_letter in alphabet_l:
                if user_letter in w and user_letter not in wrongs:
                    for i in range(lw):
                        if user_letter == w[i]:
                            finding[i] = user_letter
                    wrongs.add(user_letter)
                elif user_letter in wrongs:
                    print("You already typed this letter")
                elif user_letter not in w and user_letter not in wrongs:
                    print("No such letter in the word")
                    tries -= 1
                    wrongs.add(user_letter)
                k = "".join(finding)
                if "-" not in k and tries > 0:
                    #isis: o_O
                    print()
                    print("{}".format(k))
                    print("You guessed the word!")
                    print("You survived!")
                    print()
                    break
                elif tries == 0 and "-" in k:
                    print("You are hanged!")
                    print()
                    break
                elif tries > 0 and "-" in k:
                    print()
                    print("{}".format(k))
                    user_letter = input("Input a letter:")
            elif len(user_letter) != 1 and tries > 0:
                print("You should input a single letter")
                print()
                k = "".join(finding)
                print("{}".format(k))
                user_letter = input("Input a letter:")
            elif user_letter not in alphabet_l and tries > 0:
                print("It is not an ASCII lowercase letter")
                print()
                k = "".join(finding)
                print("{}".format(k))
                user_letter = input("Input a letter:")
    elif user_action == "exit":
        break
    else:
        continue
