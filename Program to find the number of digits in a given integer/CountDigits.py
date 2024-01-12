# Function to count digits in a given integer
def main():
    # Get user input
    user_input = int(input("Enter an integer: "))

    # Call the function and print the result
    result = count_digits(user_input)
    print(f"Number of digits: {result}")

def count_digits(number):
    # Take the absolute value for negative numbers
    if (number < 0):
        number = abs(number)
    # Handeling 0 as an Input
    if (number == 0):
        return 1
    else:
        digit_count = 0

        # Use a while loop to count digits
        while number != 0:
            number //= 10
            digit_count += 1

        return digit_count

# Call the main function
if __name__ == "__main__":
    main()