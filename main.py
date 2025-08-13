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

def pi(iterations: int = 10):
    sum = 0
    for i in range(1, iterations):
        sum += 1 / (i * i)
    return square_root(6 * sum)