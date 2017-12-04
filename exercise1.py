def findNext(user_input):
    digits = [int(i) for i in str(user_input)]  # Convert input to int list

    for i in range(len(digits) - 1, 0, -1):
        if digits[i] > digits[i - 1]:  # Last 2 digits
            digits[i:] = sorted(digits[i:])  # Sort on index
            for y in range(i, len(digits)):
                if digits[y] > digits[i - 1]:
                    digits[i - 1], digits[y] = digits[y], digits[i - 1]
                    break
            break

    return ''.join(str(e) for e in digits)

    """
    digits.reverse()  # Reverse list

    for i in range(len(digits) - 1):
        # If the first value is greater than the second -> switch positions
        if digits[i] > digits[i + 1]:
            digits[i], digits[i + 1] = digits[i + 1], digits[i]
            break

    digits.reverse()  # Reverse back

    return ''.join(str(e) for e in digits)  # Return string
    """


def main():
    user_input = input("Enter a number : ")  # Read user input

    if user_input.isdigit(): # Validate
        print(findNext(user_input))
    else:
        print("Veuillez entrer un nombre entier positif.")


if __name__ == "__main__":
    main()
