def max_of_three(a, b, c):
    return max(a, b, c)

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))
    maximum = max_of_three(num1, num2, num3)
    print(f"The maximum of the three numbers is: {maximum}")

if __name__ == "__main__":
    main()
