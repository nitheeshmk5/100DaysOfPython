students = {
    'Nitheesh':80,
    'Dharshan':90,
    'Praveen':95,
    'Elango':55,
    'Hari':20
}
students_new = {}

for i in students:
    marks = students[i]
    if marks >= 90:
        students_new[i] = "Outstanding"
    elif marks >= 70:
        students_new[i] = "Mass"
    elif marks >= 60 :
        students_new[i] = "Pass"
    else:
        students_new[i] = "Fass"

print(students_new)