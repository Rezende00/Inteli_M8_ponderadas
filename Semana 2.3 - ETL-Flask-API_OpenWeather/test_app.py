import pandas as pd
import requests
import sqlite3
import pytest
from app import coletar_dados, criar_tabela, limpar_tabela, app
from unittest.mock import patch

def testar_conexao_com_db():
    conn = limpar_tabela()
    assert conn is not None
    assert isinstance(conn, sqlite3.Connection)
    
def testar_conteudo_da_tabela():
    tabela = criar_tabela()
    conn = limpar_tabela()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tabela_tempo")
    resultados = cursor.fetchall()
    conn.close()
    assert len(resultados) == len(tabela)

def teste_coletar_dados():
    with patch('app.requests.get') as mock_get:
        mock_response = {'main': {'temp': 25.0}}
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        dados = coletar_dados()
        assert len(dados) == 1
        assert dados[0]['main']['temp'] == 25.0

        mock_get.return_value.status_code = 404
        dados_erro = coletar_dados()
        assert len(dados_erro) == 0

def testar_resposta_json():
    with app.test_client() as client:
        resposta = client.get('/tempo')
        assert resposta.status_code == 200
        dados_json = resposta.json()
        assert any('Data de Ingestão' in item for item in dados_json)
        assert any('Tipo' in item for item in dados_json)
        assert any('Valores' in item for item in dados_json)
        assert any('Uso' in item for item in dados_json)