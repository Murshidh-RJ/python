MAX_LINES = 3
MAX_BAT = 100
MIN_BAT = 1

def deposite():
  while True:
    amount = input("what would you like to deposite? $")
    if amount.isdigit():
      amount=int(amount)
      if amount>0:
        break
      else:
        print("Amount must be greater than 0.")
    else:
      print("please enter a number.")

  return amount

def get_number_of_lines():
  while True:
    Lines = input("Enter the number of lines to be bet on (1-" + str(MAX_LINES) + ")? ")
    if Lines.isdigit():
      Lines=int(Lines)
      if 1 <= Lines <= MAX_LINES:
        break
      else:
        print("Enter a Valid Number of Lines.")
    else:
      print("please enter a number.")

  return Lines


def get_bat():
  while True:
    amount = input("how much do you want to bat on each line? $")
    if amount.isdigit():
      amount=int(amount)
      if MIN_BAT <= amount <= MAX_BAT:
        break
      else:
        print(f"Enter an amount between ${MIN_BAT} - ${MAX_BAT}.")
    else:
      print("please enter a number.")

  return amount


def main():
  balance = deposite()
  Lines = get_number_of_lines()


  main()
