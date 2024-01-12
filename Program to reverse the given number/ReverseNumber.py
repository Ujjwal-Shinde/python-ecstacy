# Function to count digits in a given integer
def main():
    # Get user input
    user_input = int(input("Enter an integer: "))

    # Call the function and print the result
    result = reverse_number(user_input)
    print(f"Reverse Number: {result}")

# Function to reverse a given integer
def reverse_number(number):
    reversed_number = 0
    while (number != 0):
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    return reversed_number
   
# Call the main function
if __name__ == "__main__":
    main()