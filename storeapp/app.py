from flask import Flask, request, jsonify
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

# post store items, to specific store
@app.post('/stores/<string:name>/item/')
def create_items(name):
    request_item = request.get_json()
    for store in stores:
        if store['name'] == name:
            store_items = [item['name'] for item in store['items']]
            if request_item['name'] in store_items:
                # only increase quantity, for later
                return {'message': 'item already exists'}, 409
            new_item = {'name': request_item['name'], 'price': request_item['price']}
            # validate data, for later
            store['items'].append(new_item)
        return jsonify(new_item), 201
    return {'message': 'invalid endpoint'}, 404

# get specific store's items
@app.get('/stores/<string:name>/item/')
def get_store_items(name):
    for store in stores:
        if store['name'] == name:
            return {'store_items': store}

if __name__ == '__main__':
    app.run(debug=True)