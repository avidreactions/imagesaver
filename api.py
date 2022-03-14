from flask import Flask, render_template;
from app import grab_images;

app = Flask(__name__);

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route("/")
def home():
  return "<h1>Hello world</h1>";

@app.route("/about")
def about():
  return "<h1>This is the about page</h1>"

@app.route("/imagesaver")
def imagesaver():
  grab_images("https://www.ufc.com");
  return "<h1>RUNNING IMAGE SAVER</h1>"

if __name__ == "__main__":
  app.run(debug=True);