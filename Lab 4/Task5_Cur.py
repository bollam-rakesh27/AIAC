file_path = r"C:\Users\Rakesh\OneDrive\Attachments\AIAC\Lab 4\text.txt"

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        print("Number of lines in the file:", len(lines))
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
