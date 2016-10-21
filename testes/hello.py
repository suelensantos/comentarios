from flask import Flask, url_for, request, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # pass
    # return 'Index Page'
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a 
    # KeyError if the cookie is missing


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        # do_the_login()
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password.'
    else:
        show_the_login_form()

    return render_template('login.html', error=error)


@app.route('/hello')
def hello_world():
    return 'Hello, World!'


@app.route('/user/<username>')
def show_user_profile(username):
    pass
    # show the user profile for that user
    # return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    pass
    # show the post with the given id, the id is an integer
    # return 'Post %d' % post_id


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


''' with app.test_request_context():
    print url_for('index')  # /
    print url_for('login')  # /login
    print url_for('login', next='/')  # /login?next=/
    print url_for('profile', username='John Doe')  # /user/John%20Doe '''


@app.route('/home/')
@app.route('/home/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
