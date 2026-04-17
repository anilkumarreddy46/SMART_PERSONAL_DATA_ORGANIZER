from models.person import Person
from utils.validators import *
from utils.file_ops import *
from utils.cleaners import *
from analysis.analyzer import analyze
from analysis.visualizer import visualize


def add_record(records):
    name = input("Enter name: ")

    age = input("Enter age: ")
    if not validate_age(age):
        print("Invalid age ❌")
        return

    phone = input("Enter phone: ")
    if not validate_phone(phone):
        print("Invalid phone ❌")
        return

    email = input("Enter email: ")
    if not validate_email(email):
        print("Invalid email ❌")
        return

    gender = input("Enter gender: ")
    city = input("Enter city: ")
    interests = input("Enter interests (comma separated): ").split(",")

    person = Person(name, int(age), phone, email, gender, city, interests)
    records.append(person)

    save_data(records)
    print("Record added ✅")


def display_all(records):
    for r in records:
        r.display()


def search(records):
    key = input("Search: ").lower()

    for r in records:
        if key in r.name.lower() or key in r.city.lower():
            r.display()


def delete_record(records):
    rid = int(input("Enter ID: "))
    for r in records:
        if r.id == rid:
            records.remove(r)
            save_data(records)
            print("Deleted ✅")
            return


def menu():
    records = load_data()

    while True:
        print("""
1. Add Record
2. Display All
3. Search
4. Delete
5. Export CSV
6. Analyze
7. Visualize
8. Exit
""")

        ch = input("Enter choice: ")

        if ch == "1":
            add_record(records)

        elif ch == "2":
            display_all(records)

        elif ch == "3":
            search(records)

        elif ch == "4":
            delete_record(records)

        elif ch == "5":
            export_csv(records)

        elif ch == "6":
            analyze(records)

        elif ch == "7":
            visualize(records)

        elif ch == "8":
            break

        else:
            print("Invalid choice ❌")


if __name__ == "__main__":
    menu()
