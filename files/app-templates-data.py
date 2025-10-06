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
    print("There are total of ", len(items), " items.")
    return render_template('item.html',id=item,qty=quantity,unit_price=unit_price, price=price, items=items)