from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

db = client.mars_db
collection = db.mars_data_coll

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_mission_data = mars_data_coll.find_one()

    # Return template and data
    return render_template("index.html", mars_info=mars_mission_data)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run scrapped functions
    # ? mars_results = mongo.db.mars_info
    mars_info = scrape_mars.scrape_info()
    mars_info = scrape_mars.news_title()
    mars_info = scrape_mars.news_p()
    mars_info = scrape_mars.featured_image_url()
    mars_info = scrape_mars.mars_weather()
    mars_info = scrape_mars.facts_table()
    mars_info = scrape_mars.hemisphere_image_urls()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_info, upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
