import time
import sys
from colorama import init, Fore, Style

# Initialize colorama for colored text
init()

# ASCII art for cutehack v2 in yellow
ascii_art = f"""
{Fore.RED}░█▀▀█ ░█▀▀█ ▀▀█▀▀ ░█▀▀█ ░█▀▀▄ ░█▀▀█ ▀▀█▀▀ ░█▀▀█ ░█▀▄▀█ 
░█░░░ ░█░░░ ░░█░░ ░█▀▀▄ ░█░░░ ░█░░░ ░░█░░ ░█▀▀▄ ░█░█░█ 
░█▄▄█ ░█▄▄█ ░░▀░░ ░█▄▄█ ░█▄▄▀ ░█▄▄█ ░░▀░░ ░█▄▄█ ░█░░▀█{Style.RESET_ALL}
"""

# List of tool names in green
tool_names = [
    f"{Fore.GREEN}Tool 1{Style.RESET_ALL}",
    f"{Fore.GREEN}Tool 2{Style.RESET_ALL}",
    f"{Fore.GREEN}Tool 3{Style.RESET_ALL}",
    f"{Fore.GREEN}Tool 4{Style.RESET_ALL}",
    f"{Fore.GREEN}Tool 5{Style.RESET_ALL}",
    f"{Fore.GREEN}Tool 6{Style.RESET_ALL}",
    f"{Fore.GREEN}Tool 7{Style.RESET_ALL}",
    f"{Fore.GREEN}Tool 8{Style.RESET_ALL}",
    f"{Fore.GREEN}Tool 9{Style.RESET_ALL}",
    f"{Fore.GREEN}Tool 10{Style.RESET_ALL}"
]

# Function to display ASCII art with loading animation
def display_ascii_art():
    for char in ascii_art:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.005)

# Function to display tool options
def display_tool_options():
    print("\nChoose a tool to run:")
    for idx, tool_name in enumerate(tool_names, start=1):
        print(f"[ {Fore.RED}{idx}{Style.RESET_ALL} ] {tool_name}")

# Function to run the selected tool
def run_tool(tool_index):
    if 1 <= tool_index <= len(tool_names):
        selected_tool = tool_names[tool_index - 1]
        print(f"\nRunning {selected_tool}...")
        # Add your code to run the selected tool here
    else:
        print("\nInvalid option. Please choose a valid tool.")

# Main program
if __name__ == "__main__":
    # Display ASCII art with loading animation
    print(Fore.GREEN)
    display_ascii_art()
    print(Style.RESET_ALL)

    # Display tool options
    display_tool_options()

    # User input prompt in green and blue
    while True:
        try:
            user_input = int(input(f"{Fore.RED}\n┌──(ChTools{Fore.BLUE}㉿{Fore.RED}CutehackYt)-[~]\n└─> {Fore.GREEN}"))
            run_tool(user_input)
            break
        except ValueError:
            print(Fore.RED + "Error: Please enter a valid number.")
