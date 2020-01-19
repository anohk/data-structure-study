from general_linear_list.ordered_list import OrderedList
from general_linear_list.student import Student


# TODO ordered_list.py, student.py에서 pass로 처리된 메소드를 구현한다.
# TODO main.py에서는 TODO가 적혀있는 부분 외에는 수정하지 않는다.
# TODO main.py 실행시 output.txt와 같은 결과를 내도록 만든다.

def print_header(text):
    print("\n####################")
    print("# {}".format(text))


students = [
    Student(320001, "KyoungJoo", "jkj8790@gmail.com"),
    Student(320002, "SorrowBeaver", "sorrowbeaver@gmail.com"),
    Student(320003, "Beaver", "beaver@gmail.com"),
    Student(320004, "anohk", "anohk@gmail.com"),
    Student(320005, "anyoung", "anyoung@gmail.com")
]

ordered_list = OrderedList()

# Insert dummy data
print_header("Insert dummy data")
for student in students:
    result = ordered_list.insert(student)
    if not result:
        print("Insertion failed")

# Iterate elements
print_header("Iterate elements")
ordered_list.print_all()

# Print with email
print_header("Print with email")
# TODO email하고 같이 찍히도록 만들기
# ordered_list.print_all()

# Search elements
print_header("Search elements")
searchingKeys = [320001, 320003, 120001]
for key in searchingKeys:
    result = ordered_list.retrieve(key)
    if result:
        print("Student found (key: {})".format(key))
        print(result)
    else:
        print("Search failed (key: {})".format(key))

print_header("Remove elements")
erasingKeys = [320001, 320005, 320003, 320004, 320002]
for key in erasingKeys:
    removed_student = ordered_list.remove(key)
    if removed_student:
        print("Erase succeeded (key: {})".format(key))
    else:
        print("Erase failed (key: {})".format(key))

# List empty check
print_header("List empty check")
if ordered_list.is_empty():
    print("Empty")
else:
    print("Not empty")
