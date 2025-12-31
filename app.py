from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

produtos = [
    {"id": 1, "Nome": "Farinha", "Preço": 2.5},
    {"id": 2, "Nome": "Arroz", "Preço": 5.0},
    {"id": 3, "Nome": "Feijão", "Preço": 6.2},
    {"id": 4, "Nome": "Açúcar", "Preço": 4.3},
    {"id": 5, "Nome": "Café", "Preço": 9.8},
    {"id": 6, "Nome": "Macarrão", "Preço": 3.5},
    {"id": 7, "Nome": "Óleo", "Preço": 7.9}
]

@app.route('/')
def home():
    return "/Settings para documentação"

@app.route('/Settings')
def doc():
    return render_template('index.html')


# 🔹 Listar todos os produtos
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    return jsonify(produtos)


# 🔹 Buscar produto por ID
@app.route('/produtos/<int:id>', methods=['GET'])
def buscar_produto(id):
    for produto in produtos:
        if produto["id"] == id:
            return jsonify(produto)
    return jsonify({"erro": "Produto não encontrado"}), 404


# 🔹 Adicionar produto
@app.route('/produtos', methods=['POST'])
def adicionar_produto():
    novo = request.json
    produtos.append(novo)
    return jsonify(novo), 201


# 🔹 Deletar produto
@app.route('/produtos/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    for produto in produtos:
        if produto["id"] == id:
            produtos.remove(produto)
            return jsonify({"msg": "Produto removido"})
    return jsonify({"erro": "Produto não encontrado"}), 404


app.run(host="127.0.0.1", port=5000, debug=True)
