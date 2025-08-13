def cm_to_inches(cm):
    """Convert centimeters to inches."""
    return cm * 0.39

def main():
    try:
        cm = float(input("Enter length in centimeters: "))
        inches = cm_to_inches(cm)
        print(f"{cm} cm = {inches:.2f} inches")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
