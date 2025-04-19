# Mineração de Conhecimento com Azure AI Search: Minha Experiência Prática

## Introdução

E aí, pessoal! Acabei de finalizar um projeto super interessante na área de IA para o bootcamp da DIO. Trabalhei com ferramentas de mineração de conhecimento usando o Azure AI Search e queria compartilhar com vocês como foi esse processo!

Neste projeto, precisei organizar e extrair insights de um conjunto de avaliações de clientes de uma cafeteria fictícia chamada "Fourth Coffee". Sem essas ferramentas de IA, analisar manualmente todo esse conteúdo seria um pesadelo, principalmente quando precisamos extrair informações específicas como sentimentos, locais mencionados e palavras-chave importantes.

## O que eu aprendi e fiz

### Configurando o ambiente no Azure

Primeiro, precisei criar alguns recursos no Azure:

- Um serviço de **Azure AI Search** (escolhi o plano Basic pra economizar)
- Um recurso de **Azure AI Services** pra usar as funcionalidades de IA
- Uma **conta de armazenamento** pra guardar os documentos originais e resultados

Foi bem tranquilo de configurar, mas confesso que demorei um pouco pra entender como tudo se conectava. Basicamente, o Azure AI Search usa as habilidades do Azure AI Services para processar os documentos armazenados no Storage.

### Subindo os documentos para análise

Baixei os arquivos de avaliações dos clientes do link que o professor disponibilizou e criei um container chamado `coffee-reviews` na minha conta de armazenamento. Depois, fiz o upload de tudo para lá. São vários documentos em formato de texto e algumas imagens também.

### A parte mais legal: processamento com IA!

Aí veio a parte que achei mais maneira do projeto. Usei o assistente de importação do Azure AI Search para:

1. Conectar na minha fonte de dados (o container com as avaliações)
2. Configurar um conjunto de "habilidades cognitivas" para extrair:
   - Locais mencionados nas avaliações
   - Frases-chave importantes
   - Sentimentos (positivo, negativo, neutro)
   - Tags e legendas para as imagens

Achei particularmente interessante a parte de extração de sentimentos. É impressionante como a IA consegue entender o tom de uma avaliação!

### Knowledge Store: salvando os resultados

Uma funcionalidade que não conhecia antes era o Knowledge Store. Basicamente, ele salva todos os dados enriquecidos em um formato estruturado para análises futuras. Configurei o sistema para salvar:

- Documentos completos processados
- Frases-chave extraídas
- Entidades (como locais)
- Informações de imagens

Isso criou várias tabelas na minha conta de armazenamento que posso acessar depois para análises mais detalhadas ou até conectar com o Power BI!

### Hora de testar: fazendo consultas

Depois que o indexador terminou de processar tudo (demorou uns 5 minutos), pude finalmente fazer algumas consultas no índice:

```
search=*&$count=true
```
Essa consulta retornou todas as avaliações - achei 21 documentos no total.

```
search=locations:'Chicago'
```
Com essa, filtrei só as avaliações que mencionavam Chicago - foram 3 resultados.

```
search=sentiment:'negative'
```
E aqui encontrei apenas 1 avaliação negativa! Ótimo para a cafeteria fictícia, né?

## O que descobri analisando os dados

Fazendo algumas análises, consegui extrair alguns insights interessantes:

1. A maioria das avaliações eram positivas (o que é um bom sinal!)
2. A única avaliação negativa mencionava problemas com o tempo de espera
3. As palavras-chave mais comuns estavam relacionadas ao "sabor do café", "ambiente" e "atendimento"
4. Várias avaliações mencionavam locais específicos, o que sugere que a cafeteria tem várias unidades

Achei muito maneiro como consegui extrair essas informações sem precisar ler manualmente cada avaliação!

## Dificuldades que enfrentei

Nem tudo foram flores! Tive alguns desafios pelo caminho:

- Entender a diferença entre skillset, indexer, index e data source foi confuso no começo
- Algumas configurações avançadas como "Base-64 Encode Keys" não estavam bem explicadas na documentação
- A primeira vez que executei o indexador, ele falhou porque esqueci de habilitar o acesso anônimo a blobs

Mas no final, depois de algumas tentativas e consultas à documentação, consegui resolver tudo!

## O que achei do projeto como um todo

Como estudante de ciência de dados, achei esse projeto muito relevante pro mercado atual. Muitas empresas têm toneladas de dados não estruturados (textos, imagens, etc.) e ferramentas como o Azure AI Search podem ajudar muito a extrair valor desses dados.

O legal é que, mesmo sem precisar programar muito (usei principalmente a interface do Azure), consegui criar um pipeline completo de processamento de dados. Claro que se eu quisesse customizar mais, poderia usar a API com Python ou mesmo integrar com outras ferramentas.

## Conclusão

No geral, foi uma experiência super válida! Consegui entender na prática como funciona um sistema de mineração de conhecimento e como as tecnologias de IA podem ser aplicadas em cenários reais de negócio.

A parte mais legal? Ver a máquina "entendendo" o conteúdo dos textos quase como um humano faria, extraindo sentimentos, identificando entidades e resumindo os pontos principais. Definitivamente vou considerar usar essas ferramentas em projetos futuros da faculdade e, quem sabe, no mercado de trabalho!

---

## Links úteis que me ajudaram

- [Documentação do Azure AI Search](https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search)
- [Tutorial oficial da Microsoft que segui](https://microsoftlearning.github.io/mslearn-ai-fundamentals/Instructions/Labs/11-ai-search.html)
- [Dicas de configuração de skillsets](https://learn.microsoft.com/en-us/azure/search/cognitive-search-defining-skillset)

---

_Projeto desenvolvido para o bootcamp de IA da DIO (Digital Innovation One)._
