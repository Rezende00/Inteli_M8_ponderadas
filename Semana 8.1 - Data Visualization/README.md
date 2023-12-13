# Atividade de Criação de Data Visualization com Metabase, Grafana ou Power BI

## Sumário
[1. Objetivo ](#c1)<br>
[2. Descrição das Ferramentas e Escolha ](#c2)<br>
[3. Configuração da Ferramenta](#c3) <br>
[4. Criação de gráficos no Metabase](#c4)<br>

#### **Barema**:

- Escolha e justificativa da ferramenta de visualição de dados (Metabase, Grafafa ou PowerBI) para o projeto;
- Configuração correta da ferramenta escolhida para importar e processar os dados;
- Desenvolvimento de um dashboard ou visualização de dados que represente de forma eficaz as informações do dataset;
- Aplicação de técnicas adequadas de visualização para facilitar a interpretação e análise dos dados;
- Documentação completa da visualização, incluindo legenda, rótulos e uma interpretação clara dos dados apresentados;
- Explicação detalhada no readme do processo de escolha da ferramenta, configuração, criação da visualização e análise dos dados;
- A clareza e precisão na documentação e explicação serão avaliadas. Erros ortográficos e gramaticais serão penalizados, com desconto de até 20% dos pontos;

## <a name="c1">Objetivo</a>

O principal objetivo desta atividade de Visualização de Dados é fornecer uma representação visual eficaz e interpretável das informações contidas no conjunto de dados selecionado. Busco explorar as potencialidades de ferramentas de visualização, como Metabase, Grafana ou PowerBI, para apresentar insights valiosos que possam ser utilizados na tomada de decisões informadas. Tendo isso em vista, irei passar por todo o processo de escolha da ferramenta, configuração, criação da visualização e análise dos dados, como descrito no barema da atividade.

## <a name="c2">Descrição das Ferramentas e Escolha</a>

Para a escolha da ferramenta de visualização de dados tive que considerar diferentes aspectos, como a natureza dos dados, a facilidade de uso, a capacidade de personalização, a integração com outras ferramentas, entre outros. Sendo assim, realizei uma análise comparativa entre as ferramentas Metabase, Grafana e PowerBI, que são as mais populares e utilizadas no mercado. A seguir, apresento uma breve descrição de cada uma delas, de forma comparativa, com objetivo de esclarecer o processo de escolha.

<img src="assets/metabase_icon.png" alt="Metabase Icon" width="200">

O Metabase destaca-se como uma ferramenta de inteligência de negócios (BI) reconhecida por sua implementação ágil e facilidade de uso. Sua proposta é permitir que até mesmo usuários sem conhecimento avançado em SQL construam gráficos e obtenham insights por meio de uma interface amigável. Seu construtor de consultas visuais simplifica a criação de filtros, gráficos e dashboards, tornando a análise de dados acessível a todos. Além disso, o Metabase oferece a capacidade de construir modelos semânticos enriquecidos, promovendo consultas consistentes e eficientes.

O Metabase, como ferramenta de business intelligence de código aberto, vai além da simplicidade ao oferecer recursos avançados. Os administradores podem compartilhar painéis em tempo real, aprimorando o desempenho com insights detalhados apresentados em tabelas e gráficos de barras. O editor de notebook integrado e a compatibilidade com SQL possibilitam às equipes obter respostas conforme sua conveniência, ampliando a visualização com assinaturas, tabelas dinâmicas e variáveis em consultas interativas. A integração ativa com diversos bancos de dados externos, como MySQL, Amazon Redshift e outros, amplia ainda mais a versatilidade do Metabase.

<img src="assets/grafana_icon.png" alt="Grafana Icon" width="200">

O Grafana é uma plataforma de código aberto conhecida por sua flexibilidade e ampla aplicação, especialmente em monitoramento de operações de TI. Sua versatilidade é evidenciada pela integração fácil com diversas fontes de dados, como Prometheus, InfluxDB e Elasticsearch. O Grafana proporciona uma interface altamente personalizável, permitindo aos usuários criar painéis detalhados e atraentes para análises visuais abrangentes. Sua abordagem única de unificar dados de várias fontes em um único painel sem centralização fornece uma visão panorâmica, quebrando barreiras de dados. Além disso, a capacidade de compartilhamento de painéis fomenta a colaboração e a transparência nas equipes.

Grafana expande ainda mais sua utilidade, atendendo às necessidades de monitoramento em diversas áreas, desde métricas do Prometheus até registros, aplicativos e fontes de dados personalizadas. A plataforma Grafana Cloud oferece uma solução altamente disponível e gerenciada para coletar, analisar e alertar sobre métricas Graphite e Prometheus, bem como logs Loki. O Grafana Enterprise, com seus plug-ins corporativos, proporciona aos usuários acesso facilitado a fontes de dados existentes, otimizando a visualização de dados em soluções complexas e caras de monitoramento.

<img src="assets/powerbi_icon.png" alt="PowerBI Icon" width="200">

O Microsoft Power BI se destaca como uma plataforma de visualização de dados projetada para criar uma cultura orientada a dados e impulsionar a inteligência de negócios. A ferramenta facilita a criação e o compartilhamento de visualizações de dados avançadas, apoiando a tomada de decisões baseadas em dados. Sua interface empresarial simplificada torna a análise acessível a usuários com diferentes níveis de habilidade técnica. A integração com diversas fontes de dados e ferramentas, incluindo o Microsoft Excel, oferece flexibilidade aos usuários.

Power BI vai além, proporcionando uma governança robusta e recursos avançados de proteção de dados. Permite a aplicação de rótulos de confidencialidade reconhecíveis por meio de aplicativos do Office 365, garantindo conformidade com regulamentações e políticas de privacidade. Os usuários podem supervisionar dados confidenciais usando o Microsoft Cloud App Security, estendendo políticas de governança e proteção. A Proteção de Informações da Microsoft permite bloquear atividades arriscadas em tempo real, assegurando a confidencialidade dos dados. Além disso, o Power BI oferece recursos de aprendizado online para rápida adoção e disseminação do conhecimento na organização.

### Comparação técnica entre as ferramentas

Agora que temos uma noção de como cada uma das ferramentas funcionam, vamos fazer uma análise comparativa entre elas, considerando alguns aspectos importantes para a escolha da ferramenta de visualização de dados, com base nas necessidades da nossa atividade. A fonte que está sendo utilizada é do site 
<a href="https://www.saasworthy.com/compare/microsoft-power-bi-vs-grafana-vs-metabase?pIds=5042,5906,10031">"SaaSworthy"</a> - aqui você consegue acessar diretamente para a comparação técnica entre as 3 ferramentas.

<img src="assets/image.png" alt="PowerBI Icon" width="700">
<img src="assets/image 2.png" alt="PowerBI Icon" width="700">

### Escolha da Ferramenta

Após a análise comparativa entre as ferramentas, decidi escolher o **Metabase** para a realização da atividade de Visualização de Dados. A escolha foi baseada em alguns aspectos, como a facilidade de uso, a capacidade de personalização, a integração com outras ferramentas, entre outros. Porém, para destacar essa escolha, vou apresentar três pontos principais que me fizeram escolher o Metabase:

1. **Facilidade de uso**: O Metabase é uma ferramenta de visualização de dados que possui uma interface amigável e intuitiva, que permite que até mesmo usuários sem conhecimento avançado em SQL construam gráficos e obtenham insights por meio de uma interface amigável. Seu construtor de consultas visuais simplifica a criação de filtros, gráficos e dashboards, tornando a análise de dados acessível a todos. Além disso, o Metabase oferece a capacidade de construir modelos semânticos enriquecidos, promovendo consultas consistentes e eficientes.

2. **Precificação**: O Metabase é uma ferramenta de visualização de dados de código aberto, ou seja, é gratuito. Isso foi um fator decisivo para a escolha, pois não precisarei pagar nada para utilizar a ferramenta e realizar a atividade de Visualização de Dados.

3. **Já ter utilizado a ferramenta**: Já tive a oportunidade de utilizar o Metabase em um projeto de Data Visualization, onde tive que criar um dashboard para um cliente. Sendo assim, já tenho uma certa familiaridade com a ferramenta, o que facilitará o processo de criação da visualização de dados.

## <a name="c3">Configuração da Ferramenta</a>

<img src="assets/Docker_icon.png" alt="PowerBI Icon" width="180">
<img src="assets/metabase_icon.png" alt="PowerBI Icon" width="180">

### Passo 1: Confirmação do WSL2 e Docker Desktop
- Para seguir com esse tutorial, é necessário fazer a confirmação de que o WSL2 e o Docker Desktop estão instalados e funcionando corretamente. 
    - Recomendo a leitura do tutorial <a href="https://github.com/codeedu/wsl2-docker-quickstart">"wsl2-docker-quickstart"</a> para a instalação e configuração do WSL2 e Docker Desktop. 

### Passo 2: Instalação do Metabase via Docker
- Após a confirmação do WSL2 e Docker Desktop, vamos instalar o Metabase via Docker. Para isso, será necessário inicializar o Docker Desktop e abrir o seu terminal. Clique na tecla Windows (<img src="assets/windows_icon.svg" alt="PowerBI Icon" width="20">) e digite "CMD" para abrir o terminal do Windows.

1. No terminal, digite o seguinte comando para baixar a imagem mais recente do Metabase via Docker:
    ```bash
    docker pull metabase/metabase:latest
    ```
2. Após o download da imagem, digite o seguinte comando para criar um container do Metabase:
    ```bash
    docker run -d -p 3000:3000 --name metabase metabase/metabase
    ```
3. Para verificar se o container está rodando, digite o seguinte comando:
    ```bash
    docker ps
    ```
    - Se o container estiver rodando, você verá uma saída semelhante a essa:
        ```bash
        CONTAINER ID   IMAGE                 COMMAND                  CREATED          STATUS          PORTS                                       NAMES
        4b8b8b8b8b8b   metabase/metabase     "/app/run_metabase.sh"   10 minutes ago   Up 10 minutes
        ```

### Passo 3: Acessando o Metabase
- Para acessar o Metabase, abra o seu navegador e digite na URL (barra de pesquisa do navegador) o seguinte endereço <a href= "http://localhost:3000">"http://localhost:3000"</a>.

## <a name="c4">Criação de gráficos no Metabase</a>

### Abrindo o MetaBase

![Alt text](image.png)