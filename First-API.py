from flask import Flask, request

app = Flask(__name__)

stores1 = [
    {"name": "arroz", "price":"5000"}
]


@app.get("/store")
def get_stores():
    return {"stores": stores1}

@app.get('/store/<string:store_name>')
def getProduct(store_name):
    stores_find = [store for store in stores1 if store['name'] == store_name]
    if (len(stores_find) > 0):
        return ({"store": stores_find[0]})
    return ({"Message": "store no encontrada"})

@app.post('/store')
def post_stores():
    store_new = {
        "name": request.json['name'],
        "price": request.json['price']
    }
    stores1.append(store_new)
    return ({"message": "Store añadida"})

@app.delete('/store/<string:store_name>')
def store_delete(store_name):
    stores_find = [store for store in stores1 if store['name'] == store_name]
    if len(stores_find) > 0:
        stores1.remove(stores_find[0])
        return(
            {
                "message": "Store borrada"
            }
        )
    return ({"message": "Store no encontrada"})

@app.put('/store/<string:store_name>')
def store_update(store_name):
    stores_find =[store for store in stores1 if store['name'] == store_name]
    if (len(stores_find)>0):
        stores_find[0]['name'] = request.json['name']
        stores_find[0]['price'] = request.json['price']
        return ({
            "message":"Store actualizada"
        })

if __name__ == '__main__':
    app.run(debug=True, port=4500)