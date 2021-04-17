from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index.html")
def Page():
    return render_template("index.html")

@app.route("/page_2.html)
def page():
    return render_template("page_2.html")

@app.route("/yourshoppinglist.html")
def shoppinglist_page():
    return render_template("yourshoppinglist.html")

@app.route("/portfoliosite.html")
def portfoliosite_page():
    return render_template("portfoliosite.html")

if __name__ == "__main__":
    app.run(debug=True)