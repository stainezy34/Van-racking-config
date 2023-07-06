import itertools

def parse_set_number(set_number):
    parts = set_number.split('-')
    if len(parts) != 5:
        raise ValueError("Invalid SET number format. Please provide in the format SET-height-width-depth-catch_type.")

    height = int(parts[1])
    width = int(parts[2])
    depth = int(parts[3])
    catch_type = parts[4]

    return height, width, depth, catch_type


def calculate_install_length(width, install_length):
    # Define the standard widths and their corresponding values
    width_options = {
        '429': 429,
        '474': 474,
        '500': 500,
        '529': 529,
        '600': 600,
        '629': 629,
        '900': 900
    }
    
    # Calculate the unit breakdown options
    unit_breakdown_options = {}
    for r in range(1, min(len(width_options), 2) + 1):
        for combo in itertools.combinations(width_options.values(), r):
            total_length = sum(combo)
            units = install_length // total_length
            remaining_length = install_length % total_length
            if remaining_length <= 100:
                unit_breakdown_options[combo] = units, remaining_length

    return unit_breakdown_options


def print_van_racking_set(set_number):
    height, width, depth, catch_type = parse_set_number(set_number)
    install_length = width

    print("Van Racking Set:")
    print("Height:", height, "mm")
    print("Width:", width, "mm")
    print("Depth:", depth, "mm")
    print("Catch Type:", catch_type)
    print("Installation Length:", install_length, "mm")

    unit_breakdown_options = calculate_install_length(width, install_length)

    print("Unit Breakdown Options:")
    for combo, (units, remaining_length) in unit_breakdown_options.items():
        combo_string = " x ".join(str(option) for option in combo)
        print(combo_string + ":", units, "units")
        print("Remaining Length:", remaining_length, "mm")


if __name__ == "__main__":
    set_number = input("Enter the SET number: ")
    print_van_racking_set(set_number)

