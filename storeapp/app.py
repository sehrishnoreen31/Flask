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

# post request
@app.post('/stores/')
def create_stores():
    request_data = request.get_json()
    store_names = [store['name'] for store in stores]
    if request_data['name'] in store_names:
        return {'message': 'store already exists'}, 409
    else:
        new_store = {'name': request_data['name'], 'items': []}
        stores.append(new_store)
        return new_store, 201
        

if __name__ == '__main__':
    app.run(debug=True)