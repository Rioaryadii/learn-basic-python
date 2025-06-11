# Rio Fandia Aryadi
# 241011400059
# 02TPLE001

# 20 - Scope and Global Variable

x = 5 # Global variable

def local_scope():
    y = 10  # Local variable
    print("Local y:", y)

def global_scope():
    global x  # Declare x as global
    x = 20  # Modify the global variable
    print("Global x:", x)

def modify_global():
    global x  # Declare x as global
    x += 5  # Modify the global variable
    print("Modified global x:", x)

def main():
    global_scope()  # Call function to modify global variable
    print("After global_scope, x:", x)  # Check modified global variable

    local_scope()  # Call function with local variable
    print("After local_scope, x:", x)  # Check global variable again

    modify_global()  # Call function to modify global variable again
    print("After modify_global, x:", x)  # Final check of global variable

if __name__ == "__main__":
    main()