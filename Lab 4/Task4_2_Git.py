def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def main():
    user_input = input("Enter a string: ")
    count = count_vowels(user_input)
    print(f"No.of.vowels={count}")

main()