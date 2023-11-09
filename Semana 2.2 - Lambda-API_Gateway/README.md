# Lambda com API Gateway na AWS

## Descrição

Este projeto é uma solução que integra o AWS Lambda com a AWS API Gateway, com o objetivo de criar um Endpoint REST altamente seguro e eficiente para processar mensagens autenticadas. O README fornecido com o projeto inclui detalhes sobre como configurar, executar e testar a solução, bem como informações sobre a estrutura do código e os testes unitários. Este projeto é uma base sólida para criar serviços de mensagens seguros e escaláveis na AWS.

## Pré-requisitos

- Conta na AWS academy ou AWS normal (com acesso aos serviços)
- Python >=3.8 instalado
- Vscode instalado
- Extensão Thunder Client instalada no Vscode

## **Desenvolvimento**

   Antes de prosseguir, certifique-se de ter uma conta na AWS academy (ou a normal) e de ter suas credenciais. 

### 1. Acesso à AWS Academy - Vocareum
   Siga o passo a passo para dar start ao seu ambiente na AWS:

- Acesse o Laboratório da AWS Academy e clique em Start Lab, após a conclusão do processo, clique em Open Console(bolinha verde).
    ![Acesso ao Labs](a_start_aws.png)

- Abrindo o console da aws academy, pesquise pelo serviço da Lambda:
![console](a_start_aws.png)
   
### 2. Acesso ao serviço Lambda
- Acesso ao serviço Lambda e clique em "Funções" no menu lateral esquerdo.
![console](a_start_aws.png)

- Após isso, clique em "criar função", para criar uma função lambda e siga os passos abaixo para completar os campos necessários:
![console](a_start_aws.png)

### 3. Criação de um Gatilho - API Gateway
- Agora, faremos a criação de uma API Gateway, que será um gatilho da nossa função.
![console](a_start_aws.png)
![console](a_start_aws.png)

- Agora, será necessário fazer a configuração da API Gateway, para estabelecer a comunicação com a função lambda e estar de acordo com o que foi proposto no projeto.
![console](a_start_aws.png)
![console](a_start_aws.png)
- Para selecionar qual a função lambda que será utilizada, copie o ARN da função lambda e cole no campo "Função Lambda":
![console](a_start_aws.png)
![console](a_start_aws.png)

- Agora, você possui um endpoint da sua API Gateway, que será utilizado para fazer as requisições HTTP, além de já ter configurado ela para fazer requisições POST. Então, vamos testar?

### 4. Configuração do VSCode
- IMPORTANTE: Verificar se a instalação do vscode está de acordo com o que foi proposto no pré-requisito.

- Instalação da extensão Thunder Client
![console](a_start_aws.png)

### 5. Contrução do código da função lambda

- A seguir, será apresentado o código da função lambda, que será utilizado para fazer a autenticação do usuário e senha, além de fazer o processamento de uma mensagem que será enviada e recebida pelo thunder client.

![console](a_start_aws.png)

```
import base64
import json

class APIGatewayAuthenticator:
    def __init__(self, users):
        self.users = users

    def authenticate(self, event):
        headers = event.get('headers', {})
        authorization_header = headers.get('Authorization', '')

        if not authorization_header:
            return {
                'statusCode': 401,
                'body': 'Acesso não autorizado'
            }

        if authorization_header.startswith('Basic '):
            encoded_credentials = authorization_header[len('Basic '):]
            credentials = base64.b64decode(encoded_credentials).decode('utf-8')

            user, password = credentials.split(':')

            if user in self.users and self.users[user] == password:
                return {
                    'statusCode': 200,
                    'body': json.dumps(event['body'])
                }

        return {
            'statusCode': 401,
            'body': 'Acesso não autorizado'
        }

def lambda_handler(event, context):
    users = {
        "pedro": "rezende",
    }
    
    authenticator = APIGatewayAuthenticator(users)
    return authenticator.authenticate(event)
```

- PS: Ao inserir o código, não esqueça de dar deploy para atualizar a função lambda e o endpoint da API Gateway.


### 6. Teste da função lambda

- Agora, vamos testar a função lambda, para isso, vamos utilizar o thunder client.

- Primeiramente, vamos fazer uma requisição POST para o endpoint da API Gateway, para isso, copie o endpoint da API Gateway e cole no thunder client, além de selecionar o método POST.
![console](endpoint.png)

- Disponibilizarei um body, com um json, para a requisição POST, que será utilizado para testar a função lambda.

```
{
    {"book": {"title": "O Senhor dos Anéis", "author": "J.R.R. Tolkien", "year": 1954}}
}
```

![console](post_thunder.png)


- Além disso, é necessário passar o Auth Basic, que será o usuário e senha, que foi definido na função lambda, para isso, clique em "Auth - Basic" e preencha os campos com o usuário e senha, respectivos, que foram apresentados no código.

![console](auth_thunder.png)

### 7. Teste da função lambda

- Com tudo preparado, basta clicar em "Send" e verificar o resultado da requisição.

![console](final.png)

- PS: Caso o acesso dê "Acesso não autorizado", verifique se o usuário e senha estão corretos, além de verificar se o endpoint da API Gateway está correto.

### 8. Endpoint REST
- O Lambda foi integrado com o API Gateway para criar um endpoint REST. Você pode acessar o endpoint REST no seguinte URL:
https://ce9crkozg1.execute-api.us-east-1.amazonaws.com/default/First_Test 

## Testes

- Está sendo disponibilizado um script em python para simulação e cumprimento de testes da atividade, para isso, basta executar o script no terminal.

```
python teste.py
```

- Além disso, esterei disponibilizando prints, com a execução de testes dentro da AWS. Como por exemplo, uma simulação de um Acesso Não Autorizado:
![console](a_start_aws.png)
![console](a_start_aws.png)
![console](a_start_aws.png)

# **Referências**
- Algumas das prints demonstradas foram disponibilizadas pelo estudante e colega de trabalho, Lucas Britto.
- A excução da tarefa foi feita em conjunto com:
    - Dayllan Alho,
    - Izabella Frias,
    - Lucas Britto,
    - Giovanna Furlan.