class student:
    def __init__(self, name="", roll_number=0, marks=0.0):
        self.name=name
        self.roll_number=roll_number
        self.marks=marks

    def input_details(self):
        self.name = input("Enter student name: ")
        self.roll_number = int(input("Enter roll number: "))
        self.marks = float(input("Enter marks: "))

    def display_grade(self):
        if self.marks >= 90:
            print("You got A grade")
        elif self.marks < 90 and self.marks >= 75:
            print("You got B grade")
        elif self.marks < 75 and self.marks >= 60:
            print("You got C grade")
        else:
            print("Better Luck Next time")

# Main function
def main():
    student1 = student()
    student1.input_details()
    student1.display_grade()

if __name__ == "__main__":
    main()
        

    
