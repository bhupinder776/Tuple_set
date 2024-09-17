def main():
    # Define the seasons in a tuple, each repeated for three months
    seasons = ("winter", "winter", "spring", "spring", "spring",
               "summer", "summer", "summer", "autumn", "autumn",
               "autumn", "winter")

    # Ask the user for the number of a month
    month = int(input("Enter the number of a month (1-12): "))

    # Check if the input month is valid
    if 1 <= month <= 12:
        # Get the corresponding season from the tuple
        season = seasons[month - 1]
        print(f"The month {month} is in {season}.")
    else:
        print("Invalid month number. Please enter a number between 1 and 12.")

# Run the main program
main()
