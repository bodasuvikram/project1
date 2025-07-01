import os

File_name = "history.txt"

# Show history
def show_history():
    if not os.path.exists(File_name):
        print("No history found.")
        return
    with open(File_name, "r") as file:
        lines = file.readlines()
        if len(lines) == 0:
            print("No history found.")
        else:
            print("-----History-----")
            for line in lines:
                print(line.strip())

# Clear history
def clear_history():
    open(File_name, "w").close()
    print("History cleared.")

# Save calculation to history
def save_to_history(equation, result):
    with open(File_name, "a") as file:
        file.write(f"{equation} = {result}\n")

# Perform calculation
def calculation(user_input):
    split = user_input.split(" ")
    if len(split) != 3:
        print("Invalid input! Please use (15 + 8) format.")
        return

    try:
        first_num = float(split[0])
        operator = split[1]
        second_num = float(split[2])
    except ValueError:
        print("Invalid numbers entered.")
        return

    if operator == "+":
        result = first_num + second_num
    elif operator == "-":
        result = first_num - second_num
    elif operator == "*":
        result = first_num * second_num
    elif operator == "/":
        if second_num == 0:
            print("Can't divide by zero!")
            return
        result = first_num / second_num
    else:
        print("Invalid operator. Use only +, -, *, /.")
        return

    # Convert result to int if applicable
    if result == int(result):
        result = int(result)
    print(f"Result: {result}")
    save_to_history(user_input, result)

# Main menu loop
def main():
    print("===== SIMPLE CALCULATOR =====")
    while True:
        user_input = input("Enter calculation (e.g., 6 + 9), or command (history, clear, exit): ")
        command = user_input.strip().lower()

        if command == "exit":
            print("Goodbye!")
            break
        elif command == "history":
            show_history()
        elif command == "clear":
            clear_history()
        else:
            calculation(user_input)

main()
