from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data
posts = [
    {'id': 1, 'title': 'Post 1', 'content': 'Content of post 1'},
    {'id': 2, 'title': 'Post 2', 'content': 'Content of post 2'}
]

# Routes
@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:id>')
def post(id):
    post = next((post for post in posts if post['id'] == id), None)
    return render_template('post.html', post=post)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        posts.append({'id': len(posts)+1, 'title': title, 'content': content})
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/delete/<int:id>')
def delete(id):
    global posts
    posts = [post for post in posts if post['id'] != id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
