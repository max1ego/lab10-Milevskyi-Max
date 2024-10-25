import os

program_files_path = "C:\\Program Files"

for item in os.listdir(program_files_path):
    print(item)

windows_path = "C:\\Windows"
file_list = []

for item in os.listdir(windows_path):
    file_path = os.path.join(windows_path, item)
    if os.path.isfile(file_path):
        file_list.append(file_path)


file = open("w.txt", "w", encoding="utf-8")
for file_path in file_list:
    file.write(file_path + "\n")
file.close()


