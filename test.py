import subprocess
from os import listdir, system
from os.path import isfile, join
import re
import sys

show_args = False
if len(sys.argv) == 1:
    show_args = input("Show args? ").lower() in ("y", "yes", "t", "true", "1")
else:
    show_args_2 = sys.argv[1] != "noargs"


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [atoi(c) for c in re.split(r'(\d+)', text)]


databases = [f for f in listdir("./databases/")
             if isfile(join("./databases/", f))]
sequences = [f for f in listdir("./sequences/")
             if isfile(join("./sequences/", f))]
sequences.sort(key=natural_keys)
expected_outcome = ["Bob", "No match", "No match", "Alice", "Lavender", "Luna", "Ron", "Ginny",
                    "Draco", "Albus", "Hermione", "Lily", "No match", "Severus", "Sirius", "No match", "Harry", "No match", "Fred", "No match"]
real_outcome = []

for i in range(4):
    proc = subprocess.Popen(['python', "dna.py",  f"databases/{databases[1]}", f"sequences/{sequences[i]}"],
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    communicate = str(proc.communicate()[0])
    real_outcome.append(communicate)
    print(
        f"Test {i+1}: {communicate}\n args: databases/{databases[1]}; sequences/{sequences[i]}" if show_args or show_args_2 else "")
for j in range(4, 20):
    proc = subprocess.Popen(['python', "dna.py",  f"databases/{databases[0]}", f"sequences/{sequences[j]}"],
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    communicate = str(proc.communicate()[0])
    real_outcome.append(communicate)
    print(
        f"Test {j+1}: {communicate}\n args: databases/{databases[0]}; sequences/{sequences[j]}" if show_args or show_args_2 else "")

if show_args or show_args_2:
    pass
else:
    system("cls")
for i in range(len(real_outcome)):
    if expected_outcome[i] in real_outcome[i]:
        result = "Passed"
    else:
        result = "Failed"
    print(f"\nTest {i+1}: {result}")
    print(
        f"Real Outcome: {real_outcome[i]}\nExpected Outcome: {expected_outcome[i]}" if result == "Failed" else f"{expected_outcome[i]}", end=" ")
