def read_price_row(csv_path, person_number):
    """Return the two prices from the requested line, counting from 1."""
    # Open the file for reading. The with block closes it automatically.
    with open(csv_path) as price_file:
        # Store all lines in memory so they remain available after the file closes.
        lines = price_file.readlines()

    line_number = person_number - 1  # Python list indices start at 0.
    line = lines[line_number]  # Retrieve the requested line.
    # Remove surrounding whitespace, split at the comma, and name the two values.
    starter_price, main_course_price = line.strip().split(",")

    return starter_price, main_course_price  # Return the prices to the caller.


def read_all_prices(csv_path):
    """Return all prices as a list of tuples."""
    prices = []

    with open(csv_path) as price_file:
        for line in price_file:  # Repeat the following steps for each line.
            starter_price, main_course_price = line.strip().split(",")
            # Add this pair of prices to the list.
            prices.append((starter_price, main_course_price))

    return prices  # Return the complete list of price pairs.


def get_person_prices(all_prices, person_number):
    """Return the two prices for one person, counting from 1."""
    # Inputs: the stored list of all prices and the requested person's number.
    position_in_list = person_number - 1  # Python list indices start at 0.
    starter_price, main_course_price = all_prices[position_in_list]

    return starter_price, main_course_price
