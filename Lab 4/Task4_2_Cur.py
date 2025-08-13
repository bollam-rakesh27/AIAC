def count_vowels(s):
    count = 0
    for ch in s:
        if ch.lower() in 'aeiou':
            count += 1
    return count

# Get input from the user
user_input = input("Enter a string: ")

# Call the function and store the result
vowel_count = count_vowels(user_input)

# Display the result
print(f"No.of.vowels={vowel_count}")



