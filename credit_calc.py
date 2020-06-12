import math
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--type")
parser.add_argument("--payment", type=int)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest")

args = parser.parse_args()

if args.type == "annuity":
    if not args.interest:
        print("Incorrect parameters")
    elif not args.principal:
        i = float(args.interest) / (12 * 100)
        args.principal = math.floor(args.payment / (i * ((1 + i) ** args.periods) / (((1 + i) ** args.periods) - 1)))
        print(f"Your credit principal = {args.principal}!")
        annuity = args.principal * ((i * (1 + i) ** args.periods) / ((1 + i) ** args.periods - 1))
        overpayment = math.ceil(annuity) * args.periods - args.principal
        print(f"Overpayment = {overpayment}")
    elif not args.periods:
        i = float(args.interest) / (12 * 100)
        args.periods = math.log((args.payment / (args.payment - i * args.principal)), (1 + i))
        args.periods = math.ceil(args.periods)
        if args.periods > 11:
            years = args.periods // 12
            month = args.periods % 12
            if years == 1 and month == 0:
                print(f"You need {years} year to repay this credit!")
            elif month == 0:
                print(f"You need {years} years to repay this credit!")
            elif month == 1:
                print(f"You need {years} years and {month} month to repay this credit!")
            else:
                print(f"You need {years} years and {month} months to repay this credit!")
        else:
            if args.periods == 1:
                print(f"You need {args.periods} month to repay this credit!")
            else:
                print(f"You need {args.periods} months to repay this credit!")
        overpayment = args.payment * args.periods - args.principal
        print(f"Overpayment = {overpayment}")
    else:
        i = float(args.interest) / (12 * 100)
        annuity = args.principal * ((i * (1 + i) ** args.periods) / ((1 + i) ** args.periods - 1))
        print(f"Your annuity payment = {math.ceil(annuity)}!")
        overpayment = math.ceil(annuity) * args.periods - args.principal
        print(f"Overpayment = {overpayment}")

elif args.type == "diff":
    if not args.interest:
        print("Incorrect parameters")
    else:
        i = float(args.interest) / (12 * 100)
        m = 1
        overpayment = 0
        for j in range(args.periods):
            differ = args.principal / args.periods + i * (args.principal - (args.principal * (m - 1)) / args.periods)
            print(f"Month {m}: paid out {math.ceil(differ)}")
            overpayment += math.ceil(differ)
            m += 1
        print()
        print(f"Overpayment = {overpayment - args.principal}")
else:
    print("Incorrect parameters")

type_calc = ""
if type_calc == "n":
    credit_principal = int(input("Enter the credit principal: "))
    monthly_pay = int(input("Enter monthly payment: "))
    credit_interest = int(input("Enter credit interest: "))

    i = credit_interest / (12 * 100)
    n_periods = math.log((monthly_pay / (monthly_pay - i * credit_principal)), (1 + i))
    n_periods = math.ceil(n_periods)
    if n_periods > 11:
        years = n_periods // 12
        month = n_periods % 12
        if years == 1 and month == 0:
            print(f"You need {years} year to repay this credit!")
        elif month == 0:
            print(f"You need {years} years to repay this credit!")
        elif month == 1:
            print(f"You need {years} years and {month} month to repay this credit!")
        else:
            print(f"You need {years} years and {month} months to repay this credit!")
    else:
        if n_periods == 1:
            print(f"You need {n_periods} month to repay this credit!")
        else:
            print(f"You need {n_periods} months to repay this credit!")

elif type_calc == "a":
    credit_principal = int(input("Enter the credit principal: "))
    n_periods = int(input("Enter count of periods: "))
    credit_interest = int(input("Enter credit interest: "))

    i = credit_interest / (12 * 100)
    annuity = credit_principal * ((i * (1 + i) ** n_periods) / ((1 + i) ** n_periods - 1))
    print(f"Your annuity payment = {math.ceil(annuity)}!")

elif type_calc == "p":
    monthly_pay = float(input("Enter monthly payment: "))
    n_periods = int(input("Enter count of periods: "))
    credit_interest = float(input("Enter credit interest: "))
    i = credit_interest / (12 * 100)
    credit_principal = monthly_pay / (i * ((1 + i) ** n_periods) / (((1 + i) ** n_periods) - 1))
    print(f"Your credit principal = {round(credit_principal)}!")

