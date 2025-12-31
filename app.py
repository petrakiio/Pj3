from flask import Flask,jsonify,request

app = Flask(__name__)

produtos = [
    {
        "id": 1,
        "Nome": "Farinha",
        "Preço": 2.5
    },
    {
        "id": 2,
        "Nome": "Arroz",
        "Preço": 5.0
    },
    {
        "id": 3,
        "Nome": "Feijão",
        "Preço": 6.2
    },
    {
        "id": 4,
        "Nome": "Açúcar",
        "Preço": 4.3
    },
    {
        "id": 5,
        "Nome": "Café",
        "Preço": 9.8
    },
    {
        "id": 6,
        "Nome": "Macarrão",
        "Preço": 3.5
    },
    {
        "id": 7,
        "Nome": "Óleo",
        "Preço": 7.9
    }
]

@app.route('/')
def home():
    return "De um "