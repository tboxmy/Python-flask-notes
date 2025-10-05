# `01` Setup

## Requirements

1. Python 3+

Expecting Python version 3.13 or higher.

2. IDE

Examples are using Visual Code. Please feel free to use any IDE of your preference.

In Visual Code, open a terminal and verify the python in use.

```
$ python --version
```

3. Create a working environment

```
python -m venv /path/to/virtual/environment
```

## Running a Python project in Visual Code

1. Open Visual Code.

Ensure this is a new project. Otherwise follow these steps to create a folder and the environment.

- Click File ->New Window
- Choose Open Folder, 
- Create a folder in location of your choice, click Select Folder. I will call mine python-flask
- Click View ->Command Palette and select Python: Create Environment ->Venv -> Python 3.13.x 

2. Check the virtual environment

Click View ->Terminal

Select Default Profile as Command Prompt

3. Create and test a Python script

Create a new file called hello_world.py

```
def print_hello_world(name):
    print("Hello", name, "!")

# Calling the function
print_hello_world("Tboxmy")
```

Click the Run button in Visual Code and view results in the terminal window.

