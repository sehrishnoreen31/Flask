from flask import Flask, render_template
app = Flask(__name__)

# html
@app.route('/')
def index():
    return "<html><h1>My template</h1></html>"

# template
@app.route('/render/')
def rendered_temp():
    return render_template('index.html')

# jinja template
@app.route('/user/<user>/')
def rendered_user(user):
    return render_template('index.html', name=user)

# if else
@app.route('/student/<int:marks>/')
def result(marks):
    return render_template('index.html', marks=marks)

# dictionaries
@app.route('/detail/')
def result_detail():
    detail = {'name':'sehrish', 'marks':80}
    return render_template('result.html', detail=detail)

if __name__ == '__main__':
    app.run(debug=True)