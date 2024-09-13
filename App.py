from flask import Flask,request,url_for,render_template,make_response
import pandas as pd
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hellio, World!"
from markupsafe import escape

@app.route("/<name>")
@app.route("/name/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"mad{post_id}"
@app.route('/users/', defaults={'page': 1})
@app.route('/users/page/<int:page>')
def show_users(page):
    return f'valid page: {page}'

@app.route('/user/<username>/post/<int:post_id>')
def show_user_post(username, post_id):
    return f'User {username}, Post {post_id}'
@app.route('/files/<path:filename>')
def download_file(filename):
    return f'Downloading file {filename}'

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        return 'Handling POST request'
    return 'Handling GET request'
# if __name__=='__main__':
#     app.run()

@app.route('/login', subdomain='<subdomain>')
def login1(subdomain):
    return f'Login page for {subdomain}'


with app.test_request_context():
    # print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    # print(url_for('profile', username='John Doe'))

@app.route('/hello/')
@app.route('/hello/<name>')
def madllo(name=None):
    return render_template('hello.html', person=name)

with app.test_request_context('/manly', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/manly'
    assert request.method == 'POST'
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        
        f = request.files.get('gmiiot_email_setup')
        print('checking file',f)
        reading = pd.read_csv(f)
        reading.to_csv('gmiiot_email_setup1.csv')        
        # f.save('/var/www/uploads/uploaded_file.txt')

@app.route('/mad')
def index():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.


# @app.route('/max')
# def index():
#     resp = make_response(render_template(...))
#     resp.set_cookie('username', 'the username')
#     return resp
# float('inf')