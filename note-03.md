# `03` Install and Test a Flask Application

Build a webservice to provide an API

   GET /

## Install Flask

In Visual Code, open the terminal and install Flask package

```
pip install flask 
OR
python -m pip install flask
```

## The Default application

A default Flask application invokes app.py. Lets create a **Route** that invokes the function **home()**. Refer to example file app-hello.py

Create the file app.py

```
from datetime import datetime

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    return "Hello, Flask! Its " + formatted_now
```

## Start a webservice

Ensure terminal is running in environment. 

1. In Visual Code's terminal, enter

```
python -m flask run
```

2. Open a web browser and enter the URL http://127.0.0.1:5000 

The URL may differ on systems.

To stop this web service, click Ctrl+c

2. To start the web srvice in another IP or port, provide the host and port information. Example, to use the localhost IP and port 8080.

```
python -m flask run --host=0.0.0.0 --port=8080
```

## Use Templates with Flask

Templates provide a regular HTML file with embedded Python logic and data. The function **render_template()** will access from the template directory. By default this is named **templates**. Refer example in the file app-templates.py

1. Create the directory templates
2. Create the file templates/index.html with the following contents.

```
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Application</title>
    </head>
    <body>
        <h1>Homepage</h1>
        Welcome
    </body>
    </html>
```

3. Create the file app.py

```
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():    
    return render_template('index.html')
```

4. Start the webservice

At the terminal, type

```
python -m flask run
```

5. View the page in a web browser

Open web browser with the URL http://127.0.0.1:8080/

## Pass values to a Template

Example of passing a value and a list to a template using the route

  GET /item

Refer to example file app-templates-data.py

1. Create the file app.py

```
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/item')
def get_item():
    items = ["Apple", "Banana", "Ciku"]
    item = 1
    quantity = 200
    unit_price = 1.5
    price = quantity * unit_price
    price = f"{price:.2f}" 
    return render_template('item.html',id=item,qty=quantity,unit_price=unit_price, price=price, items=items)

```

2. Create the file templates/item.html

```
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Application</title>
    </head>
    <body>
        <h1>Item Report</h1>
        <p><strong>{{ items[id] }}</strong></p>
        <p>Unit Price: RM{{ unit_price }}</p>
        <p>Quantity: {{ qty }}</p>
        <p>Sales : RM{{price}}</p>
    </body>
    </html>
```
