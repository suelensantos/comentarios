from flaskext.mysql import MySQL


def get_connect_mysql(app):
    mysql = MySQL()
    mysql.init_app(app)
    return mysql


def query(app, sql):  # get comentario
    mysql = get_connect_mysql(app)
    app.config.from_object('config.Config')
    cursor = mysql.connect().cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    return data


def insert(app, data):  # post comentario
    try:
        mysql = get_connect_mysql(app)
        app.config.from_object('config.Config')
        conn = mysql.connect()
        cursor = conn.cursor()
        sql = "insert into comentarios (nome, comentario, post_id, data) values ('%s', '%s', %s, '%s')" % (data['nome'], data['comentario'], data['post_id'], '2016-12-02')
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        return {'msg': 'Operacao efetuada com sucesso!'}
    except:
        return {'msg': 'Error'}
