from src.model.Entities.Message import Message

assistant = Message("Mistral", True)
while True:
    user = input('Você: ')
    assistant.send_message(user)
    print('')
