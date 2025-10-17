from flask import Flask, render_template, request , redirect ,url_for ,flash

app = Flask(__name__)
app.config["SECRET_KEY"]="una_clave_muy_larga_y_dificil_de_adivinar"
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
@app.route("/crear", methods=["GET", "POST"])
def crear():
    error = None
    if request.method == "POST":
        nombreCompleto = request.form.get("nombre")
        apellido = request.form.get("apellido")
        email = request.form.get("email")
        password = request.form.get("password")
        confirmPassword = request.form.get("confirmPassword")
        fechaNacimiento = request.form.get("fechaNacimiento")
        genero = request.form.get("genero")
        genero_personalizado = request.form.get("genero_personalizado")

        if password != confirmPassword:
            error = "Las contraseñas no coinciden"
        elif not nombreCompleto or not email or not password:
            error = "Todos los campos obligatorios deben completarse."

        if error:
            flash(error)
            return redirect(url_for("crear"))
        else:
            flash(f"Registro exitoso, bienvenido/a {nombreCompleto} {apellido}")
            return redirect(url_for("index"))
    return render_template("crear.html")

@app.route("/inicio")
def inicio():
    return render_template('inicio.html')

if __name__ == '__main__':
    app.run(debug=True)