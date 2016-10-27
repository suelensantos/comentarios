from flask import Flask, jsonify
from datetime import datetime
app = Flask(__name__)


@app.route('/comentarios/<int:post_id>')
def comentarios(post_id):
    coments = {
        'Nome': 'Suelen Santos',
        'Comentario': 'Hello, this is app comment.',
        'Data': datetime.now(),
        'ID': '01',
        'Post_ID': post_id
    }

    return jsonify(results=coments)


if __name__ == "__main__":
    app.run(port=8001, host='localhost', debug=True)
