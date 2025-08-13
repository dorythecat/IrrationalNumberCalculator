from decimal import *

getcontext().prec = 100 # Set the precision to 100 digits

def square_root(x: Decimal, guess: Decimal = 0, iterations: int = 10) -> Decimal:
    if guess == 0:
        guess = x / 2
    for _ in range(iterations): # Heron's method
        guess = (guess + x / guess) / 2
    return guess

def factorial(x: Decimal) -> Decimal:
    if x == 1 or x == 2:
        return x
    f = 2
    for i in range(3, x + 1):
        f *= i
    return f

def power(x: Decimal, y: int) -> Decimal:
    if y == 0:
        return 1
    p = x
    for _ in range(y - 1):
        p *= x
    return p

def pi(iterations: int = 100) -> Decimal:
    sum = 0
    for i in range(1, iterations):
        sum += Decimal(1 / (i * i))
    return square_root(6 * sum, 0, int(iterations / 10))

def euler(iterations: int = 100) -> Decimal:
    return power(1 + Decimal(1 / iterations), iterations)

def golden_ratio(iterations: int = 100) -> Decimal:
    return Decimal((1 + Decimal(square_root(5, 0, iterations))) / 2)

if __name__ == "__main__":
    print("Welcome to the Irrational Number Calculator!")
    print("This calculator will calculate irrational numbers like pi and sqrt(2), with 100 decimal digits!")
    print("It will do so with iterative algorithms, and will show you how precision changes with each iteration.")
    print("This is the list of numbers we can calculate (enter q to quit):")
    print("")
    print("1) Square Root of 2")
    print("2) Pi")
    print("3) Euler's Number")
    print("4) Golden Ratio")

    response = input("")
    match response:
        case "q":
            print("Aborting...")
            exit()
        case "1":
            i = 1
            print("We're gonna calculate the square root of 2 using Heron's method (initial guess of 0)")
            while True:
                print(f"{i} iterations: {square_root(Decimal(2), 0, i)}")
                i *= 10
        case "2":
            i = 10
            print("We're gonna calculate pi using the sum of the reciprocals of the squares of the first n natural numbers")
            while True:
                print(f"{i} iterations: {pi(i)}")
                i *= 10
        case "3":
            i = 10
            print("We're gonna calculate euler's number using the sum of the reciprocals of the first n natural numbers")
            while True:
                print(f"{i} iterations: {euler(i)}")
                i *= 10
        case "4":
            i = 10
            print("We're gonna calculate the golden ratio using the sum of the reciprocals of the first n natural numbers")
            while True:
                print(f"{i} iterations: {golden_ratio(i)}")
                i *= 10
        case _:
            print("Invalid input. Aborting.")
            exit()