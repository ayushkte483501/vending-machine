import json

def save_students(students):
    file = open("students.json", "w")
    json.dump(students, file)
    file.close()


def load_students():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []