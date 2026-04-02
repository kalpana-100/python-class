#CLI system. - Ask system information:
# - name - email - class
# at first create .txt file and then store information in a file.
# Display students in CLI.
#should be able to search student with email.

# Step 1: Data
data = [
    ['Sudeshna', 'sudeshna1@gmail.com', '6'],
    ['Nabina', 'Nabina2@gmail.com', '8'],
    ['Isneha', 'Isneha3@gmail.com', '10']
]

# Step 2: Save to file
file = open("students.txt", "w")

for student in data:
    file.write(student[0] + "," + student[1] + "," + student[2] + "\n")

file.close()


# Step 3: Show students
def show_students():
    file = open("students.txt", "r")

    print("\nStudents:")
    for line in file:
        print(line.strip())

    file.close()


# Step 4: Search by email
def search_student():
    email_input = input("Enter email: ")

    file = open("students.txt", "r")
    found = False

    for line in file:
        name, email, cls = line.strip().split(",")

        if email == email_input:
            print("Found:", name, email, cls)
            found = True

    if found == False:
        print("Not found")

    file.close()


# Step 5: Menu
while True:
    print("\n1. Show Students")
    print("2. Search by Email")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_students()

    elif choice == "2":
        search_student()

    elif choice == "3":
        break

    else:
        print("Wrong choice")

        