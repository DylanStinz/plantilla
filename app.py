from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('base.html')
@app.route("/animal")
def animal():
    return render_template('animales.html')
@app.route("/vehiculos")
def vehiculos():
    return render_template('carros.html')
if __name__ == '__main__':
    app.run(debug=True)