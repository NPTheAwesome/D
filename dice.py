#!/usr/bin/python3

import random 
import os
import sys

class Colours:
	ENDC = '\033[0m'

	BOLD = '\033[1m'
	UNDER = '\033[4m'
	NO_UNDER = '\033[24m'
	REVERSE = '\033[7m'
	FOREWARD = '\033[27m'

	FORE_DARK_BLACK = '\033[30m'
	FORE_DARK_RED = '\033[31m'
	FORE_DARK_GREEN = '\033[32m'
	FORE_DARK_ORANGE = '\033[33m'
	FORE_DARK_BLUE = '\033[34m'
	FORE_DARK_MAGENTA = '\033[35m'
	FORE_DARK_CYAN = '\033[36m'
	FORE_DARK_WHITE = '\033[37m'

	FORE_BRIGHT_BLACK = '\033[90m'
	FORE_BRIGHT_RED = '\033[91m'
	FORE_BRIGHT_GREEN = '\033[92m'
	FORE_BRIGHT_ORANGE = '\033[93m'
	FORE_BRIGHT_BLUE = '\033[94m'
	FORE_BRIGHT_MAGENTA = '\033[95m'
	FORE_BRIGHT_CYAN = '\033[96m'
	FORE_BRIGHT_WHITE = '\033[97m'

	BACK_DARK_BLACK = '\033[40m'
	BACK_DARK_RED = '\033[41m'
	BACK_DARK_GREEN = '\033[42m'
	BACK_DARK_ORANGE = '\033[43m'
	BACK_DARK_BLUE = '\033[44m'
	BACK_DARK_MAGENTA = '\033[45m'
	BACK_DARK_CYAN = '\033[46m'
	BACK_DARK_WHITE = '\033[47m'

	BACK_BRIGHT_BLACK = '\033[1000m'
	BACK_BRIGHT_RED = '\033[101m'
	BACK_BRIGHT_GREEN = '\033[102m'
	BACK_BRIGHT_ORANGE = '\033[103m'
	BACK_BRIGHT_BLUE = '\033[104m'
	BACK_BRIGHT_MAGENTA = '\033[105m'
	BACK_BRIGHT_CYAN = '\033[106m'
	BACK_BRIGHT_WHITE = '\033[107m'

rainbow_pattern = [Colours.FORE_BRIGHT_RED, 
                   Colours.FORE_DARK_ORANGE, 
                   Colours.FORE_BRIGHT_ORANGE, 
                   Colours.FORE_DARK_GREEN,
                   Colours.FORE_BRIGHT_BLUE, 
                   Colours.FORE_BRIGHT_MAGENTA]

# A function to retrieve an integer from a user, either greater than 0, or between 0 and a variable limit
def get_integer_from_user(prompt, limits = (None, None)):
    while True:
        response = input(prompt)
        try:
            integer = int(response)
            no_lower = not type(limits[0]) == type(0)
            no_upper = not type(limits[1]) == type(0)
            under    = False
            over     = False
            if not no_lower:
                under = integer < limits[0]
            if not no_upper:
                upper = integer > limits[1]
            if (no_lower or not under) and (no_upper or not over):
                return integer
            else:
                if limit < limits[0]:
                    print(f"\t{Colours.FORE_BRIGHT_ORANGE}Please input an integer {Colours.FORE_BRIGHT_RED}greater{Colours.FORE_BRIGHT_ORANGE} than {Colours.FORE_BRIGHT_RED}{limits[0]}{Colours.FORE_BRIGHT_ORANGE}.{Colours.ENDC}")
                else:
                    print(f"\t{Colours.FORE_BRIGHT_ORANGE}Please input an integer {Colours.FORE_BRIGHT_RED}less{Colours.FORE_BRIGHT_ORANGE} than {Colours.FORE_BRIGHT_RED}{limits[1]}{Colours.FORE_BRIGHT_ORANGE}.{Colours.ENDC}")
        except:
            print(f"\t{Colours.FORE_BRIGHT_ORANGE}Please input an {Colours.FORE_BRIGHT_RED}integer{Colours.FORE_BRIGHT_ORANGE}.{Colours.ENDC}")

# A function to retrieve an floaing point number from a user, either greater than 0, or between 0 and a variable limit
def get_float_from_user(prompt, limit = 0):
    while True:
        response = input(prompt)
        try:
            floating = float(response)
            if floating >= 0 and (floating <= limit or limit < 1):
                return floating
            else:
                if limit < 1:
                    print(f"\t{Colours.FORE_BRIGHT_ORANGE}Please input an floating point number {Colours.FORE_BRIGHT_RED}greater{Colours.FORE_BRIGHT_ORANGE} than {Colours.FORE_BRIGHT_RED}0{Colours.FORE_BRIGHT_ORANGE}.{Colours.ENDC}")
                else:
                    print(f"\t{Colours.FORE_BRIGHT_ORANGE}Please input an floating point number {Colours.FORE_BRIGHT_RED}between 0{Colours.FORE_BRIGHT_ORANGE} and {Colours.FORE_BRIGHT_RED}{str(limit)}{Colours.FORE_BRIGHT_ORANGE}.{Colours.ENDC}")
        except:
            print(f"\t{Colours.FORE_BRIGHT_ORANGE}Please input an {Colours.FORE_BRIGHT_RED}floating point number{Colours.FORE_BRIGHT_ORANGE}.{Colours.ENDC}")

# A function to retrieve a decision from a user, either true/false, or from a variable list of options
def get_choice_from_user(prompt, options = ['n', 'y']):
    valid = []
    for char in options:
        reference = char.lower()
        present = False
        for value in valid:
            if reference == value:
                present = True
                break

        if not present: 
            valid.append(reference)

    buffer = []
    for char in valid:
        buffer.append(char.upper())

    while True: 
        data = input(prompt)
        for char in data:
            for option in options:
                if char.lower() == option:
                    return option
                    
        print(f"\t{Colours.FORE_BRIGHT_ORANGE}Invalid input, please input one of the following options{Colours.ENDC}:", end = '\n\t\t')
        for char in buffer:
            if char == buffer[-1]:
                print(f"or {Colours.FORE_BRIGHT_RED}{char}{Colours.ENDC}.", end = '\n')
            else:
                print(f"{Colours.FORE_BRIGHT_RED}{char}{Colours.ENDC},", end = ' ')

# A simple function to retrieve a string value from a user, and double check that they have input the correct value.
def get_string_from_user(prompt, strict = True):
    while True:
        response = input(prompt)
        if strict:
            if response.isalpha():
                if get_choice_from_user(f"{Colours.FORE_BRIGHT_BLUE}Are you sure you want to use {Colours.FORE_BRIGHT_GREEN}{response}{Colours.FORE_BRIGHT_BLUE}? ({Colours.FORE_BRIGHT_GREEN}Y{Colours.FORE_BRIGHT_BLUE}, {Colours.FORE_BRIGHT_GREEN}N{Colours.FORE_BRIGHT_BLUE}) - {Colours.ENDC}") == 'y':
                    return response
                else:
                    print(f"\t{Colours.FORE_BRIGHT_GREEN}Alright.{Colours.ENDC}")
            else:
                print(f"\t{Colours.FORE_BRIGHT_ORANGE}Please input a string consisting of only {Colours.FORE_BRIGHT_RED}letters{Colours.FORE_BRIGHT_ORANGE}.{Colours.ENDC}")
        else:
            if get_choice_from_user(f"{Colours.FORE_BRIGHT_BLUE}Are you sure you want to use {Colours.FORE_BRIGHT_GREEN}\"{response}\"{Colours.FORE_BRIGHT_BLUE}? ({Colours.FORE_BRIGHT_GREEN}Y{Colours.FORE_BRIGHT_BLUE}, {Colours.FORE_BRIGHT_GREEN}N{Colours.FORE_BRIGHT_BLUE}) - {Colours.ENDC}") == 'y':
                return response
            else:
                print(f"\t{Colours.FORE_BRIGHT_GREEN}Alright.{Colours.ENDC}")

def roll_dice(sides = 6, dice = 1):
    vals = []
    total = 0
    count = 0
    while count < dice:
        vals.append(random.randint(1, sides))
        count += 1
    for roll in vals:
        total += roll
    return total

def batch_roll(iterations, sides = 6, dice = 1):
    rolls = []
    count = 0
    while count < iterations:
        rolls.append(roll_dice(sides, dice))
        count += 1
    return rolls

def batch_roll_orders(orders):
    batches = []
    for order in orders:
        batches.append(batch_roll(order.roll, order.size, order.dice))
    return batches

def find_counts(rolls):
    counts = []
    for roll in rolls:
        accounted = False
        for num in counts:
            if roll == num[0]:
                num[1] += 1
                accounted = True
                break
        if not accounted:
            counts.append([roll, 1])
    return counts

def order(counts):
    itera = []
    for count in counts:
        itera.append(count)
    ordered = []
    while len(ordered) < len(counts):
        lowest = [sys.maxsize, 0]
        for count in itera:
            if count[0] < lowest[0]:
                lowest = count
        ordered.append(lowest)
        itera.remove(lowest)
    return ordered

def pad(ordered, size, dice):
    padded = []
    maximum = size * dice
    next_value = dice
    offset = 0    
    while len(padded) < maximum - dice + 1:
        try:
            while ordered[offset][0] > next_value:
                padded.append([next_value, 0])
                next_value += 1
            padded.append(ordered[offset])
            offset += 1
            next_value += 1
        except IndexError:
            padded.append([next_value, 0])
            next_value += 1
        except Exception as e: 
            print(e)
            break
    return padded

def multi_plot(roll_sets, orders):
    global terminal_width, terminal_height
    front = len(" | ")
    graphs = []
    for rolls in roll_sets:
        graphs.append(find_counts(rolls))
    largest = 0
    longest = [0, 0]
    for counts in graphs:
        for count in counts:
            if count[1] > largest:
                largest = count[1]
            length = len(str(count[0]))
            if length > longest[0]:
                longest[0] = length
            length = len(str(count[1]))
            if length > longest[1]:
                longest[1] = length
    scale = (terminal_width - front - longest[0] - longest[1]) / largest
    ordered_graphs = []
    for counts in graphs:
        ordered_graphs.append(order(counts))
    padded_graphs = []
    index = 0
    for ordered in ordered_graphs:
        padded_graphs.append(pad(ordered, orders[index].size, orders[index].dice))
        index += 1

    for ordered in padded_graphs:

        half        = str(int(largest / 2)) + '↓'
        half_length  = len(half)

        first_space  = int((terminal_width - front - longest[0] - 2 - longest[1] - half_length) / 2)
        second_space = int((terminal_width - front - longest[0] - 2 - longest[1] - half_length) / 2)
        if first_space + second_space != int(terminal_width - front - longest[0] - 2 - longest[1] - half_length):
            second_space += 1

        output  = '\n'
        output += " " * (longest[0] + 2)
        output += "0↓"
        output += " " * first_space
        output += half
        output += " " * second_space
        output += '↓'
        output += str(largest)
        output += '\n'
        output += " " * (longest[0] + 2)
        output += "_" * (terminal_width - front - longest[0] + 1)
        print(output)
        counter = 0
        for count in ordered:
            output = ""
            length = len(str(count[0]))
            output += " " * (longest[0] - length)
            output += rainbow_pattern[counter % 6]
            output += str(count[0])
            output += Colours.ENDC
            output += " | "
            output += rainbow_pattern[counter % 6]
            output += "█" * int(count[1] * scale)
            output += rainbow_pattern[(counter + 3) % 6]
            output += str(count[1])
            output += Colours.ENDC
            print(output)
            counter += 1
    return padded_graphs

def plot_odds(result, order, offset):
    odds = []
    for value in result:
        odds.append([value[0] + offset, (value[1] / order.roll) * 100])
    
    targets = []
    next_value = 1
    while next_value < order.dice * order.size + offset + 2:
        if next_value < order.dice + offset:
            #targets.append([next_value, round(100 - odds[0][1], 2)])
            targets.append([next_value, 100])
        else:
            tally = 0
            index = 0
            while index < next_value - (order.dice + offset) and index < len(odds) - 1:
                tally += odds[index][1]
                index += 1
            targets.append([next_value, round(100 - tally, 2)])
        next_value += 1

    target_strings = []
    for target in targets:
        target_strings.append([f"{target[0]}", f"{target[1]}%"])
    global terminal_width, terminal_height
    front = len(" | ")
    largest = 100
    longest = [0, 0]
    for target in target_strings:
        length = len(target[0])
        if length > longest[0]:
            longest[0] = length
        length = len(target[1])
        if length > longest[1]:
            longest[1] = length
    scale = (terminal_width - front - longest[0] - longest[1]) / largest

    half         = '50%↓'
    half_length  = len(half)

    first_space  = int((terminal_width - front - longest[0] - 2 - longest[1] - half_length) / 2)
    second_space = int((terminal_width - front - longest[0] - 2 - longest[1] - half_length) / 2)
    if first_space + second_space != int(terminal_width - front - longest[0] - 2 - longest[1] - half_length):
        second_space += 1

    output  = '\n'
    output += " " * (longest[0] + 1)
    output += "0%↓"
    output += " " * first_space
    output += half
    output += " " * second_space
    output += f"↓{largest}%"
    output += '\n'
    output += " " * (longest[0] + 2)
    output += "_" * (terminal_width - front - longest[0] + 1)
    print(output)
    counter = 0
    for target in target_strings:
        output = ""
        length = len(str(target[0]))
        output += " " * (longest[0] - length)
        output += rainbow_pattern[counter % 6]
        output += str(target[0])
        output += Colours.ENDC
        output += " | "
        output += rainbow_pattern[counter % 6]
        output += "█" * int(targets[counter][1] * scale)
        output += rainbow_pattern[(counter + 3) % 6]
        output += str(target[1])
        output += Colours.ENDC
        print(output)
        counter += 1

def multi_plot_odds(results, orders, offsets):
    index = 0
    for result in results:
        plot_odds(result, orders[index], offsets[index])
        index += 1

class order_object():
    def __init__(self, size, dice, roll):
        self.size = size
        self.dice = dice
        self.roll = roll

terminal_width, terminal_height = os.get_terminal_size()

orders = []
offsets = []
graph_count = get_integer_from_user(f"{Colours.FORE_BRIGHT_BLUE}How many graphs shall we make? - {Colours.FORE_BRIGHT_GREEN}", (0, None))
index = 0
while index < graph_count:
    print(f"\n{Colours.FORE_BRIGHT_BLUE}Parameters for graph number {Colours.FORE_BRIGHT_GREEN}{index + 1}{Colours.ENDC}")
    orders.append(order_object(get_integer_from_user(f"\t{Colours.FORE_BRIGHT_BLUE}How many sides shall each die have? - {Colours.FORE_BRIGHT_GREEN}"), get_integer_from_user(f"\t{Colours.FORE_BRIGHT_BLUE}How many dice shall we throw each roll? - {Colours.FORE_BRIGHT_GREEN}"), get_integer_from_user(f"\t{Colours.FORE_BRIGHT_BLUE}How many roles shall we take? - {Colours.FORE_BRIGHT_GREEN}")))
    offsets.append(get_integer_from_user(f"\t{Colours.FORE_BRIGHT_BLUE}What skill modifier/offset should we use for the graph? - {Colours.FORE_BRIGHT_GREEN}"))
    index += 1

print(f"{Colours.ENDC}", end='')
results = multi_plot(batch_roll_orders(orders), orders)
multi_plot_odds(results, orders, offsets)