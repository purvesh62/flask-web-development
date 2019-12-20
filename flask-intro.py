from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Purvesh Rathod',
        'title': 'Machine Learning',
        'content': 'Machine Learning Daily',
        'date_posted': 'December 20, 2019'
    },
    {
        'author': 'Harsh Mishra',
        'title': 'Java Programming',
        'content': 'Java Daily',
        'date_posted': 'December 20, 2019'
    },

]

@app.route('/')
def hello_world():
    return render_template('home.html',posts = posts)

@app.route('/about')
def about():
    return render_template('about.html',title = 'About')

if __name__ == '__main__':
    app.run()
