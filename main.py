from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Page():
    return render_template("page_1.html")

@app.route("/my_work")
def page():
    return render_template("page_2.html")

@app.route("/your_shopping_list")
def shoppinglist_page():
    return render_template("yourshoppinglist.html")

@app.route("/portfolio_site")
def portfoliosite_page():
    return render_template("portfoliosite.html")

if __name__ == "__main__":
    app.run(debug=True)