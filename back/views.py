from flask import Blueprint, render_template, send_from_directory
from model import database as db
import os
from flask import Flask, jsonify, request, session

main = Blueprint('main', __name__)

@main.context_processor
def inject_common_data():
    common_data = {
        'logo': 'images/logo.png',
        'style': 'css/styles.css'
    }
    return common_data

# Define a route within the Blueprint
@main.route('/')
def home():
    return render_template('home.html')

@main.route('/namorados')
def namorados():
    caixa =  []
    caixa = [{"nome":"Caixa G","img":"cesta1.jpg", "preco": 99.00,
            "desc":"Caixa dos namorados personalizada contendo: 1 bolo de coração, 1 presente, \
            4 doces, 1 bebida, 2 empadas, 1 biscoito salgado e decoração"}]
    caixa.append({"nome":"Caixa M","img":"cesta1.jpg", "preco": 79.00,
            "desc":"Caixa dos namorados personalizada contendo: 1 bolo de pote, 1 presente, \
            2 doces, 1 bebida, 2 empadas e decoração"})
    print(caixa)
    subprod = []
    subprod.append({"lista":"Bolo",
                "itens":[{"nome":"Modelo 1 bejinho", "image":"cesta1.jpg"},
                            {"nome":"Modelo 2 bejinho", "image":"bolo.jpg"},
                            {"nome":"Modelo 1 brigadeiro", "image":"cesta1.jpg"},
                            {"nome":"Modelo 2 brigadeiro", "image":"cesta1.jpg"}]})
    subprod.append({"lista":"Bebida",
                "itens":[{"nome":"Coca-cola lata", "image":"cesta1.jpg"},
                            {"nome":"Del Valle Uva lata", "image":"cesta1.jpg"},
                            {"nome":"Ice Tea garrafinha", "image":"cesta1.jpg"},
                            {"nome":"Iogurte morango", "image":"cesta1.jpg"}]})
    subprod.append({"lista":"Biscoito",
                "itens":[{"nome":"Doritos nacho", "image":"cesta2.png"},
                            {"nome":"2 torcidas queijo/cebola", "image":"cesta1.jpg"}]})
    subprod.append({"lista":"Presente",
                "itens":[{"nome":"Creme hidratante LoveSpell", "image":"cesta1.jpg"},
                            {"nome":"Carteira com fecho", "image":"cesta1.jpg"},
                            {"nome":"Batom HudaBeauty cor goiaba", "image":"cesta1.jpg"},
                            {"nome":"Caneca porcelana preta coração", "image":"cesta1.jpg"},
                            {"nome":"Copo 500ml Flamengo", "image":"cesta1.jpg"},
                            {"nome":"Copo 500ml Fluminense", "image":"cesta1.jpg"},
                            {"nome":"Copo 500ml Vasco", "image":"cesta1.jpg"}]})

    data = {
        'caixas': caixa,
        'subprod': subprod
    }   
    return render_template('namorados.html', **data)

@main.route('/db0000009')
def db_():
    con = db.PgDatabase.connect(db.PgDatabase)

    #sql_file_name = '.sql'
    #create2 = db.PgDatabase.execute_sql_file(db.PgDatabase,sql_file_name)

    data = {
        'title': 'Home Page',
        #'a1': str(create2),
        #'a2': str(create2)
    }    
    return render_template('home.html', **data)

@main.route('/static/<path:filename>')
def static(filename):
    return send_from_directory('static', filename)

@main.route('/select_product', methods=['POST', 'GET'])
def process_qt_calculation():
    if request.method == "POST":
        qtc_data = request.get_json()
        subprod = []
        if str(qtc_data[0]['caixa']) == "Caixa G":
            subprod.append({"lista":"Bolo",
                        "itens":[{"nome":"Modelo 1 bejinho", "image":"cesta1.jpg"},
                                 {"nome":"Modelo 2 bejinho", "image":"cesta1.jpg"},
                                 {"nome":"Modelo 1 brigadeiro", "image":"cesta1.jpg"},
                                 {"nome":"Modelo 2 brigadeiro", "image":"cesta1.jpg"}]})
            subprod.append({"lista":"Bebida",
                        "itens":[{"nome":"Coca-cola lata", "image":"cesta2.png"},
                                 {"nome":"Del Valle Uva lata", "image":"cesta1.jpg"},
                                 {"nome":"Ice Tea garrafinha", "image":"cesta1.jpg"},
                                 {"nome":"Iogurte morango", "image":"cesta1.jpg"}]})
            subprod.append({"lista":"Biscoito",
                        "itens":[{"nome":"Doritos nacho", "image":"cesta1.jpg"},
                                 {"nome":"2 torcidas queijo/cebola", "image":"cesta1.jpg"}]})
            subprod.append({"lista":"Presente",
                        "itens":[{"nome":"Creme hidratante LoveSpell", "image":"cesta1.jpg"},
                                 {"nome":"Carteira com fecho", "image":"cesta1.jpg"},
                                 {"nome":"Batom HudaBeauty cor goiaba", "image":"cesta1.jpg"},
                                 {"nome":"Caneca porcelana preta coração", "image":"cesta1.jpg"},
                                 {"nome":"Copo 500ml Flamengo", "image":"cesta1.jpg"},
                                 {"nome":"Copo 500ml Fluminense", "image":"cesta1.jpg"},
                                 {"nome":"Copo 500ml Vasco", "image":"cesta1.jpg"}]})
        elif str(qtc_data[0]['caixa']) == "Caixa M":
            subprod.append({"lista":"Bolo Pote",
                        "itens":[{"nome":"Prestígio", "image":"cesta1.jpg"},
                                 {"nome":"Cenoura com chocolate", "image":"cesta1.jpg"},
                                 {"nome":"Doce de banana", "image":"cesta1.jpg"}]})
            subprod.append({"lista":"Bebida",
                        "itens":[{"nome":"Coca-cola lata", "image":"cesta1.jpg"},
                                 {"nome":"Del Valle Uva lata", "image":"cesta1.jpg"},
                                 {"nome":"Ice Tea garrafinha", "image":"cesta1.jpg"},
                                 {"nome":"Iogurte morango", "image":"cesta1.jpg"}]})
            subprod.append({"lista":"Biscoito",
                        "itens":[{"nome":"Doritos nacho", "image":"cesta1.jpg"},
                                 {"nome":"2 torcidas queijo/cebola", "image":"cesta1.jpg"}]})
            subprod.append({"lista":"Presente",
                        "itens":[{"nome":"Creme hidratante LoveSpell", "image":"cesta1.jpg"},
                                 {"nome":"Carteira com fecho", "image":"cesta1.jpg"},
                                 {"nome":"Batom HudaBeauty cor goiaba", "image":"cesta1.jpg"},
                                 {"nome":"Caneca porcelana preta coração", "image":"cesta1.jpg"},
                                 {"nome":"Copo 500ml Flamengo", "image":"cesta1.jpg"},
                                 {"nome":"Copo 500ml Fluminense", "image":"cesta1.jpg"},
                                 {"nome":"Copo 500ml Vasco", "image":"cesta1.jpg"}]})

            print(subprod)   

        #db.session.add(Store_QTc_data(qtc_data[0]['QTc'], qtc_data[1]['prolonged'], qtc_data[2]['HR'], qtc_data[3]['QT'], qtc_data[4]['Sex']))
        #db.session.commit() 
        results = {'processed': 'true'}
        return jsonify(subprod)