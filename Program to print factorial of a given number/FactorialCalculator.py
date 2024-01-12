def main():
    # Taking input from the user
    userInput = int(input("Enter a non-negative integer: "))

    # Checking if the number is non-negative
    if userInput < 0:
        print("Please enter a non-negative integer.")
    else:
        # Calculating and printing the factorial
        result = factorial(userInput)
        print(f"Factorial of {userInput} is: {result}")


# Function to calculate the factorial using a loop
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    main()
