# Knowledge Mining with Azure AI Search

**Author**: Gabriel Demetrios Lafis

---

## 🇬🇧 English

### 📋 Description

This project demonstrates a practical application of knowledge mining using **Azure AI Search** (formerly Azure Cognitive Search). The primary goal is to build an intelligent search solution capable of indexing, understanding, and extracting valuable insights from a dataset of unstructured customer reviews for a fictional coffee shop, "Fourth Coffee."

By leveraging a powerful combination of Azure AI services, this solution automates the analysis of large volumes of text and image data, transforming raw information into structured, actionable knowledge. This project serves as a comprehensive showcase of how modern AI can unlock hidden patterns and sentiments from customer feedback, providing a significant competitive advantage for any data-driven business.

### ✨ Features

- **Automated Data Ingestion**: Connects directly to Azure Blob Storage to seamlessly index new documents.
- **AI-Powered Enrichment Pipeline**: Utilizes a cognitive skillset to perform:
  - **Sentiment Analysis**: Automatically determines if customer feedback is positive, negative, or neutral.
  - **Key Phrase Extraction**: Identifies the most important talking points and topics within the reviews.
  - **Named Entity Recognition (NER)**: Extracts and categorizes entities such as locations, people, and organizations.
  - **Image Analysis**: Generates captions and tags for images included in the reviews.
- **Knowledge Store**: Persists the enriched data into structured tables in Azure Table Storage, making it available for deeper analytics and visualization in tools like Power BI.
- **Faceted Navigation & Advanced Queries**: Enables complex and intuitive querying of the indexed data, allowing for deep exploration of customer feedback.

### 🛠️ Tech Stack

- **Azure AI Search**: Core search and indexing service.
- **Azure AI Services**: Provides the cognitive skills for data enrichment.
- **Azure Blob Storage**: Stores the raw data (customer reviews).
- **Azure Table Storage**: Stores the structured, enriched data in the Knowledge Store.

### 🚀 Getting Started

#### Prerequisites

- An active **Azure Subscription**.
- **Azure CLI** or access to the **Azure Portal**.

#### Installation & Configuration

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/galafis/Azure-Cognitive-Search-Utilizando-AI-Search-para-indexa-o-e-consulta-de-Dados.git
    cd Azure-Cognitive-Search-Utilizando-AI-Search-para-indexa-o-e-consulta-de-Dados
    ```

2.  **Provision Azure Resources**:
    - Create an **Azure AI Search** resource (Basic tier or higher).
    - Create an **Azure AI Services** multi-service resource.
    - Create an **Azure Storage Account**.

3.  **Upload Data**:
    - In your Storage Account, create a blob container named `coffee-reviews`.
    - Upload the sample customer review documents (provided in the `/data` directory of this repository) to the container.

4.  **Configure the AI Search Pipeline**:
    - In the Azure Portal, navigate to your AI Search resource and launch the **Import data** wizard.
    - **Connect to your data**: Select Azure Blob Storage and point it to the `coffee-reviews` container.
    - **Add cognitive skills**: Attach your Azure AI Services resource and configure the following skills:
        - Sentiment Analysis
        - Key Phrase Extraction
        - Named Entity Recognition (Locations)
        - Image Analysis (Generate tags and captions)
    - **Define the index**: Specify the fields for your search index, ensuring they are retrievable, filterable, and searchable as needed.
    - **Configure the indexer**: Set a schedule for the indexer to run and process new data automatically.

### 💻 Usage

Once the indexer has successfully run, you can use the **Search explorer** in the Azure Portal to query your data. Here are a few examples:

- **Return all documents**:
  ```
  search=*&$count=true
  ```

- **Find reviews mentioning a specific location**:
  ```
  search=locations:'Chicago'
  ```

- **Find all negative reviews**:
  ```
  search=sentiment:'negative'
  ```

### 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🇧🇷 Português

### 📋 Descrição

Este projeto demonstra uma aplicação prática de mineração de conhecimento utilizando o **Azure AI Search** (anteriormente Azure Cognitive Search). O objetivo principal é construir uma solução de busca inteligente capaz de indexar, compreender e extrair insights valiosos de um conjunto de dados não estruturados de avaliações de clientes de uma cafeteria fictícia, a "Fourth Coffee".

Ao alavancar uma poderosa combinação de serviços de IA do Azure, esta solução automatiza a análise de grandes volumes de dados de texto e imagem, transformando informações brutas em conhecimento estruturado e acionável. Este projeto serve como uma vitrine abrangente de como a IA moderna pode desvendar padrões e sentimentos ocultos no feedback dos clientes, proporcionando uma vantagem competitiva significativa para qualquer negócio orientado a dados.

### ✨ Funcionalidades

- **Ingestão Automatizada de Dados**: Conecta-se diretamente ao Azure Blob Storage para indexar novos documentos de forma transparente.
- **Pipeline de Enriquecimento com IA**: Utiliza um conjunto de habilidades cognitivas para realizar:
  - **Análise de Sentimentos**: Determina automaticamente se o feedback do cliente é positivo, negativo ou neutro.
  - **Extração de Frases-Chave**: Identifica os pontos de discussão e tópicos mais importantes nas avaliações.
  - **Reconhecimento de Entidades Nomeadas (NER)**: Extrai e categoriza entidades como locais, pessoas e organizações.
  - **Análise de Imagens**: Gera legendas e tags para imagens incluídas nas avaliações.
- **Knowledge Store**: Persiste os dados enriquecidos em tabelas estruturadas no Azure Table Storage, disponibilizando-os para análises mais profundas e visualização em ferramentas como o Power BI.
- **Navegação Facetada e Consultas Avançadas**: Permite consultas complexas e intuitivas dos dados indexados, possibilitando uma exploração profunda do feedback dos clientes.

### 🛠️ Tecnologias Utilizadas

- **Azure AI Search**: Serviço principal de busca e indexação.
- **Azure AI Services**: Fornece as habilidades cognitivas para o enriquecimento de dados.
- **Azure Blob Storage**: Armazena os dados brutos (avaliações dos clientes).
- **Azure Table Storage**: Armazena os dados estruturados e enriquecidos no Knowledge Store.

### 🚀 Como Começar

#### Pré-requisitos

- Uma **Assinatura do Azure** ativa.
- **Azure CLI** ou acesso ao **Portal do Azure**.

#### Instalação e Configuração

1.  **Clonar o Repositório**:
    ```bash
    git clone https://github.com/galafis/Azure-Cognitive-Search-Utilizando-AI-Search-para-indexa-o-e-consulta-de-Dados.git
    cd Azure-Cognitive-Search-Utilizando-AI-Search-para-indexa-o-e-consulta-de-Dados
    ```

2.  **Provisionar Recursos no Azure**:
    - Crie um recurso do **Azure AI Search** (nível Basic ou superior).
    - Crie um recurso multi-serviço do **Azure AI Services**.
    - Crie uma **Conta de Armazenamento do Azure**.

3.  **Fazer Upload dos Dados**:
    - Na sua Conta de Armazenamento, crie um contêiner de blob chamado `coffee-reviews`.
    - Faça o upload dos documentos de avaliação de clientes de amostra (fornecidos no diretório `/data` deste repositório) para o contêiner.

4.  **Configurar o Pipeline do AI Search**:
    - No Portal do Azure, navegue até o seu recurso do AI Search e inicie o assistente **Importar dados**.
    - **Conectar-se aos seus dados**: Selecione o Azure Blob Storage e aponte para o contêiner `coffee-reviews`.
    - **Adicionar habilidades cognitivas**: Anexe seu recurso do Azure AI Services e configure as seguintes habilidades:
        - Análise de Sentimentos
        - Extração de Frases-Chave
        - Reconhecimento de Entidades Nomeadas (Locais)
        - Análise de Imagens (Gerar tags e legendas)
    - **Definir o índice**: Especifique os campos para o seu índice de busca, garantindo que sejam recuperáveis, filtráveis e pesquisáveis conforme necessário.
    - **Configurar o indexador**: Defina um cronograma para o indexador ser executado e processar novos dados automaticamente.

### 💻 Uso

Assim que o indexador for executado com sucesso, você pode usar o **Search explorer** no Portal do Azure para consultar seus dados. Aqui estão alguns exemplos:

- **Retornar todos os documentos**:
  ```
  search=*&$count=true
  ```

- **Encontrar avaliações que mencionam um local específico**:
  ```
  search=locations:'Chicago'
  ```

- **Encontrar todas as avaliações negativas**:
  ```
  search=sentiment:'negative'
  ```

### 📄 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

