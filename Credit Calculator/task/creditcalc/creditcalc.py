import math

# print('''What do you want to calculate?
# type "n" for the count of months,
# type "a" for the annuity monthly payment,
# type "p" for the credit principle:''')
# print("> ")
choice = input('''What do you want to calculate?
type "n" for the count of months,
type "a" for the annuity monthly payment,
type "p" for the credit principle:\n''')

if choice == 'n':
    # print("Enter the credit principle:\n> ")
    principle = float(input("Enter the credit principle:\n"))
    # print("Enter the monthly payment:\n> ")
    monthly_payment = float(input("Enter the monthly payment:\n"))
    # print("Enter the credit interest:\n> ")
    interest = float(input("Enter the credit interest:\n")) / 100
    interest /= 12  # Convert interest to monthly
    #     Calculate n
    periods = math.ceil(
        math.log(monthly_payment / (monthly_payment - interest * principle),
                 1 + interest)
    )
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
elif choice == 'a':
    print("Enter the credit principle:")
    principle = float(input())
    print("Enter the number of periods:")
    periods = int(input())
    print("Enter the credit interest:")
    interest = float(input()) / 100
    interest /= 12  # Convert interest to monthly
    #     calculate a
    monthly_payment = math.ceil(
        principle * (
            (interest * math.pow(1 + interest, periods))
            / (math.pow(1 + interest, periods) - 1)
        )
    )
    print("Your annuity payment = {}!".format(monthly_payment))
elif choice == 'p':
    print("Enter the monthly payment:")
    monthly_payment = float(input())
    print("Enter the count of periods:")
    periods = int(input())
    print("Enter the credit interest:")
    interest = float(input()) / 100
    interest /= 12
    #     calculate p
    principle = round(
        monthly_payment / (
            (interest * math.pow(1 + interest, periods))
            / (math.pow(1 + interest, periods) - 1)
        )
    )
    print("Your credit principle = {}!".format(principle))
