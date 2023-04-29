import os
import subprocess

folder_path = '/path/to/folder'
for filename in os.listdir('D:/PycharmProjects/ALANFI-TESTCASES/Alnafi-Main/COURSES_TEST_CASES'):
    if filename.endswith('.py'):
        subprocess.call(['python', os.path.join(folder_path, filename)])
    else:
        continue

