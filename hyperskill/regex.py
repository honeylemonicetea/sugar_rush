# write your code here
import sys

sys.setrecursionlimit(10000)


def commoncause(reg, inpt):
    # if length of both lists is zero, they're consumed, return True
    if len(reg) == 0:
        return "True"
    elif len(reg) == 0 and len(inpt) == 0:
        return 'True'
    elif len(inpt) < len(reg):
        return 'False'
    else:
        if len(inpt) > len(reg) and reg[0] != '.' and reg[0] != inpt[0]:
            inpt.remove(inpt[0])
            return commoncause(reg, inpt)
        elif reg[0] == '.' or reg[0] == inpt[0] and len(reg) > 1:
            reg.remove(reg[0])
            inpt.remove(inpt[0])
            return commoncause(reg, inpt)
        elif reg[0] == '.' or reg[0] == inpt[0] and len(reg) == 1:
            return "True"
        elif len(inpt) == len(reg) and inpt[0] != reg[0]:
            return "False"


def regexbeginning(reg, inpt):
    # if length of both lists is zero, they're consumed, return True
    if len(reg) == 0 or " " in reg:
        return "True"
    elif len(reg) == 0 and len(inpt) == 0:
        return 'True'
    elif len(inpt) < len(reg):
        return 'False'
    elif reg[0] != '.' and inpt[0] != reg[0]:
        return "False"
    else:
        if reg[0] == '.' or reg[0] == inpt[0] and len(reg) > 1:
            reg.remove(reg[0])
            inpt.remove(inpt[0])
            return regexbeginning(reg, inpt)
        elif reg[0] == '.' or reg[0] == inpt[0] and len(reg) == 1:
            return "True"
        elif len(inpt) == len(reg) and inpt[0] != reg[0]:
            return "False"


def regexend(reg, inpt):
    if len(reg) == 0:
        return "True"
    elif len(reg) == 0 and len(inpt) == 0:
        return 'True'
    elif len(inpt) < len(reg):
        return 'False'
    elif reg[-1] != '.' and inpt[-1] != reg[-1]:
        return "False"
    else:
        if reg[-1] == '.' or reg[-1] == inpt[-1] and len(reg) > 1:
            reg.remove(reg[-1])
            inpt.remove(inpt[-1])
            return regexend(reg, inpt)
        elif reg[-1] == '.' or reg[-1] == inpt[-1] and len(reg) == 1:
            return "True"
        elif len(inpt) == len(reg) and inpt[-1] != reg[-1]:
            return "False"


def recursiveregex(reg, inpt):
    if len(reg) > 0:
        if reg[0] == "^" and reg[-1] == "$":
            reg.remove("^")
            reg.remove("$")
            return reg == inpt
        elif reg[0] == "^":
            reg.remove("^")
            return regexbeginning(reg, inpt)
        elif reg[-1] == "$":
            reg.remove("$")
            return regexend(reg, inpt)

        else:
            return commoncause(reg, inpt)
    else:
        return commoncause(reg, inpt)

def repeat_controller(regex):
    regex = regex.split("|")
    reg = list(regex[0])
    inpt = list(regex[1])
    if "?" in reg:  # zero or once
        sp = regex[0].find("?") - 1
        if reg[sp] == '.' or reg[sp] == inpt[sp]:  # means that they match once
            reg.remove("?")
            reg.remove(reg[sp])
            inpt.remove(inpt[sp])
            if "^" not in reg and "$" not in reg:
                return regexbeginning(reg, inpt)
            else:
                return recursiveregex(reg, inpt)
        else:  # they don't match
            reg.remove("?")
            reg.remove(reg[sp])
            if "^" not in reg and "$" not in reg:
                return regexbeginning(reg, inpt)
            else:
                return recursiveregex(reg, inpt)
    # ? works
    elif "*" in reg:  # zero or more
        # negative index of the preceding character
        leng = len(reg)
        reg_loc = regex[0].find("*")
        sp = - (leng - (reg_loc - 1))
        if reg[sp] == "." or reg[sp] == inpt[sp + 1]:
            letter = inpt[sp + 1]
            start = len(inpt) + (sp + 1)
            for i in range(start, 0, -1):
                if inpt[i] == letter:
                    inpt.remove(inpt[i])
            reg.remove("*")
            reg.remove(reg[reg_loc - 1])
            if "^" not in reg and "$" not in reg:
                return regexbeginning(reg, inpt)
            else:
                return recursiveregex(reg, inpt)
        else:
            reg.remove("*")
            reg.remove(reg[reg_loc - 1])
            if "^" not in reg and "$" not in reg:
                return regexbeginning(reg, inpt)
            else:
                return recursiveregex(reg, inpt)
    elif "+" in reg:  # once or more
        leng = len(reg)
        reg_loc = regex[0].find("+")
        sp = - (leng - (reg_loc - 1))
        if reg[-1] != "$" and reg[0] != '^':
            if reg[sp] == "." or reg[sp] == inpt[sp + 1]:
                letter = inpt[sp + 1]
                start = len(inpt) + (sp + 1)
                for i in range(start, 0, -1):
                    if inpt[i] == letter:
                        inpt.remove(inpt[i])
                reg.remove("+")
                reg.remove(reg[reg_loc - 1])
                return regexbeginning(reg, inpt)
            else:
                reg.remove("+")
                return regexbeginning(reg, inpt)
        else:
            if reg[0] == "^" and reg[-1] != "$":  # the case from ?
                sp = regex[0].find("+") - 1
                if reg[sp] == '.' or reg[sp] == inpt[sp - 1]:
                    letter = inpt[sp - 1]
                    for i in range(sp - 1, len(inpt)):
                        if inpt[i] == letter:
                            inpt.remove(inpt[i])
                        else:
                            break
                    reg.remove(reg[sp])
                    reg.remove("+")
                    return recursiveregex(reg, inpt)
            elif reg[-1] == "$" and reg[0] != "^":
                sp = regex[0].find("+") - 1
                if reg[sp] == '.' or reg[sp] == inpt[sp]:
                    letter = inpt[sp]
                    for i in range(sp, len(inpt)):
                        if inpt[i] == letter:
                            inpt.remove(inpt[i])
                        else:
                            break
                    reg.remove(reg[sp])
                    reg.remove("+")
                    return recursiveregex(reg, inpt)
            elif reg[0] == "^" and reg[-1] == "$":
                sp = regex[0].find("+") - 1
                if reg[sp] == '.' or reg[sp] == inpt[sp - 1]:
                    letter = inpt[sp - 1]
                    l = len(inpt)
                    for k in range(4):
                        for i in range(sp - 1, l):
                            if inpt[i] == letter:
                                inpt.remove(inpt[i])
                            else:
                                break
                    reg.remove(reg[sp])
                    reg.remove("+")
                    return recursiveregex(reg, inpt)

    else:
        return recursiveregex(reg, inpt)
def escape(regex):
    regex = regex.split("|")
    reg = list(regex[0])
    inpt = list(regex[1])
    if '\\' in reg:
        esc = regex[0].find("\\")
        next = reg[esc + 1]
        if next in inpt:
            reg.remove("\\")
            reg.remove(next)
            inpt.remove(next)
            r= "".join(reg)
            i = "".join(inpt)
            re = r + "|" + i
            return repeat_controller(re)
        else:
            return "False"
    else:
        r = "".join(reg)
        i = "".join(inpt)
        re = r + "|" + i
        return repeat_controller(re)
print(escape(input()))
