import math
import argparse
import sys


def calc_annual_periods(_principal, _interest, _payment):
    return math.ceil(math.log(_payment / (_payment - _interest * _principal),
                              1 + _interest))


def print_annual_periods(_periods):
    if 0 < periods < 12:
        print("You need {number} {unit} to repay this credit!"
              .format(number=periods,
                      unit="month" if periods == 1 else "months"))
    elif 12 <= periods < 24:
        print("You need 1 year{conj}{num_month}{unit_month}"
              " to repay this credit!"
              .format(num_month="" if periods % 12 == 0 else " " + str(periods
                                                                       % 12),
                      conj="" if periods % 12 == 0 else " and",
                      unit_month="" if periods % 12 == 0
                      else " month" if periods % 12 == 1 else " months"))
    elif periods >= 24:
        print("You need {num_year} years{conj}{num_month}{unit_month}"
              " to repay this credit!"
              .format(num_year=periods // 12,
                      conj="" if periods % 12 == 0 else " and",
                      num_month="" if periods % 12 == 0
                      else " " + str(periods % 12),
                      unit_month="" if periods % 12 == 0
                      else " month" if periods % 12 == 1 else " months"))


def calc_annual_payment(_principal, _interest_, _periods):
    return math.ceil(_principal * (
            (_interest_ * math.pow(1 + _interest_, _periods))
            / (math.pow(1 + _interest_, _periods) - 1)))

# choice = input('''What do you want to calculate?
# type "n" for the count of months,
# type "a" for the annuity monthly payment,
# type "p" for the credit principle:\n''')

# if choice == 'n':
#     # print("Enter the credit principle:\n> ")
#     principle = float(input("Enter the credit principle:\n"))
#     # print("Enter the monthly payment:\n> ")
#     monthly_payment = float(input("Enter the monthly payment:\n"))
#     # print("Enter the credit interest:\n> ")
#     interest = float(input("Enter the credit interest:\n")) / 100
#     interest /= 12  # Convert interest to monthly
#     #     Calculate n
#     periods = math.ceil(
#         math.log(monthly_payment / (monthly_payment - interest * principle),
#                  1 + interest)
#     )
#     if 0 < periods < 12:
#         print("You need {number} {unit} to repay this credit!"
#               .format(number=periods,
#                       unit="month" if periods == 1 else "months"))
#     elif 12 <= periods < 24:
#         print("You need 1 year{conj}{num_month}{unit_month}"
#               " to repay this credit!"
#               .format(num_month="" if periods % 12 == 0 else " " + str(periods
#                                                                        % 12),
#                       conj="" if periods % 12 == 0 else " and",
#                       unit_month="" if periods % 12 == 0
#                       else " month" if periods % 12 == 1 else " months"))
#     elif periods >= 24:
#         print("You need {num_year} years{conj}{num_month}{unit_month}"
#               " to repay this credit!"
#               .format(num_year=periods // 12,
#                       conj="" if periods % 12 == 0 else " and",
#                       num_month="" if periods % 12 == 0
#                       else " " + str(periods % 12),
#                       unit_month="" if periods % 12 == 0
#                       else " month" if periods % 12 == 1 else " months"))
# elif choice == 'a':
#     print("Enter the credit principle:")
#     principle = float(input())
#     print("Enter the number of periods:")
#     periods = int(input())
#     print("Enter the credit interest:")
#     interest = float(input()) / 100
#     interest /= 12  # Convert interest to monthly
#     #     calculate a
#     monthly_payment = math.ceil(
#         principle * (
#             (interest * math.pow(1 + interest, periods))
#             / (math.pow(1 + interest, periods) - 1)
#         )
#     )
#     print("Your annuity payment = {}!".format(monthly_payment))
# elif choice == 'p':
#     print("Enter the monthly payment:")
#     monthly_payment = float(input())
#     print("Enter the count of periods:")
#     periods = int(input())
#     print("Enter the credit interest:")
#     interest = float(input()) / 100
#     interest /= 12
#     #     calculate p
#     principle = round(
#         monthly_payment / (
#             (interest * math.pow(1 + interest, periods))
#             / (math.pow(1 + interest, periods) - 1)
#         )
#     )
#     print("Your credit principle = {}!".format(principle))

#######################################################################################


parser = argparse.ArgumentParser(usage='Calculate differentiate and annuity payment.')
parser.add_argument('--type',
                    choices=['diff', 'annuity'],
                    required=True,
                    help='type of the payment, has two values "diff" or "annuity".')
parser.add_argument('--principal', type=float, help='Amount of the credit principal.')
parser.add_argument('--periods', type=int, help='Number of payments (months).')
parser.add_argument('--interest', type=float, help='Nominal interest rate (in percent).')
parser.add_argument('--payment',
                    help='The monthly payment, '
                         'only acceptable when --type has the value "annuity".')

if len(sys.argv) < 5:
    print('Incorrect parameters')

args = parser.parse_args()
print(args)
print(args.__contains__("type"))
print(args.type)

if args.type == "diff":
    if args.__contains__("payment"):
        print('Incorrect parameters')
        exit(-1)

    if args.__contains__("interest"):
        interest = args.interest

    if args.__contains__("principal"):
        principal = args.principal

    if args.__contains__("periods"):
        periods = args.periods

    # Calculate diff payment and output formatted string

else:
    # annuity payment
    if ~args.__contains__("principal"):
        interest = args.interest / 1200
        periods = args.periods
        payment = args.payment

        # calculate principal
        principal = round(
            payment / (
                (interest * math.pow(1 + interest, periods))
                / (math.pow(1 + interest, periods) - 1)
            )
        )
        print("Your credit principal = {}!".format(principal))
    elif ~args.__contains__("periods"):
        principal = args.principal
        interest = args.interest / 1200
        payment = args.payment
        # Calculate periods
        periods = calc_annual_periods(principal, interest, payment)
        print_annual_periods(periods)
    elif ~args.__contains__("payment"):
        principal = args.principal
        interest = args.interest / 1200
        periods = args.periods
        # Calculate payment
        payment = calc_annual_payment(principal, interest, periods)
        print("Your annuity payment = {}!".format(payment))
