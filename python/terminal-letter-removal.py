def remove_letter(text, letter):
    return text.replace(letter, "")

# ANSI colors
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

print(CYAN + "Letter Remover Tool" + RESET)

text = input(YELLOW + "Enter a string: " + RESET)
letter = input(YELLOW + "Enter the letter to remove (case-sensitive): " + RESET)

result = remove_letter(text, letter)

print(GREEN + "\nResult: " + RESET + result)

input(RED + "\nPress Enter to close..." + RESET)