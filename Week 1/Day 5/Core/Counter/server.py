from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello():
    counter = 0
    return render_template('index.html' , counter = counter)

if __name__ == '__main__':
    app.run(debug=True)