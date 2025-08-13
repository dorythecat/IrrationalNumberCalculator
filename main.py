def square_root(x: float, guess: float = 0, iterations: int = 10):
    if guess == 0:
        guess = x / 2
    for i in range(iterations): # Heron's method
        guess = (guess + x / guess) / 2
    return guess