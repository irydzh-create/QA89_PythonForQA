import csv
import json

def read_students():
    with open("students.csv","r",encoding="utf-8",newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Student:{row['name']} ({row['age']})")
read_students()



def save_profile(name: str, age: int, city: str) -> None:
    profile = {
        "name": name,
        "age": age,
        "city": city
    }
    with open("profile.json", "w", encoding="utf-8") as file:
        json.dump(profile, file, ensure_ascii=False, indent=4)

save_profile("Maria","30","Haifa")
print()
