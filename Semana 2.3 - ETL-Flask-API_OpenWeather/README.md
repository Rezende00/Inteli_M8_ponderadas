# OpenWeather - ETL em Flask
![OpenWeather Logo](https://openweathermap.org/themes/openweathermap/assets/img/logo_white_cropped.png)

## Introdução
Este projeto consiste em uma aplicação Flask que realiza uma ETL (Extração, Transformação e Carga) de dados climáticos de mais de 10 cidades do Brasil da API OpenWeather (pública e gratuita) para uma tabela no banco de dados SQLite3, guardando as informações em 4 colunas: Data da Ingestão, Tipo, Valores, Uso. Além disso, inclui testes de integração para garantir o correto funcionamento das funcionalidades.

## Explicações sobre o projeto


## Requisitos

- Python 3.6 ou superior
- Instalação das dependências do arquivo requirements.txt (será dada instrução de instalação no tópico de configuração)
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

## Configuração do Flask
Certifique-se de ter o Python instalado. Em seguida, instale as dependências necessárias usando o comando:


pip install -r requirements.txt

Para executar a aplicação, utilize o seguinte comando:

python app.py


A aplicação estará disponível em http://127.0.0.1:5000/.

## ETL (Extração, Transformação e Carga)

Função `coletar_dados()`
Esta função realiza a extração de dados climáticos da API OpenWeather para mais de 10 cidades brasileiras. Em caso de erro na requisição, um log é exibido indicando a cidade com problema.

Função `limpar_tabela()`
Esta função realiza a limpeza da tabela no banco de dados SQLite (dados_tempo), removendo todos os registros.

Função `criar_tabela()`
Esta função realiza a transformação dos dados obtidos pela função coletar_dados e os armazena na tabela dados_tempo. A tabela é composta por quatro colunas: Data de Ingestão, Tipo, Valores e Uso.

## Testes
Os testes de integração são implementados utilizando a biblioteca pytest. Eles abrangem cenários de sucesso e cenários de erro para as funções coletar_dados, limpar_tabela e criar_tabela. Certifique-se de instalar as dependências de teste antes de executar os testes:

pip install -r requirements.txt

Execute os testes com o comando:

pytest test_app.py
