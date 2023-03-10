
def days_to_units(num_of_days, conversion_units):
    if conversion_units == "hours":
     return f"{num_of_days} days are {num_of_days * 24}  hours"
    elif conversion_units == "minitue":
        return f"{num_of_days} days are {num_of_days * 24 * 60}  minutes"
    else:
        return "unsupported units"


def validate_and_execute():
    try:
        user_input_number = int(days_and_units_dictionary["days"])

        # we want to do conversion only for positive integers
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_units_dictionary["units"])
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a valid positive number")
        else:
            print("you entered a negative number, no conversion for you!")
    except ValueError:
        print("your input is not a valid number. Don't ruin my program!")
user_input_message= input("Hey user, enter a number of days, and units \n ")