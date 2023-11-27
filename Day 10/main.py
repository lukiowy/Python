from art import logo
def add(n1, n2):
    sum = n1 + n2
    return sum


def sub(n1, n2):
    subt = n1 - n2
    return subt


def mult(n1, n2):
    multip = n1 * n2
    return multip


def division(n1, n2):
    div = n1 / n2
    return div


dict = {"+": add, "-": sub, "*": mult, "/": division}

def calc():
  print(logo)
  num1 = float(input("What is the first number? "))
  running = True
  
  while running:
    print("What operation do you choose?")
    for i in dict:
        print(i)
    operation = input("Choose one from above: ")
    num2 = float(input("What is the second number? "))
    asd = dict[operation]
    result = asd(num1, num2)
    print(f"{num1} {operation} {num2} = {result}")
    still_run = input(f"Type 'y' for next calculation with {result}, 'a' to start again or 'n' to stop: ")
    if still_run == "a":
          running = False
          calc()
    elif still_run == "y":
          num1 = result
    elif still_run == "n":
      running =False
          
calc()