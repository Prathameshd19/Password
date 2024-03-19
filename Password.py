import string
import random

def generate_password(length):
    # Define the characters that will be used to generate the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Shuffle the characters
    shuffled = random.sample(characters, len(characters))

    # Generate the password
    password = ''.join(random.choice(shuffled) for i in range(length))

    return password

# Set the desired length of the password
password_length = 10

# Generate and print the password
print(f"Your new password is: {generate_password(password_length)}")
