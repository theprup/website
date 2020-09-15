from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
     return render_template("/about.html")

@app.route("/blog")
def blog():
     return render_template("/blog.html")

@app.route("/bookshelf")
def bookshelf():
     return render_template("/bookshelf.html")


@app.route("/work")
def work():
     return render_template("/work.html")

if __name__ == "__main__":
    app.run(debug=False)
