def add():
    addnum1 = int(input("Enter your first number:"))
    addnum2 = int(input("Enter your second number:"))
    sum = addnum1 + addnum2
    print(sum)
def subract():
    subtractnum1 = int(input("Enter your first number:"))
    subtractsum2 = int(input("Enter your second number:"))
    difference = subtractnum1 - subtractsum2
    print(difference)
def multiply():
    multiplynum1 = int(input("Enter your first number:"))
    multiplynum2 = int(input("Enter your second number:"))
    product = multiplynum1 * multiplynum2
    print(product)
def divide():
    dividenum1 = int(input("Enter your first number:"))
    dividenum2 = int(input("Enter your second number:"))
    quotient = dividenum1 / dividenum2
    print(quotient)
def main():
 print("Welcome to Calculator!")
 print("0.) Quit")
 print("1.) ADD")
 print("2.) SUBTRACT")
 print("3.)  MULTIPLY")
 print("4.) DIVIDE")
 print(input("Choose one of the Following options:"))

 if int(input("Choose one of the Following options:")) == 0:
     print("Goodbye!")
 elif int(input("Choose one of the Following options:")) ==1:
     add()
 elif int(input("Choose one of the Following options:")) == 2:
     subract()
 elif int(input("Choose one of the Following options:")) == 3:
     multiply()
 elif int(input("Choose one of the Following options:")) == 4:
     divide()
 else:
     print("Invalid input")



if __name__ == "__main__":
    main()
