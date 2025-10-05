# `02` Common packages

General packages to work with 

## os

Check access to the current working directory

Create a new file called example_os.py

```
import os 
cwd = os.getcwd() 
print("Current working directory:", cwd) 
```

Click the Run button in Visual Code and view results in the terminal window.

## datetime

Handle date and time objects.

Create a new file called example_datetime.py

```
from datetime import datetime

now = datetime.now()
formatted_now = now.strftime("%A, %d %B, %Y at %X")
print("Hello, Flask! Its ", formatted_now)
```
