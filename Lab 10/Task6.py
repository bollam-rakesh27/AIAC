def grade(score):
    return "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
print(grade(95))
print(grade(85))
print(grade(75))
print(grade(65))
print(grade(55))