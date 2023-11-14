import pandas as pd
import requests
import sqlite3
import pytest
from app import coletar_dados, criar_tabela, limpar_tabela, app
from unittest.mock import patch
from flask import Flask, jsonify
from sqlalchemy import create_engine

def teste_conectar_db():
    resultado = limpar_tabela()
    assert isinstance(type(resultado), type(sqlite3.Cursor))
    
def teste_criar_tabela():
    tabela = criar_tabela()
    assert isinstance(tabela, pd.DataFrame)

def teste_coletar_dados():
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
    
    with patch('app.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.side_effect = [
            {'main': {'temp': 25.0}},
            {'main': {'temp': 22.0}},
            {'main': {'temp': 20.0}},
            {'main': {'temp': 18.0}},
            {'main': {'temp': 15.0}},
            {'main': {'temp': 12.0}},
            {'main': {'temp': 10.0}},
            {'main': {'temp': 8.0}},
            {'main': {'temp': 5.0}},
            {'main': {'temp': 2.0}},
        ]

        dados = coletar_dados()
        assert len(dados) == len(dez_cidades)
        assert dados[0]['main']['temp'] == 25.0
        assert dados[1]['main']['temp'] == 22.0
        assert dados[2]['main']['temp'] == 20.0
        assert dados[3]['main']['temp'] == 18.0
        assert dados[4]['main']['temp'] == 15.0
        assert dados[5]['main']['temp'] == 12.0
        assert dados[6]['main']['temp'] == 10.0
        assert dados[7]['main']['temp'] == 8.0
        assert dados[8]['main']['temp'] == 5.0
        assert dados[9]['main']['temp'] == 2.0

def testar_resposta_json():
    with app.test_client() as client:
        resposta = client.get('/')
        assert resposta.status_code == 200
        dados_json = resposta.json