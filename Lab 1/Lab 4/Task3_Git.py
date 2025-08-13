def read_and_format_name():
    full_name = input("Enter full name: ").strip()
    parts = full_name.split()
    if len(parts) == 2:
        first_name, last_name = parts
        print(f"First name : {first_name} Last name : {last_name}")
    elif len(parts) == 1:
        print("Please enter both first and last names.")
    else:
        print("Invalid format. Please enter only first and last names separated by space.")

if __name__ == "__main__":
    read_and_format_name()