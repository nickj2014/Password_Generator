import random
import string


def main():
    run = True
    print("""Welcome to my password generator!
Enter strong, medium or weak. 'Exit' to quit.""")

    while run:
        strength = input("Please enter strong, medium or weak: ")  # Get choice
        strength = strength.lower()  # Change choice to lowercase
        if strength in ["strong", "medium", "weak"]:  # Check if choice is an option
            password = generate(strength)  # Call generate function with strength option
            print(password)  # Print generated password
        elif strength == "exit":  # Check if choice is exit
            run = False
        else:
            print("Invalid input")


def generate(strength):
    weak = ["Banana", "Apple", "Orange", "Puppy", "Chocolate", "Tower"]  # Options for weak
    med = ["Banana", "Apple", "Orange", "502", "398", "Puppy", "87", "Chocolate", "Tower"]  # Options for medium
    characters = string.ascii_letters + string.digits + string.punctuation  # String containing A-Z, a-z, special chars
    strong = list(characters)  # Convert string to list for random choices of strong password

    if strength == "weak":
        password = "".join(random.sample(weak, 2))  # Join 2 random weak options

    elif strength == "medium":
        password = "".join(random.sample(med, 3))  # Join 3 random medium options

    elif strength == "strong":
        password = "".join(random.sample(strong, random.randrange(12, 16)))  # Join random amount of strong options

    return password


main()
