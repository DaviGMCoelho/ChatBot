# ChatBot de IA Offline
Desenvolvido para atuar como uma interface local de interação e execução de modelos de Inteligência Artifical locais, atualmente suporta apenas modelos de texto da Ollama.
O projeto ainda em fase de desenvolvimento.

---

## 🚀 Tecnologias utilizadas
- [Python 3.13.2](https://www.python.org/) → linguagem back-end
- [LangChain](https://www.langchain.com/) → orquestração do pipeline RAG e execução do modelo 
- [Chroma](https://www.trychroma.com/) → banco vetorial para armazenamento dos embeddings
- **Bibliotecas utilzadas:** Consulte requirements.txt
---

## 👨‍💻 Funcionalidades do projeto:
|Já implementadas|Futuras implementações|
|:------------------|:------------------|
|Atualmente, você pode usar:| Futuras implementações:|
|- Memória persistente, a IA se lembra de toda sua conversa.|- Memória inteligente / Retrieval-Augmented Generation. (RAG)|
|- Utilização de qualquer modelo Ollama para geração de texto.|- Criação de múltiplos chats.|
|- Interface se ajusta ao tamanho do seu monitor.|- Geração de imagens.|
|- Suporte a vários usuários.|- Criptografia no banco de dados.|

---

## 🏗️ Conceitos aplicados

Durante o desenvolvimento deste projeto, foram aprimorados diversos conceitos de engenharia de software:

- **Orientação a Objetos (OO)**: Arquitetura totalmente baseada em OO em Python, com classes bem definidas e responsabilidades claras.
- **MVC (Model-View-Controller-Services)**: Estrutura em camadas para separação de responsabilidades, facilitando manutenção e escalabilidade.

---

## 📥 Instalação

Baixe os arquivos do projeto e execute na sua IDE ou

Clone o repositório caso estiver com o Git instalado:

```bash
git clone https://github.com/seu-usuario/rag-pdf-ai.git
```

Crie e ative um ambiente virtual:

```bash
python -m venv venv
python -m .\venv\Scripts\activate # Windows
```

Instale as dependências:
```bash
python -m pip install -r requirements.txt
```

Caso não tenha um modelo instalado Ollama instalado, entre no [site oficial da Ollama](https://www.ollama.com/search) e escolha algum modelo.

Realize o processo de instalação.
- **Aviso:** Cuidado com modelos que tem 7/8b ou mais de parâmetos! Eles exigem um maior processamento para funcionar!
- **Recomendação:** Comece usando modelos mais leves como 1.5b e vá aumentando a partir daí.

Por fim, abra o projeto na sua IDE e execute o arquivo Main!

---

## ▶️ Como usar
Assim que abrir o chatbot, vai precisar fazer algumas coisas para conseguir usar:
   1. Criar seu perfil de usuário.
   2. Ir em "Perfil", no canto superior esquerdo da tela.
   3. Definir o modelo que vai usar em "Modelo de texto".
      -  Aqui vão ser exibidos todos os modelos que você tem instalado, é só escolher!
   4. Apertar em confirmar.

Pronto, agora é só usar! Sempre que quiser mudar de modelo é só fazer o mesmo processo.

---

## 💻 Requisitos necessários:
- Ter alguma IDE que rode Python, em breve irei disponibilizar um executável do projeto.
- Ter Python instalado, versão utilizada: 3.13.2
- Sistema Operacional: Windows 11. (Não pude testar em outros SOs e outras versões do Windows)

Observações: Por ser algo local, a experiência de utilização dos modelos depende muito da configuração do seu computador, recomendo começar com modelos com 1/2b parâmetros e ir aumentando até encontrar um equilíbrio entre a qualidade e o tempo de resposta.

---

## 📂 Estrutura do projeto

```bash
rag_project/
│── data/                
│   ├── database/        # Base de dados
│── docs/                # Protótipo de telas, implementações futuras
│── src/                 # Pasta onde são armazenadas as exceções
│   ├── controller/      # Lógica de controle
│   ├── manager/         # Lógica de gerenciamento dos modelos
│   ├── model/           # Estrutura de dados do sistema
│   ├── repository/      # Camada de requisição ao banco de dados
│   ├── service/         # Camada lógica e requisições
│   ├── utils/           # Códigos utilitários do sistema
│   ├── validation/      # Regras de validação
│   ├── view/            # Interface do sistema
│── main.py              # Ponto de entrada
│── README.md            # Arquivo de introdução
│── requirements.txt     # Bibliotecas utilizadas
```

Gostou do projeto, tem alguma sugestão ou tá fazendo algo parecido? Me chama aí, bora conversar!
Eu também sou freelancer, quer um específico para você? Só me chamar!
