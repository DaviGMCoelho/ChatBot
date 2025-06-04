from ollama import chat

class Message:
    def __init__(self, cod_chat: str, origin: str, message_type: str):
        self.cod_chat = cod_chat
        self.origin = origin
        self.message_type = message_type


    def send_message(self, content: str):
        stream = chat(
            model = self.model, # Define o modelo a ser usado
            messages=[{"role": "user", "content": content}], # role | content : conteúdo que será usado pra responder 
            stream=self.stream
        )

        for chunk in stream: # Pra cada pedaço da mensagem
            print(chunk["message"]["content"], end='', flush=True) # Flush imprime a mensagem a medida que é gerada