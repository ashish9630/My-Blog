from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/technology")
def technology():
    return render_template("technology.html")

@app.route("/lifestyle")
def lifestyle():
    return render_template("lifestyle.html")

@app.route("/travel")
def travel():
    return render_template("travel.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")  
def contact():
    return render_template("contact.html")
    
if __name__ == "__main__":
    app.run(debug=True)    