# FIBONACCI GENERATOR
def fib():
    a, b = 0, 1 
    while True:  
        yield a  # This pauses the function and sends the current value of a
        a, b = b, a + b
# Create a generator object
num = fib()

# Infinite loop to continuously generate Fibonacci numbers
while True:
    print(next(num))  # Get the next number from the generator
    input()  # Wait for the user to press Enter before continuing
