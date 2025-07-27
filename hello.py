from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

@app.route('/page')
def page():
    return 'Other Page'

@app.route('/page3')
def page3():
    return 'Page 3'

if __name__ == '__main__':
    app.run(debug=True)
