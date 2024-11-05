import random
import string

def generate_password(length, include_uppercase, include_numbers, include_special_chars):
    # Basic characters (lowercase letters)
    characters = string.ascii_lowercase

    # Add additional character sets based on user preferences
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    # Ensure there's at least one character in the final password from each chosen set
    password = []
    if include_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if include_numbers:
        password.append(random.choice(string.digits))
    if include_special_chars:
        password.append(random.choice(string.punctuation))

    # Fill the rest of the password length with random choices from the selected character set
    while len(password) < length:
        password.append(random.choice(characters))

    # Shuffle the list to ensure a random order
    random.shuffle(password)

    # Convert the list to a string
    return ''.join(password)

def valid_length(length, include_uppercase, include_numbers, include_special_chars):
    # Calculate the minimum required length based on the chosen options
    min_length = 1 + include_uppercase + include_numbers + include_special_chars
    return length >= max(min_length, 8)


def main():
    print("Welcome to the Python Password Generator!")
    
    # Get user preferences
    while True:
        length = int(input("Enter the desired password length (atleast 8 characters when all options are enabled): "))
        include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        include_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
        # Validate the length based on the chosen options
        if valid_length(length, include_uppercase, include_numbers, include_special_chars):
            break
        else:
            print("The length is too short for the selected options. Please choose a longer length.")

    # Generate the password
    password = generate_password(length, include_uppercase, include_numbers, include_special_chars)
    
    # Output the generated password
    print("\nGenerated Password:", password)


if __name__ == "__main__":
    main()
