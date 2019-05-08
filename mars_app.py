from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app)

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    destination_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", vacation=destination_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    def scrape():

    # Run scrapped functions
    mars_info = mongo.db.mars_info
    mars_data = scrape_mars.news_title()
    mars_data = scrape_mars.news_p()
    mars_data = scrape_mars.featured_image_url()
    mars_data = scrape_mars.mars_weather()
    mars_data = scrape_mars.facts_table()
    mars_data = scrape_mars.hemisphere_image_urls()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
