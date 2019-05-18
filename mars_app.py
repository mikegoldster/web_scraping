from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pymongo
import mission_to_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
#
# client =
# db = client.mars_db
# coll = db.mars_data_coll

# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    mars_info = mongo.db.mars_info.find_one()
    return render_template("index.html", mars_info=mars_info)

# from mission_to_mars.py import mars_info

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    mars_info = mission_to_mars.scrape()
    mongo.db.mars_info.update(
        {},
        mars_info,
        upsert=True
    )
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
