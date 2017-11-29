def findNext(user_input):
    digits = [int(i) for i in user_input]  # Convert input to int list

    digits.reverse()  # Reverse list

    for i in range(len(digits) - 1):
        if digits[i] > digits[i + 1]: # If the first value is greater than the second -> switch positions
            digits[i], digits[i + 1] = digits[i + 1], digits[i]
            break

    digits.reverse() # Reverse back
    
    return ''.join(str(e) for e in digits) # Return string


user_input = input("Enter a number : ")  # Read user input

print(findNext(user_input))
