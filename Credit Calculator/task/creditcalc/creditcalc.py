import math
import argparse
import sys


def calc_annual_periods(_principal, _interest, _payment):
    return math.ceil(math.log(_payment / (_payment - _interest * _principal),
                              1 + _interest))


def print_annual_periods(_periods):
    if 0 < periods < 12:
        print("It will take {number} {unit} to repay this credit!"
              .format(number=periods,
                      unit="month" if periods == 1 else "months"))
    elif 12 <= periods < 24:
        print("It will take 1 year{conj}{num_month}{unit_month}"
              " to repay this credit!"
              .format(num_month="" if periods % 12 == 0 else " " + str(periods
                                                                       % 12),
                      conj="" if periods % 12 == 0 else " and",
                      unit_month="" if periods % 12 == 0
                      else " month" if periods % 12 == 1 else " months"))
    elif periods >= 24:
        print("It will take {num_year} years{conj}{num_month}{unit_month}"
              " to repay this credit!"
              .format(num_year=periods // 12,
                      conj="" if periods % 12 == 0 else " and",
                      num_month="" if periods % 12 == 0
                      else " " + str(periods % 12),
                      unit_month="" if periods % 12 == 0
                      else " month" if periods % 12 == 1 else " months"))


def calc_annual_payment(_principal, _interest, _periods):
    return math.ceil(_principal * (
            (_interest * math.pow(1 + _interest, _periods))
            / (math.pow(1 + _interest, _periods) - 1)))


def calc_diff_payment(_principal, _interest, _periods):
    _payment = []
    for i in range(1, _periods + 1):
        d_i = math.ceil(
            _principal / _periods
            + _interest * (_principal - (_principal * (i - 1)) / _periods)
        )
        _payment.append(d_i)
    over_payment = sum(_payment) - _principal
    _payment.append(over_payment)
    return _payment


def print_diff_payment(_payment):
    for i in range(0, len(_payment) - 1):
        print("Month {month}: payment is {money}".format(month=i + 1, money=_payment[i]))

    print("\nOverpayment = {}".format(int(_payment[len(_payment) - 1])))


parser = argparse.ArgumentParser(usage='Calculate differentiate and annuity payment.')
parser.add_argument('--type',
                    choices=['diff', 'annuity'],
                    required=True,
                    help='type of the payment, has two values "diff" or "annuity".')
parser.add_argument('--principal', type=float, help='Amount of the credit principal.')
parser.add_argument('--periods', type=int, help='Number of payments (months).')
parser.add_argument('--interest', type=float, help='Nominal interest rate (in percent).')
parser.add_argument('--payment',
                    type=float,
                    help='The monthly payment, '
                         'only acceptable when --type has the value "annuity".')

if len(sys.argv) < 5:
    print('Incorrect parameters')
    exit(-1)

args = parser.parse_args()

if args.type == "diff":
    if args.payment is None:
        interest = args.interest / 1200
        principal = args.principal
        periods = args.periods

        if interest * principal * periods < 0:
            print("Incorrect parameters")
            exit(-1)

        # Calculate diff payment and output formatted string
        payment = calc_diff_payment(principal, interest, periods)
        print_diff_payment(payment)
    else:
        print("Incorrect parameters")
        exit(-1)

else:
    # annuity payment
    if args.principal is None:
        interest = args.interest / 1200
        periods = args.periods
        payment = args.payment

        if interest * periods * payment < 0:
            print("Incorrect parameters")
            exit(-1)

        # calculate principal
        principal = math.floor(
            payment / (
                (interest * math.pow(1 + interest, periods))
                / (math.pow(1 + interest, periods) - 1)
            )
        )
        print("Your credit principal = {}!".format(principal))
        print("Overpayment = {}".format(int(payment * periods - principal)))
    elif args.periods is None:
        principal = args.principal
        interest = args.interest / 1200
        payment = args.payment

        if principal * interest * payment < 0:
            print("Incorrect parameters")
            exit(-1)

        # Calculate periods
        periods = calc_annual_periods(principal, interest, payment)
        print_annual_periods(periods)
        print("Overpayment = {}".format(int(payment * periods - principal)))
    elif args.payment is None:
        principal = args.principal
        interest = args.interest / 1200
        periods = args.periods
        # Calculate payment
        payment = calc_annual_payment(principal, interest, periods)
        print("Your annuity payment = {}!".format(payment))
