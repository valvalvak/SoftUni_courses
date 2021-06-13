import os

_, _, files_list = next(os.walk(input()))

current_directory_files = {}

for elements in files_list:
    name, extension = os.path.splitext(elements)
    if extension not in current_directory_files:
        current_directory_files[extension] = []
    current_directory_files[extension].append(name)

path_to_desktop = os.path.join(os.environ["USERPROFILE"], "Desktop", "report.txt")

with open(path_to_desktop, "w+") as report_file:
    for extension, files in sorted(current_directory_files.items()):
        report_file.writelines(extension + '\n')
        for file in files:
            report_file.writelines(f"- - - {file}{extension}" + '\n')

# with open("report.txt", 'r') as file:
#     for line in file:
#         print(line, end="")

# import shutil, os
# shutil.copy("report.txt", path_to_desktop)
