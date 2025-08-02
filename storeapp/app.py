from flask import Flask, request
app = Flask(__name__)

stores = [
    {
        'name': 'my store',
        'items': [
            {
                'name': 'chair',
                'price': 230.0
            }
        ]
    }
]

# get request
@app.get('/stores/')
def get_stores():
    return {'stores': stores}



if __name__ == '__main__':
    app.run(debug=True)