students = []

def add_student():
    id = int(input("Enter id: "))
    name = (input("Enter name: "))
    age = int(input("Enter age: "))
    course = (input("Enter course: "))

    student = {
        "id": id,
        "name": name,
        "age":age,
        "course": course
    }

    students.append(student)
    print("Student added successfully\n")


def view_student():
    if len(students) == 0:
        print("No student found")
        return
    
    for s in students:
        print("ID", s["id"])
        print("Name", s["name"])
        print("Age", s["age"])
        print("Course", s["course"])
        print("__________________")
    print()


def search_student():
    choice = input("Search student by (1) id or (2) name: ")

    if choice == "1":
        id = int(input("Enter id: "))
        for s in students:
            if s["id"] == id:
                print("Student found")
                print(S)
                return
            else:
                print("Student not found")
    elif choice == "2":
        id = int(input("Enter name: "))
        for s in students:
            if s["name"] == name :
                print("Student found")
                print(S)
                return
            else:
                print("Student not found")
    else:
        print("invalid choice\n")

#Under Development