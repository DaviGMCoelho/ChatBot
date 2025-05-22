from ollama import chat

class Message:
    def __init__(self, model: str, stream: bool):
        self.model = model
        self.stream = stream

    def send_message(self, content: str):
        stream = chat(
            model = self.model, # Define o modelo a ser usado
            messages=[{"role": "user", "content": content}], # role | content : conteúdo que será usado pra responder 
            stream=self.stream
        )

        for chunk in stream: # Pra cada pedaço da mensagem
            print(chunk["message"]["content"], end='', flush=True) # Flush imprime a mensagem a medida que é gerada


assistant = MessageSender("Mistral", True)
while True:
    user = input('Você: ')
    assistant.send_message(user)
    print('')
