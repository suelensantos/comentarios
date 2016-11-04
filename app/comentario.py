from flaskext.mysql import MySQL
from flask import Flask, jsonify
from datetime import datetime
app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'comentarios_blog'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

# vai ser a mesma url, mas dependendo do post_id, 
# vai printar apenas aqueles que contém o mesmo valor

@app.route('/comentarios/<int:post_id>')
def comentarios(post_id):
    # comments = {
    #     'nome': 'Suelen Santos',
    #     'comentario': 'Hello, this is app comment.',
    #     'data': datetime.now(),
    #     'id': 1,
    #     'post_id': post_id
    # }
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * FROM comentarios WHERE post_id='" + post_id + "' ORDER BY DESC ")
    data = cursor.fetchone()
    # verificar o q sai nessa data

    return jsonify(result=comments)


if __name__ == "__main__":
    app.run(port=8001, host='localhost', debug=True)
