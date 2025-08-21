from num import num


def sum_of_n(num):
    print(f"Sum of 1 to {num} is :")
    total = 0
    for i in range(1, num + 1):  # changed num to num+1 to include the last number
        total = total + i
    return total 

print(f"Sum of first n is : {sum_of_n(num)}")
