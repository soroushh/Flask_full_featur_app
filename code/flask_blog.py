from flask import Flask, render_template
app = Flask(__name__)
people = [
    {
        "name":"soroush",
        "family":"Khosravi",
        "job": "software engineer"
    },
    {
        "name":"Farnaz",
        "family":"Khosravi",
        "job": "software engineer"
    }
]

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html', people=people)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)


