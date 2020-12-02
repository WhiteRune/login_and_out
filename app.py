from flask import Flask, render_template, request, make_response, session

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/login', methods=['GET', 'POST'])
def get_and_post_request():
    if request.method == 'GET' and session['username'] == 'Anonymous':
        return """
         <form action='http://localhost:5000/login', method='POST'>
             <input name="username">
             <input type="submit">
         </form>
        """

    elif request.method == 'POST':
        session['username'] = request.form['username']
        username = session['username']
        return render_template('logged.html', username=username)

    else:
        return"""<h1> You are already logged in.</h1>"""


@app.route('/')
def get_count_of_user_visits_by_cookie():
    if session.get('username'):
        username = session['username']
    else:
        session['username'] = 'Anonymous'
        username = session['username']
    visited = 0
    if request.cookies.get('visited'):
        visited = int(request.cookies['visited'])

    response = make_response(render_template('index.html', visited=visited, username=username))
    response.set_cookie('visited', str(visited + 1))
    return response


@app.route('/logout')
def logout():
    if session['username'] == 'Anonymous':
        return """<h1> You are not logged in to logout. </h1>"""
    else:
        session['username'] = 'Anonymous'
        return """<h1> You are logged out. </h1>"""


if __name__ == '__main__':
    app.run(debug=True)
