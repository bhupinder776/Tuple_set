def main():
    # Initialize an empty set to store unique names
    names = set()

    while True:
        # Ask the user to enter a name
        name = input("Enter a name (or press Enter to stop): ")

        # Check if the input is an empty string to break the loop
        if name == "":
            break

        # Check if the name is new or existing
        if name in names:
            print("Existing name")
        else:
            print("New name")
            names.add(name)

    # Print out all the names, one per line
    print("\nList of names:")
    for name in names:
        print(name)


# Run the main program
main()
