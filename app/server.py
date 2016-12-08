from flask import Flask
from views import comentarios, post_comentario
app = Flask(__name__)

app.add_url_rule(
    '/comentarios/<int:post_id>',
    view_func=comentarios
)
app.add_url_rule(
    '/comentarios/post_comentario',
    view_func=post_comentario, methods=['POST']
)


if __name__ == "__main__":
    app.run(port=8001, host='localhost', debug=True)
