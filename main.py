def square_root(x: float, guess: float = 0, iterations: int = 10):
    if guess == 0:
        guess = x / 2
    for i in range(iterations): # Heron's method
        guess = (guess + x / guess) / 2
    return guess

def factorial(x: float):
    if x == 1 or x == 2:
        return x
    return x * factorial(x - 1)

def power(x: float, y: int):
    if y == 0:
        return 1
    return x * power(x, y - 1)

def pi(iterations: int = 100):
    sum = 0
    for i in range(1, iterations):
        sum += 1 / (i * i)
    return square_root(6 * sum, 0, int(iterations / 10))

if __name__ == "__main__":
    print("Welcome to the Irrational Number Calculator!")
    print("This calculator will calculate irrational numbers like pi and sqrt(2)!")
    print("It will do so with iterative algorithms, and will show you how precision changes with each iteration.")
    print("This is the list of numbers we can calculate (enter q to quit):")
    print("")
    print("1) Square Root of 2")
    print("2) Pi")

    response = input("")
    match response:
        case "q":
            exit()
        case "1":
            i = 1
            print("We're gonna claculate the square root of 2 using Heron's method (initial guess of 0)")
            while True:
                print(f"{i} iterations: {square_root(2, 0, i)}")
                i *= 10
        case "2":
            i = 10
            print("We're gonna claculate pi using the sum of the reciprocals of the squares of the first n natural numbers")
            while True:
                print(f"{i} iterations: {pi(i)}")
                i *= 10