import random
import string

def generate_captcha(length=6):
    captcha_characters = string.ascii_letters + string.digits
    captcha = ''.join(random.choice(captcha_characters) for _ in range(length))
    return captcha

def validate_captcha(input_captcha, generated_captcha):
    return input_captcha == generated_captcha

# Generate a random captcha
generated_captcha = generate_captcha()
print("Generated Captcha:", generated_captcha)

# Ask the user to input the captcha
user_input = input("Enter the Captcha: ")

# Validate the user input
if validate_captcha(user_input, generated_captcha):
    print("Captcha matched! You are a human.")
else:
    print("Captcha mismatched! Please try again.")
