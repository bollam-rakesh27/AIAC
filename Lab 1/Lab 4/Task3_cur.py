def format_full_name():
    full_name = input("Enter full name (First Last): ").strip()
    parts = full_name.split()
    if len(parts) < 2:
        print("Please enter both first and last names.")
        return
    first_name = parts[0]
    last_name = parts[-1]
    print(f"First name : {first_name}")
    print(f"Last name : {last_name}")
    print(f"Formatted: {last_name}, {first_name}")

if __name__ == "__main__":
    format_full_name()
