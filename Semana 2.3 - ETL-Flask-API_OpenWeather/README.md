# OpenWeather - ETL em Flask
![OpenWeather Logo](https://openweathermap.org/themes/openweathermap/assets/img/logo_white_cropped.png)

## Introdução
Este projeto consiste em uma aplicação Flask que realiza uma ETL (Extração, Transformação e Carga) de dados climáticos de mais de 10 cidades do Brasil da API OpenWeather (pública e gratuita) para uma tabela no banco de dados SQLite3, guardando as informações em 4 colunas: Data da Ingestão, Tipo, Valores, Uso. Além disso, inclui testes de integração para garantir o correto funcionamento das funcionalidades.

## Requisitos

- Python 3.6 ou superior
- Instalação das dependências do arquivo requirements.txt (será dada instrução de instalação no tópico de <a name="configuração-do-projeto">configuração</a>)
- Conta na API OpenWeather (https://openweathermap.org/api)
    - É necessário gerar uma chave de API para realizar as requisições. Para isso, basta criar uma conta no site e acessar a página de gerenciamento de chaves (https://home.openweathermap.org/api_keys). A chave gerada deve ser inserida no arquivo app.py, na variável API_KEY.
    - Porém, caso não queira utilizar uma chave própria, basta utilizar a chave já inserida no arquivo app.py. Ela é válida para requisições de teste.

## Estrutura do projeto
O projeto está divido em 3 arquivos principais:

- **app.py**: arquivo principal da aplicação, contendo as rotas e funções de ETL.
- **test_app.py**: arquivo de testes de integração.
- **dataWeather.db**: arquivo do banco de dados SQLite3.
- **requirements.txt**: arquivo contendo as dependências do projeto.

### Rotas da URL
O arquivo `app.py` contém as seguintes rotas:
- **`/`**: realiza a extração de dados da API OpenWeather, apresenta na tela em uma estrutura JSON os dados e os armazena no banco de dados.
- **`/clear_data`**: realiza a limpeza da tabela no banco de dados, para que seja possível realizar uma nova extração de dados.

## Explicações sobre o projeto

### Estrutura do banco de dados
O banco de dados utilizado é o SQLite3, que é um banco de dados relacional embutido. Ele é armazenado em um arquivo, que neste caso é o arquivo `dataWeather.db`. 
O banco de dados possui uma tabela chamada `dados_tempo`, que possui 4 colunas: Data de Ingestão, Tipo, Valores e Uso. A coluna Data de Ingestão armazena a data e hora em que os dados foram coletados. A coluna Tipo armazena o tipo de dado coletado (temperatura, umidade, pressão atmosférica, etc). A coluna Valores armazena os valores coletados. A coluna Uso armazena o uso do dado coletado (média, mínima, máxima, etc).

### ETL (Extração, Transformação e Carga)
Função `coletar_dados()`<br>
Esta função realiza a extração de dados climáticos da API OpenWeather para mais de 10 cidades brasileiras. Em caso de erro na requisição, um log é exibido indicando a cidade com problema.

Função `limpar_tabela()`<br>
Esta função realiza a conexão com o banco de dados SQLite e faz a limpeza da tabela (`dados_tempo`), removendo todos os registros (quando for acessado a rota `/clear_data`).

Função `criar_tabela()`<br>
Esta função realiza a transformação dos dados obtidos pela função coletar_dados e os armazena na tabela `dados_tempo`. A tabela é composta por quatro colunas: Data de Ingestão, Tipo, Valores e Uso.

### Testes de integração
Os testes de integração são implementados utilizando a biblioteca pytest. Eles abrangem cenários de sucesso para as funções coletar_dados, limpar_tabela e criar_tabela, além de um teste simples de resposta do JSON. Para executar os testes, basta executar o comando `pytest` no terminal junto com o arquivo de testes `test_app.py`.

## [Configuração do Projeto](#configuração-do-projeto)
Certifique-se de ter o Python instalado de acordo com os requisitos do projeto. Além disso, após baixar o projeto em seu computador, sugere-se a criação de um ambiente virtual para a instalação das dependências. Para isso, basta executar o seguinte comando no terminal:
```python
python -m venv venv
```

- Isso ajudará a manter as dependências do projeto separadas de outros projetos que você possa ter em seu computador.
- Além disso, sugere-se que seja utilizado a IDE VsCode para a execução do projeto.

### Instalação das dependências
Após a criação do ambiente virtual, instale as dependências necessárias usando o comando:
```python
pip install -r requirements.txt
```

IMPORTANTE: certifique-se de estar na pasta raiz do projeto ao executar o comando, além de estar com o ambiente virtual ativado.

```python
(diretório do ambiente virtual) 
cd env/Scripts/activate
```

### Execução da aplicação
Para executar a aplicação, utilize o seguinte comando:
```python
python app.py
```
- A aplicação estará disponível em http://127.0.0.1:5000/.
- Após visualizar o JSON, vá até o arquivo `dataWeather.db` e verifique se os dados foram armazenados corretamente.
- Para isso, baixe a extensão do VsCode SQLViewer e abra o arquivo `dataWeather.db` para visualizar a tabela `dados_tempo`, com seus respectivos dados apresentados no JSON.

### Execução dos testes
Para executar os testes é necessário que a aplicação esteja rodando, caso não esteja, é provável que um ou mais testes falhem, mas vale a pena testar. Para rodar, utilize o seguinte comando:
```python
pytest test_app.py
```
- É esperado que 100% dos testes funcionem corretamente.

# Agradecimentos
Agradeço aos meus colegas de turma que me ajudaram no desenvolvimento da atividade:
- Dayllan Alho
- Patrick Miranda