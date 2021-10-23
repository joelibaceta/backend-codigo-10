from flask import Flask
from flaskext.mysql import MySQL

from flask import render_template
from flask import request

app  = Flask(__name__)

mysql = MySQL(  host="localhost", user="root", 
                password="rootcodigo", db="mydb")

mysql.init_app(app)

conn = mysql.connect()

@app.route("/")
def hello_world():
    return "hello world"

# /productos?q="blanco"
@app.route("/productos")
def get_productos():

    cursor = conn.cursor()
    query = request.args.get('q')

    sql = "SELECT p.idproducto, p.nombre, p.fechProduccion, p.precio, "
    sql = sql + "p.descripcion, c.nombre, m.nombre "
    sql = sql + "FROM producto AS p "
    sql = sql + "LEFT JOIN categoria AS c "
    sql = sql + "ON p.idcategoria = c.idcategoria "
    sql = sql + "LEFT JOIN marca AS m "
    sql = sql + "ON p.idmarca = m.idmarca "

    if query != None:
        sql = sql + f" WHERE p.nombre LIKE '%{query}%'"
        sql = sql + f" OR p.descripcion LIKE '%{query}%'"
        sql = sql + f" OR c.nombre LIKE '%{query}%'"
        sql = sql + f" OR m.nombre LIKE '%{query}%'"

    cursor.execute(sql)
    results = cursor.fetchall()

    return render_template("index.html", productos = results)