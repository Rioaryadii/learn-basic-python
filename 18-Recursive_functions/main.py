# Rio Fandia Aryadi
# 241011400059
# 02TPLE001

# 18 - Recursive Functions

def factorial(n):
    """Function to calculate the factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def fibonacci(n):
    """Function to calculate the nth Fibonacci number using recursion."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def main():
    # Factorial calculation
    num = 5
    fact_result = factorial(num)
    print(f"The factorial of {num} is: {fact_result}")

    # Fibonacci calculation
    fib_index = 10
    fib_result = fibonacci(fib_index)
    print(f"The {fib_index}th Fibonacci number is: {fib_result}")

if __name__ == "__main__":
    main()