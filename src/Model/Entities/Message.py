class Message:
    def __init__(self, origin, content):
        self.origin = origin
        self.content = content

    def generate_message(self):
        return {'role': self.origin, 'content': self.content}

