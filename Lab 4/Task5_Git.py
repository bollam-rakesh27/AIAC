file_path = r"C:\Users\Rakesh\OneDrive\Attachments\AIAC\Lab 4\text.txt"

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        print(f"Number of lines in the file: {len(lines)}")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {e}")