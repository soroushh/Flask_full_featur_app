from flask import Flask, render_template
app = Flask(__name__)
posts =[
    {
        "author":"sroush",
        "title":"hey I am soroush",
        "date": "tomorrow"
    },
    {
        "author":"farnaz",
        "title":"hey I am farnaz",
        "date": "tomorrow"
    }

]

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)


