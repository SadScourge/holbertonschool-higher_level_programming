from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

def read_json_data():
  with open("products.json", "r") as file:
    return json.load(file)

def read_csv_data():
  with open("products.csv", "r") as file:
    reader = csv.DictReader(file)
    return list(reader)

@app.route("/products")
def product_display():
  source = request.args.get("source")
  product_id = request.args.get("id", type=int)

  if not source:
    return render_template("product_display.html", error="Missing source parameter (json or csv)")

  if source not in ["json", "csv"]:
    return render_template("product_display.html", error="Wrong source parameter")

  data = read_json_data() if source == "json" else read_csv_data()

  if product_id:
    filtered_data = [product for product in data if product["id"] == product_id]
    if not filtered_data:
      return render_template("product_display.html", error="Product not found")
    data = filtered_data

  return render_template("product_display.html", products=data)

@app.route('/items')
def show_items():
    with open('items.json', 'r') as f:
        data = json.load(f)
        items = data['items']

    return render_template('items.html', items=items)


if __name__ == "__main__":
  app.run(debug=True)