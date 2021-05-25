def divide(dividend, divisor):
    if(divisor == 0):
        raise ZeroDivisionError("Divisor can't be zero.")
    return dividend/divisor

def average_grade(st_grades):
    return divide(sum(st_grades) , len(st_grades))

students = [{"name" : "Bob", "grades": [78,90,65]},
            {"name" : "Rolf", "grades": []},
            {"name" : "Tom", "grades": [89,75,98]}
            ]
try:
    for student in students:
        average = average_grade(student["grades"])
        print(f"{student['name']} has {average} grades as average: ")
except ZeroDivisionError as e:
    print(e)
    print(f"{student['name']} does not have any grade yet")
else:
    print("The average of all the students have been calculated.")
finally:
    print("Thank you for using our application");