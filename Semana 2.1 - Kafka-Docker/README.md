# Docker compose com Kafka e Zookeeper

Atividade desenvolvida nesse repositório consiste na criação de um docker-compose com todos os parâmetros de um kafka e seus gerenciadores, além de um exemplo de produção e consumo de mensagem local. Para essa atividade, foi utilizado a API da Riot Games, que fornece dados de partidas de League of Legends, para que seja possível realizar a produção de mensagens e o consumo das mesmas.

## Tecnologias para execução

- WSL (Windows Subsystem for Linux):
    - O WSL é um recurso do Windows que permite a execução de distribuições Linux em um ambiente Windows. Foi usado para habilitar a execução de ferramentas e comandos Linux no ambiente Windows.

- Docker e Docker Compose:
    - O Docker é uma plataforma de virtualização de contêineres que permite criar, implantar e gerenciar aplicativos em contêineres. O Docker Compose é uma ferramenta que simplifica a definição e execução de múltiplos contêineres como parte de uma aplicação.

- Kafka:
    - Apache Kafka é uma plataforma de streaming distribuído que permite a publicação, assinatura e processamento de fluxos de eventos em tempo real. É amplamente utilizado para construir sistemas de mensagens em tempo real e processamento de dados em larga escala.

- Zookeeper:
    - ZooKeeper é um serviço de coordenação distribuída que é frequentemente usado em conjunto com o Apache Kafka para gerenciar o cluster Kafka e manter o estado dos nós do cluster.

- Python:
    - Python é uma linguagem de programação de alto nível conhecida pela sua simplicidade e legibilidade. Foi utilizado para desenvolver scripts e aplicativos que interagem com o Kafka.

- Confluent-Kafka:
    - Confluent-Kafka é uma biblioteca para Python que fornece uma interface para se comunicar com o Apache Kafka. Ela simplifica a produção e consumo de mensagens Kafka a partir de aplicativos Python.

- Outras bibliotecas Python:
    - Além do Confluent-Kafka, você mencionou o uso de outras bibliotecas Python que provavelmente desempenham funções específicas no seu projeto. Essas bibliotecas podem incluir módulos de processamento de dados, manipulação de configurações ou interações com outros sistemas.

## Pré-requisitos para execução

- Instalação do WSL:
    - Para instalar o WSL, siga as instruções do link: https://docs.microsoft.com/pt-br/windows/wsl/install-win10

- Instalação do Docker:
    - Para instalar o Docker, siga as instruções do link: https://docs.docker.com/docker-for-windows/install/

- Instalação do Docker Compose:
    - Para instalar o Docker Compose, siga as instruções do link: https://docs.docker.com/compose/install/

- Instalação do Python:
    - Para instalar o Python, siga as instruções do link: https://www.python.org/downloads/ [IMPORTANTE: Instalar dentro do WSL]

- Para a instanciação das outras tecnologias citadas anteriormente, irei recomendar alguns conteúdos abaixo:
    - [Aprenda a configurar o WSL do zero](https://www.youtube.com/watch?v=rpvjVtUPnOc&t=280s)
    - [Aprenda a configurar o Docker e integrar com VS Code](https://www.youtube.com/watch?v=ecj7FLt6chg)
    - [Aprenda a Kafka do zero](https://www.youtube.com/watch?v=_EuccnmMpPo)

## Alertas
Recomenda-se que o usuário tenha conhecimento prévio sobre as tecnologias citadas anteriormente, pois não será abordado conceitos básicos sobre as mesmas. Além disso, é recomendado que seja desenvolvido primeiramente o arquivo "consumer.py" e depois o "producer.py", pois o Kafka não armazena as mensagens em disco, apenas em memória, ou seja, se o consumidor não estiver ativo, as mensagens serão perdidas.

- Após a instalação do WSL, Docker e Docker Compose, é necessário reiniciar o computador para que as alterações sejam aplicadas. Após ter seguido todos os passos, execute o comando abaixo para verificar se o Docker está instalado corretamente:

```bash
docker --version
```
Após essa etapa, puxe os arquivos demonstrados no repositório, para um diretório do seu espaço Linux, e execute o comando abaixo para instanciar todos os serviços apresentados no docker-compose.yml:

```bash
docker-compose up
```

## Execução do producer e consumer de mensagens Kafka

O projeto desenvolvido inclui dois notebooks Python que demonstram como produzir e consumir mensagens Kafka a partir de um aplicativo Python.

- **`consumer.ipynb`**:
    - O consumer.ipynb é um notebook em Python que se conecta a um tópico Kafka e consome mensagens desse tópico. Ele imprime as mensagens consumidas no console.
Para rodá-lo, basta execcutar as células do notebook.

- **`producer.ipynb`**:
    - O producer.ipynb é um notebook em Python que se conecta a um tópico Kafka e produz mensagens nesse tópico. Ele lê as mensagens da API da Riot em JSON e as envia para o tópico Kafka.
Para rodá-lo, basta execcutar as células do notebook.

## Resultados esperados
1. Inicializar o docker-compose.yml e verificar se inicializou todos os containers e serviços.
2. Executar o consumer.py e verificar se o mesmo está esperando para consumir as mensagens do producer.py.
3. Executar o producer.py e verificar se o mesmo está produzindo as mensagens e se o consumer.py está consumindo as mensagens.
4. Verificar se as mensagens estão sendo consumidas corretamente pela célula do notebook.

## Referências
1. API da Riot Games: https://developer.riotgames.com/apis#match-v5/
2. Documentação do Docker: https://docs.docker.com/
3. Conteúdo sobre Kafka: https://medium.com/trainingcenter/apache-kafka-838882261e83
4. Conteúdo sobre Kafka: https://medium.com/trainingcenter/apache-kafka-codifica%C3%A7%C3%A3o-na-pratica-9c6a4142a08f