# ChatBot de IA Offline
Desenvolvido para atuar como uma interface local de interação e execução de modelos de Inteligência Artifical locais, atualmente suporta apenas modelos de texto da Ollama.
O projeto ainda em fase de desenvolvimento.
## Funcionalidades do projeto:
|Já implementadas|Futuras implementações|
|:------------------|:------------------|
|Atualmente, você já pode se beneficiar de:| Em um futuro próximo, pretendo implementar:|
|- Memória persistente, a IA se lembra de toda sua conversa.|- Memória inteligente / Retrieval-Augmented Generation. (RAG)|
|- Utilização de qualquer modelo Ollama para geração de texto.|- Criação de múltiplos chats.|
|- Interface se ajusta ao tamanho do seu monitor.|- Geração de imagens.|
|- Suporte a vários usuários.|- Criptografia no banco de dados.|


## Como ter o seu próprio Chatbot:
Para utilização do programa, basta apenas:
1. Baixar os arquivos do projeto.
2. Instalar as bibliotecas necessárias no arquivo requirements.txt:
   - Na pasta raiz do projeto, na 'Chatbot', abra o terminal e digite -> ```python pip install -r requirements.txt```
   - Esse comando vai instalar automaticamente todas as bibliotecas presentes no arquivo, só esperar um pouco. 
3. Caso não tenha um modelo LLM instalado, vá no site da Ollama -> https://www.ollama.com/search
4. Realize o processo de instalação do modelo desejado.
   - Aviso: Cuidado com modelos que tem 7/8b parâmetos! Eles precisam de um computador mais potente para funcionar!
   - Recomendação pessoal: Comece usando modelos mais leves como 1.5b e vá aumentando a partir daí.
5. Abrir o projeto na sua IDE e executar o arquivo Main!

## Primeiros passos:
Assim que abrir o chatbot, vai precisar fazer algumas coisas para conseguir usar:
   1. Criar seu perfil de usuário.
   2. Ir em "Perfil", no canto superior esquerdo da tela.
   3. Definir o modelo que vai usar em "Modelo de texto".
   4. Apertar em confirmar.

Pronto, agora é só usar! Sempre que quiser mudar de modelo é só fazer o mesmo processo.


## Requisitos necessários:
- Ter alguma IDE que rode Python, em breve irei disponibilizar um executável do projeto.
- Ter o Python instalado, versão utilizada: 3.13.2
- Sistema Operacional: Windows. (Não tive a chance de testar em outros SOs)

Observações: Por ser algo local, a experiência de utilização dos modelos depende muito da configuração do seu computador, recomendo começar com modelos com 1/2b parâmetros e ir aumentando até encontrar um equilíbrio entre a qualidade e o tempo de resposta.



Gostou do projeto, tem alguma sugestão ou tá fazendo algo parecido? Me chama aí, bora conversar!
