from pathlib import Path

data_folder=Path("test_data")
file_path = data_folder/"user.csv"
print(file_path)

print("************ example 5 (resolve parent directory) ************")
base_dir = Path(".").resolve().parent              # получает абсолютный путь к текущей папке и переходит на один уровень выше
folders = base_dir / "reports"                     # формирует путь к папке reports внутри родительской директории
print(folders)                                     # выводит полный путь к папке reports
print()

print("************ example 6 (create folder one level above) ************")
folder = Path("../lesson9")                        # создаёт путь к папке lesson9 на один уровень выше текущей
folder.mkdir(exist_ok=True)                        # создаёт папку, если её ещё нет
print()

print("************ example 7 (current directory) ************")
current_dir = Path(".").resolve()                  # получает абсолютный путь к текущей директории
print(current_dir)                                # выводит текущую директорию
print()

print("************ example 8 (current directory) ************")
def create_reports_folder():
    report_dir = Path("reports_1")
    report_dir.mkdir(exist_ok=True, parents=True)
    result_file=report_dir / "result.txt"
    with open(result_file, "w",encoding="utf-8") as file:
        file.write("Homework completed successfully")
    create_reports_folder()
    print()