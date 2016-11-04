from flask import Flask, jsonify
from datetime import datetime
app = Flask(__name__)


@app.route('/comentarios/<int:post_id>')
def comentarios(post_id):
    comments = {
        'nome': 'Suelen Santos',
        'comentario': 'Hello, this is app comment.',
        'data': datetime.now(),
        'id': 01,
        'post_id': post_id
    }

    return jsonify(result=comments)


if __name__ == "__main__":
    app.run(port=8001, host='localhost', debug=True)
