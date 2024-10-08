students_mark={'Hasan':78,
               'Rafiq':95,
               'Tinni':65,
               'Kashem':36,
               'Shuvro':54
}

print(students_mark),

student_grade=students_mark.copy()

for i in students_mark:
    if students_mark[i]<40:
        student_grade[i]='F'
    elif students_mark[i]<=50:
        student_grade[i]='D'
    elif students_mark[i]<=60:
        student_grade[i]='C'
    elif students_mark[i]<=70:
        student_grade[i]='B'
    elif students_mark[i]<=80:
        student_grade[i]='B+'
    elif students_mark[i]<=90:
        student_grade[i]='A'
    elif students_mark[i]<=100:
        student_grade[i]='A+'
print(student_grade)
