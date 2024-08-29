import random
import string

# Function to generate a password
def generate_password(length=12, include_uppercase=True, include_numbers=True, include_special_chars=True):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ''
    numbers = string.digits if include_numbers else ''
    special_chars = string.punctuation if include_special_chars else ''
    
    # Combine all possible characters
    all_chars = lowercase + uppercase + numbers + special_chars
    
    if not all_chars:
        print("Error: No character types selected. Unable to generate password.")
        return ""
    
    # Ensure the password has at least one of each selected character type
    password = []
    
    if include_uppercase:
        password.append(random.choice(uppercase))
    if include_numbers:
        password.append(random.choice(numbers))
    if include_special_chars:
        password.append(random.choice(special_chars))
    
    # Fill the rest of the password length
    password.extend(random.choice(all_chars) for _ in range(length - len(password)))
    
    # Shuffle to ensure randomness
    random.shuffle(password)
    
    # Convert list to string
    return ''.join(password)

# Function to get user preferences
def get_user_preferences():
    length = int(input("Enter the desired password length: "))
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    include_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'
    return length, include_uppercase, include_numbers, include_special_chars

# Main loop
def main():
    print("Welcome to the Password Generator!")
    
    while True:
        length, include_uppercase, include_numbers, include_special_chars = get_user_preferences()
        password = generate_password(length, include_uppercase, include_numbers, include_special_chars)
        
        if password:
            print(f"\nGenerated Password: {password}")
        
        play_again = input("\nDo you want to generate another password? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
    print("Thanks for using the Password Generator!")

if __name__ == "__main__":
    main()
