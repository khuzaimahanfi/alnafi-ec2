# import os
# print(os.listdir('D:/PycharmProjects/ALANFI-TESTCASES/Alnafi-Main/COURSES_TEST_CASES'))
import os
import subprocess

# path of folder you want to run the scripts of
folder_path = 'D:/PycharmProjects/ALANFI-TESTCASES/Alnafi-Main/COURSES_TEST_CASES'

for filename in os.listdir(folder_path):
    if filename.endswith(".py"):
        file_path = os.path.join(folder_path, filename)
        subprocess.call(["python", file_path])
    else:
        continue

print("Test-Complete")
