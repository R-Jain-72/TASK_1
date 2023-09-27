from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    title = "Food Theory"
    author = "Rishabh"
    content = "Food theory is the study of food and cooking from a scientific perspective which has attracted me to follow how things revolve around all things food"
    return render_template("index.html", title=title, author=author, content=content)

if __name__ == "__main__":
    app.run(debug=True)
