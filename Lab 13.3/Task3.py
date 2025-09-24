class Student:
    """Represents a student with a name, age, and marks.

    Attributes:
        name: Student's full name.
        age: Student's age in years.
        marks: List of numeric marks (e.g., for three subjects).
    """

    def __init__(self, name, age, m1, m2, m3):
        """Initialize a Student.

        Args:
            name: The student's name.
            age: The student's age.
            m1: Mark for subject 1.
            m2: Mark for subject 2.
            m3: Mark for subject 3.
        """
        self.name = name
        self.age = age
        self.marks = [m1, m2, m3]

    def details(self):
        """Print student details in a readable format."""
        print(f"Name: {self.name} | Age: {self.age}")

    def total(self):
        """Return the total of all marks."""
        return sum(self.marks)


if __name__ == "__main__":
    name = input("Enter student name: ").strip()
    try:
        age = int(input("Enter age: ").strip())
        m1 = float(input("Enter marks 1: ").strip())
        m2 = float(input("Enter marks 2: ").strip())
        m3 = float(input("Enter marks 3: ").strip())
    except ValueError:
        print("Invalid input. Age must be an integer and marks must be numbers.")
        raise SystemExit(1)

    s = Student(name, age, m1, m2, m3)
    s.details()
    print(f"Total marks: {s.total()}")