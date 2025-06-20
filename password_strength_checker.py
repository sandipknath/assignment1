def check_password_strength(password):
    # Check if password meets the criteria
    if len(password) < 8:
        return False

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/~`"
    has_special = any(char in special_characters for char in password)

    # Return True only if all conditions are met
    return has_upper and has_lower and has_digit and has_special

# --- Main Program ---

# Take password input from the user
user_password = input("Enter a password to check its strength: ")

# Call the function and validate
is_strong = check_password_strength(user_password)

# Provide feedback
if is_strong:
    print("Strong password! Your password meets all the criteria.")
else:
    print("Weak password! Please make sure your password:")
    print("- Has at least 8 characters")
    print("- Includes both UPPERCASE and lowercase letters")
    print("- Contains at least one number (0-9)")
    print("- Includes at least one special character (e.g., !@#$%^&*)")
