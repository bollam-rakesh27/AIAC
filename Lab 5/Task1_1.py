# Script to collect user data: name, age, email

def collect_user_data():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    print("\nCollected Data:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Email: {email}")

if __name__ == "__main__":
    collect_user_data()