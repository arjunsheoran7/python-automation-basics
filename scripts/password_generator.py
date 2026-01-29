import random
import string

# Length of the password
PASSWORD_LENGTH = 12

# Characters to choose from
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = "".join(random.choice(characters) for _ in range(PASSWORD_LENGTH))

print("Generated password:", password)
