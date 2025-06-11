# RIo Fandia Aryadi
# 241011400059
# 02TPLE001

# 21 - Function Review and Parameter Types

def greet(name, age=20):
    """Function to greet a person with an optional age parameter."""
    return f"Hello, {name}! You are {age} years old."

def show_args(*args):
    print("Arguments:", args)
    for arg in args:
        print("Argument:", arg)

def show_kwargs(**kwargs):
    print("Keyword Arguments:", kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def main():
    # Greeting with default age
    greeting = greet("Rio")
    print(greeting)

    # Greeting with specified age
    greeting_with_age = greet("Budi", 22)
    print(greeting_with_age)

    # Show variable arguments
    show_args(1, 2, 3, "Hello", True)

    # Show keyword arguments
    show_kwargs(name="Cici", age=19, city="Jakarta")

if __name__ == "__main__":
    main()
    