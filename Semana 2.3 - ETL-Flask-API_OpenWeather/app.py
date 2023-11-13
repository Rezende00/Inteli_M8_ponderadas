import pandas as pd
import requests
import json
from datetime import datetime
from flask import Flask, jsonify
import sqlite3
from sqlalchemy import create_engine

app = Flask(__name__)

dez_cidades = ['São Paulo', 
                'Rio de Janeiro', 
                'Belo Horizonte', 
                'Niterói', 
                'Sabará', 
                'São Gonçalo', 
                'Vitória', 
                'Guarulhos', 
                'Manhuaçu', 
                'Manhumirim']

url = "https://api.openweathermap.org/data/2.5/weather"

parametros = {
    'appid': '6d9d34c9d2f45611b182a33f1fb56e9a',
    'units': 'metric',
}

def coletar_dados():
    dados = []
    for cidade in dez_cidades:
        parametros['q'] = cidade
        resposta = requests.get(url, params=parametros)
        if resposta.status_code == 200:
            dados.append(resposta.json())
        else:
            print(f"Error - Cidade não encontrada: {resposta.status_code} - {resposta.reason}")
    return dados

def limpar_tabela():
    conn = sqlite3.connect('dataWeather.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM dados_tempo')
    conn.commit()
    conn.close()

def criar_tabela():
    data_recente = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    data = coletar_dados()
    data = [json.dumps(item) for item in data]
    
    dados_df = {
        'Data de Ingestão': [data_recente] * len(data),
        'Tipo': [f"Clima {cidade}" for cidade in dez_cidades],
        'Valores': data,
        'Uso': ["Previsão do Tempo"] * len(data)
    }
    
    df = pd.DataFrame(dados_df)
    
    engine = create_engine('sqlite:///dataWeather.db', echo=False)
    
    df.to_sql('dados_tempo', con=engine, if_exists='append', index=False)
    
    return df

@app.route('/')
def api_tempo():
    criar_tabela()
    conn = sqlite3.connect('dataWeather.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dados_tempo")
    resultado = cursor.fetchall()
    conn.close()
    return jsonify(resultado)

@app.route('/clear_data')
def clear_data():
    limpar_tabela()
    return 'Tabela do banco de dados foi esvaziada.'

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)