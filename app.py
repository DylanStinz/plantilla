from flask import Flask, render_template, request , redirect ,url_for ,flash
app.config["SECRET_KEY"]="una_clave_muy_larga_y_dificil_de_adivinar"
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
@app.route("/maravillas")
def maravillas():
    return render_template('maravillas.html')
@app.route("/acerca")
def contacto():
    return render_template('acerca.html') 
@app.route("/crear")
def crear():
    return render_template('crear.html') 
@app.route("/inicio")
def inicio():
    return render_template('inicio.html')
@app.registra("/crear", methods=["POST", "GET"])
def registrame():
    error=None
    if request.method=="POST":
            nombreCompleto=request.form["nombre"]
            email =request.form["email"]
            password=request.form["password"]
            confirmPassword=request.form["confirmPassword"]
            fechaNacimiento=request.form["fechaNacimiento"]
            genero=request.form["genero"]
            if password != confirmPassword:
                error="Las contraseñas no coinciden"
            if error != None:
                flash(error)
                return redirect(url_for("crear.html"))
            else:
                flash(f"registro exitoso, bienvenido {nombreCompleto}")
                return render_template("inicio.html")
if __name__ == '__main__':
    app.run(debug=True)