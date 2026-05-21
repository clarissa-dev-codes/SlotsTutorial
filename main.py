import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

#transposing a matrix
def print_slot_machine_spin(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()



#collects the money from the user
def deposit():
    while True:
        amount = input("Enter amount to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Invalid amount. Please enter a positive integer greater than zero.")
        else:
            print("Invalid amount. Please enter a positive integer.")

    return amount

#how many lines
def get_number_of_lines():
    while True:
        number_of_lines = input("Enter number of lines to bet on (1-" + str(MAX_LINES) + "): ")
        if number_of_lines.isdigit():
            number_of_lines = int(number_of_lines)
            if 1 <= number_of_lines <= MAX_LINES:
                break
            else:
                print("Invalid number of lines. Please enter a positive integer.")
        else:
            print("Please enter a number between 1 and " + str(MAX_LINES) + ".")

    return number_of_lines

#amount bet on each line
def get_bet():
    while True:
        bet = input("Enter bet to bet on (1-" + str(MAX_BET) + "): $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number between 1 and " + str(MAX_BET) + ".: $")

    return bet

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Amount exceeds your balance. Your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${balance} on {lines}. Total bet is ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine_spin(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    #the * is called the splat operations
    #it does all the values that is sent to that variable
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current Balance is ${balance}")
        answer = input("Press enter to spin (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")
main()