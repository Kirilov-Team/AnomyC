import colorama
import time
import os
import sys

# Initialize colorama
colorama.init()

# ASCII art for AnomyC
anomyc_ascii = """
   ▄▄▄       ███▄    █  ▒█████   ███▄ ▄███▓▓██   ██▓ ▄████▄  
  ▒████▄     ██ ▀█   █ ▒██▒  ██▒▓██▒▀█▀ ██▒ ▒██  ██▒▒██▀ ▀█  
  ▒██  ▀█▄  ▓██  ▀█ ██▒▒██░  ██▒▓██    ▓██░  ▒██ ██░▒▓█    ▄ 
  ░██▄▄▄▄██ ▓██▒  ▐▌██▒▒██   ██░▒██    ▒██   ░ ▐██▓░▒▓▓▄ ▄██▒
   ▓█   ▓██▒▒██░   ▓██░░ ████▓▒░▒██▒   ░██▒  ░ ██▒▓░▒ ▓███▀ ░
   ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ▒░   ░  ░   ██▒▒▒ ░ ░▒ ▒  ░
    ▒   ▒▒ ░░ ░░   ░ ▒░  ░ ▒ ▒░ ░  ░      ░ ▓██ ░▒░   ░  ▒   
    ░   ▒      ░   ░ ░ ░ ░ ░ ▒  ░      ░    ▒ ▒ ░░  ░        
        ░  ░         ░     ░ ░         ░    ░ ░     ░ ░      
                                            ░ ░     ░        
"""

# Add a new line for the additional row
additional_row = "=" * 100

clear = lambda: os.system('cls')
clear()
os.system('title AnomyC')

def gradient_color(start_color, end_color, ratio):
    return tuple(int(start + (end - start) * ratio) for start, end in zip(start_color, end_color))

def slide_in_with_gradient(text, start_color, end_color, additional_row=None):
    lines = text.split('\n')
    if additional_row:
        lines.append(additional_row)
    max_width = max(len(line) for line in lines)
    steps = max_width

    # Get terminal size
    terminal_width, terminal_height = os.get_terminal_size()

    # Calculate left padding to center the text
    left_padding = (terminal_width - max_width) // 2

    # Calculate top padding
    top_padding = 0

    for i in range(steps):
        clear()
        # Print top padding
        print('\n' * top_padding, end='')
        for line in lines:
            colored_line = " " * left_padding  # Add left padding
            for j, char in enumerate(line.ljust(max_width)):
                if j < i:
                    if j < 3:
                        color = start_color
                    elif j >= max_width - 3:
                        color = end_color
                    else:
                        ratio = (j - 3) / (max_width - 6)
                        color = gradient_color(start_color, end_color, ratio)
                    colored_line += f"\033[38;2;{color[0]};{color[1]};{color[2]}m{char}"
                else:
                    colored_line += " "
            print(colored_line + colorama.Fore.RESET)
        time.sleep(0.01)

    # Print final text with gradient
    clear()
    print('\n' * top_padding, end='')
    for line in lines:
        colored_line = " " * left_padding  # Add left padding
        for j, char in enumerate(line):
            if j < 3:
                color = start_color
            elif j >= len(line) - 3:
                color = end_color
            else:
                ratio = (j - 3) / (len(line) - 6)
                color = gradient_color(start_color, end_color, ratio)
            colored_line += f"\033[38;2;{color[0]};{color[1]};{color[2]}m{char}"
        print(colored_line + colorama.Fore.RESET)

# Define colors
def slide_in_additional_row(additional_row, start_color, end_color):
    max_width = len(additional_row)
    steps = max_width

    # Get terminal size
    terminal_width, _ = os.get_terminal_size()

    # Calculate left padding to center the text
    left_padding = (terminal_width - max_width) // 2

    for i in range(steps):
        colored_line = " " * left_padding  # Add left padding
        for j, char in enumerate(additional_row):
            if j < i:
                if j < 3:
                    color = start_color
                elif j >= max_width - 3:
                    color = end_color
                else:
                    ratio = (j - 3) / (max_width - 6)
                    color = gradient_color(start_color, end_color, ratio)
                colored_line += f"\033[38;2;{color[0]};{color[1]};{color[2]}m{char}"
            else:
                colored_line += " "
        print(colored_line + colorama.Fore.RESET, end='\r')
        time.sleep(0.01)

    # Print final row with gradient
    colored_line = " " * left_padding  # Add left padding
    for j, char in enumerate(additional_row):
        if j < 3:
            color = start_color
        elif j >= len(additional_row) - 3:
            color = end_color
        else:
            ratio = (j - 3) / (len(additional_row) - 6)
            color = gradient_color(start_color, end_color, ratio)
        colored_line += f"\033[38;2;{color[0]};{color[1]};{color[2]}m{char}"
    print(colored_line + colorama.Fore.RESET)

# Add a new function for the username input
def get_username(start_color, end_color):
    terminal_width, _ = os.get_terminal_size()
    prompt = "Enter username: "
    left_padding = (terminal_width - len(prompt)) // 2

    colored_prompt = " " * left_padding
    for j, char in enumerate(prompt):
        ratio = j / (len(prompt) - 1)
        color = gradient_color(start_color, end_color, ratio)
        colored_prompt += f"\033[38;2;{color[0]};{color[1]};{color[2]}m{char}"
    
    username = input(colored_prompt + colorama.Fore.RESET)
    
    # Clear the line with the input prompt
    print(f"\033[A\033[2K", end='\r')
    
    return username

# Modify the get_key function
def get_key(start_color, end_color):
    prompt = "Enter key: "
    colored_prompt = ""
    for j, char in enumerate(prompt):
        ratio = j / (len(prompt) - 1)
        color = gradient_color(start_color, end_color, ratio)
        colored_prompt += f"\033[38;2;{color[0]};{color[1]};{color[2]}m{char}"
    
    key = input(colored_prompt + colorama.Fore.RESET)
    return key


# Define colors
start_color = (128, 0, 128)  # Purple
end_color = (0, 0, 255)  # Blue

# Perform slide-in animation with gradient for ASCII art
slide_in_with_gradient(anomyc_ascii, start_color, end_color)

# Move cursor to the next line
print()

# Perform slide-in animation with gradient for additional row
slide_in_additional_row(additional_row, start_color, end_color)

# Add a blank line for spacing
print()
time.sleep(1)
username = get_username(start_color, end_color)

# Display welcome message
welcome_message = "Welcome,"
terminal_width, _ = os.get_terminal_size()
left_padding = (terminal_width - len(welcome_message) - len(username) - 2) // 2  # -2 for the comma and space

colored_welcome = " " * left_padding
for j, char in enumerate(welcome_message):
    ratio = j / (len(welcome_message) - 1)
    color = gradient_color(start_color, end_color, ratio)
    colored_welcome += f"\033[38;2;{color[0]};{color[1]};{color[2]}m{char}"

print(f"{colored_welcome}{colorama.Fore.RESET} {username}!")

# Add a blank line for spacing
print()
time.sleep(1)

# Get key input
key = get_key(start_color, end_color)

# Print the entered key (for now)
print(f"\nEntered key: {key}")

input("\nPress Enter to continue...")

# Reset colorama
colorama.deinit()