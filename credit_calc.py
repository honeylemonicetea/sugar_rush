import math
import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment", type=int)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
args = parser.parse_args()
if len(sys.argv) < 5:
    print("Incorrect parameters")
elif args.interest == None or args.type == None:
    print("Incorrect parameters")
elif args.principal == None and args.payment == None or args.payment == None and args.periods == None or args.periods == None and args.principal == None:
    print("Incorrect parameters")
elif args.principal == None and args.payment == None and args.periods == None:
    print("Incorrect parameters")
elif len(sys.argv) == 5 and args.interest != None:
    if args.type == 'annuity':
        if args.payment != None and args.payment> 0 and args.periods != None and args.periods > 0 and args.interest != None and args.interest > 0:
            # calculating principal here
            nom_int = args.interest / (12 * 100)
            p = args.payment / ((nom_int * pow(1 + nom_int, args.periods) /(pow(1 + nom_int, args.periods) - 1)))
            if int(p) < p:
                p = int(p) + 1
            print("Your credit principal = {}!".format(p))
            overp = p - args.payment * args.periods
            print()
            print("Overpayment = {}".format(overp))
            # calculating periods
        elif args.payment != None and args.payment > 0 and args.principal != None and args.principal > 0 and args.interest != None and args.interest > 0:
            nom_int = args.interest / (12 * 100)
            n = math.log((args.payment / (args.payment - nom_int * args.principal)), 1 + nom_int)
            if int(n) < n:
                n = int(n) + 1
            if n >= 12:
                year = n // 12
                mon = n - (year * 12)
                if mon > 1 and year > 1:
                    print("You need {} years and {} months to repay this credit!".format(year, mon))
                elif mon < 1 and year > 1:
                    print("You need {} years to repay this credit!".format(year))
                elif year == 1 and mon > 1:
                    print("You need {} year and {} months to repay this credit!".format(year, mon))
                elif mon < 1 and year == 1:
                    print("You need {} year to repay this credit!".format(year))
            elif 1 < n < 12:
                print("You need {} months to repay this credit!".format(int(n)))
            elif n >= 1:
                print("You need {} month to repay this credit!".format(int(n)))
            overp = args.principal - args.payment * n
            print()
            print("Overpayment = {}".format(overp))
        # calculating annuity payment
        elif args.periods != None  and args.periods > 0 and args.principal != None and args.principal > 0 and args.interest != None and args.interest > 0:
            nom_int = args.interest / (12 * 100)
            a = args.principal *((nom_int * pow(1+nom_int, args.periods) / (pow(1+nom_int, args.periods) - 1)))
            if int(a) < a:
                a = int(a) + 1
            print("Your annuity payment = {}!".format(a))
            overp = args.principal - a * args.periods
            print()
            print("Overpayment = {}".format(overp))
        else:
            print("Incorrect parameters")
    elif args.type == 'diff':
        if args.principal != None and args.principal > 0 and args.interest != None and args.interest > 0 and args.periods > 0:
            totalp = 0
            nom_int = args.interest / (12 * 100)
            for i in range(1, args.periods + 1):
                d = args.principal / args.periods + nom_int * (args.principal - args.principal * (i - 1) / args.periods)
                if int(d) < d:
                    d = int(d) + 1
                print("Month {}: paid out {}".format(i, d))
                totalp += d
            overp = args.principal - totalp
            print()
            print("Overpayment = {}".format(overp))
        else:
            print("Incorrect parameters")
