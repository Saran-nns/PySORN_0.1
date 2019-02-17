import sys
import os

# Get the current working directory and add it to sys path

cwd = os.getcwd()
print(cwd)
sys.path.insert(0, cwd)

