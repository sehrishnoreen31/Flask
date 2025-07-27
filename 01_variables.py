from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return 'Home'

@app.route('/<name>/')
def name(name):
    return f'Hello {name}'

@app.route('/<int:id>/')
def id(id):
    return f'Your id: {id}'

@app.route('/<user>/<int:uid>/')
def id_f(user, uid):
    return f'{user} id: {uid}'

if __name__ == '__main__':
    app.run(debug=True)
    
'''
    trailing slash/
    Both the rules appear similar but in the second rule, trailing slash (/) is used.
    As a result, it becomes a canonical URL. 
    Hence, using /python or /python/ returns the same output. 
    However, in case of the first rule, /flask/ URL results in 404 Not Found page.
'''