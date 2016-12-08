# -*- coding: utf-8 -*-

from mysql_connect import query, get_connect_mysql, insert
from flask import Flask, jsonify, request
app = Flask(__name__)

# precisa ver se tem q colocar na ordem dos elementos do database (nome, comentario, data, post_id)
def comentarios(post_id):  # get comentario
    data = query(app, "SELECT * FROM comentarios WHERE post_id=%d ORDER BY data DESC, post_id DESC" % post_id)
    data_result = list()
    for elem in data:
        temp = dict()
        temp[elem[0]] = {'nome': elem[1], 'comentario': elem[2], 'data': elem[3], 'post_id': elem[4]}
        data_result.append(temp)
    return jsonify(results=data_result)


def post_comentario():  # post comentario
    msg = insert(app, request.get_json())
    return jsonify(result=msg)

# Fazer TESTES para todos os arquivos
# Ao retornar um jsonify, ele retorna uma lista com uma lista de dic.. tem q retornar um json
# {"result": {
#    {
#      7,
#      "zezinho",
#      "Muito bom...",
#      "Fri, 02 Dec 2016 00:00:00 GMT",
#      39
#    }
# }
# Fazer as Exceções nas funções query e insert de mysql_connect.py

# Para rodar no terminal, basta levantar o servidor em uma aba e na outra joga o curl (e aperta enter)
# curl -X POST http://localhost:8001/comentarios/post_comentario --data '{"nome": "chiquinho", "comentario": "Legal!", "post_id": 39}' -H 'Content-Type: application/json'


if __name__ == "__main__":
    get_connect_mysql(app)
    app.run(port=8001, host='localhost', debug=True)
