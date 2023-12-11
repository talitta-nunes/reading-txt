def convert_string_to_number(input_string):
    try:
        numeric_value = int(input_string)

        formatted_value = float(numeric_value) / 1000

        return formatted_value
    except ValueError:
        print("Error: Input is not a valid integer.")
        return None