def generate_email(first_name, last_name):
    first_name = first_name.strip().lower()
    last_name = last_name.strip().lower()
    email = f"{first_name[0]}{last_name[:5]}@sru.edu.in"
    return email

def main():
    n = int(input("Enter number of students: "))
    emails = []
    for _ in range(n):
        first_name = input("Enter first name: ").strip()
        last_name = input("Enter last name: ").strip()
        if first_name and last_name:
            email = generate_email(first_name, last_name)
            emails.append(email)
        else:
            emails.append("Invalid name format")
    print("\nGenerated Email IDs:")
    for email in emails:
        print(email)

if __name__ == "__main__":
    main()
