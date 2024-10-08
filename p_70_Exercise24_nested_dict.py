student_data=[
    {
        'Name': 'Masud',
        'roll_no':10,
        'age':20,
        'course':'Python'
    },
    {
        'Name':'Tinni',
        'roll_no':15,
        'age':21,
        'course':'Java'
    }
]
print(student_data)

def add_new_student(name, roll, age, course):
    new_student={}
    new_student['Name']=name
    new_student["roll_no"]=roll
    new_student['age']=age
    new_student['course']=course
    student_data.append(new_student)

add_new_student('Rakib',22, 18, 'C++')
add_new_student('Maruf',23, 19, 'Database')
print(student_data)