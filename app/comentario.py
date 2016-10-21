import os
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/comentarios/<int:post_id>')
def comentarios(post_id):

    return render_template('comentario.html', post_id=post_id)


if __name__ == "__main__":
    PORT = os.getenv('PORT', 8001)
    app.run(port=int(PORT), host='localhost', debug=True)
