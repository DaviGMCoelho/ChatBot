import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Controller.ChatbotController import ChatbotController
from View.Desktop.ViewUtils.ResponsiveDesign import ResponsiveDesign
from View.Desktop.ViewUtils.MessageBubbles import UserBubble, BotBubble

import customtkinter as CTk
FG_COLOR = '#878787'
BORDER_COLOR = '#878787'


class FrameChatMessages(CTk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.messages = []
        FrameChatMessages.load_message_history(self)

    def load_message_history(self):
        history = ChatbotController.get_message_history(self)
        for msg in history:
            origin = msg['role']
            content = msg['content']
            FrameChatMessages.add_message_chat(self, self, origin, content)
    
    def add_message_chat(self, message_frame, role, message):
        self.messages.append(message)
        if role == 'user':
            bubble = UserBubble(message_frame, message)
            bubble.pack(anchor="e", padx=10, pady=2)
        elif role == 'assistant':
            bubble = BotBubble(message_frame, message)
            bubble.pack(anchor="w", padx=10, pady=2)
        else:
            print(f'role: {role} \n message: {message}')

        self.after(10, lambda: self._parent_canvas.yview_moveto(1.0)) # Scroll automático
        self.update_idletasks()


class FrameEntryBox(CTk.CTkFrame):
    def __init__(self, master, data_frame, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.data_frame = data_frame
        
        self.width = (ResponsiveDesign.monitor_width(self) / 3) * 2.0
        self.input_text = CTk.CTkEntry(self, placeholder_text='Pergunte qualquer coisa!', height=40, width=self.width, bg_color = FG_COLOR)
        self.input_text.grid(row=0, column=0, sticky='nsew')
        self.button_send = CTk.CTkButton(self, height=40, width=40, bg_color = FG_COLOR, text = 'Send', command=lambda: FrameEntryBox.get_message(self))
        self.button_send.grid(row=0, column=1, sticky='nsew', padx=5)

    def get_message(self):
        user_message = self.input_text.get()
        self.data_frame.add_message_chat(self.data_frame, 'user', user_message) # lento pra aparecer pq só acontece quando executa a função inteira
        model = ChatbotController('mistral') 
        response = model.send_response(user_message) # Passar thread sepárada pra melhorar performace / Interrompe a thread principal
        self.data_frame.add_message_chat(self.data_frame, 'assistant', response)


class FrameChatbot(CTk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.width = (ResponsiveDesign.monitor_width(self) / 3) * 2.0 + 12
        self.height = (ResponsiveDesign.monitor_height(self) / 1.141)
        self.frm_ChatMessages = FrameChatMessages(self, fg_color = '#C0C0C0', border_color = '#C0C0C0', width = self.width, height = self.height)
        self.frm_ChatMessages.pack()
        self.frm_EntryBox = FrameEntryBox(self, self.frm_ChatMessages, fg_color = '#878787', border_color = '#878787', width = self.width)
        self.frm_EntryBox.pack(padx=5, pady=5)
        
        

class FrameOptionChats(CTk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.width = (ResponsiveDesign.monitor_width(self) / 3) + 12
        self.height = (ResponsiveDesign.monitor_height(self) / 1.141)


class ChatBotMainInterface(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.title('ChatBot')
        self.width = ResponsiveDesign.monitor_width(self)
        self.height = ResponsiveDesign.monitor_height(self)
        self.geometry(f'{self.width}x{self.height}+0+0')
        self.configure(fg_color = FG_COLOR)

        self.option_chats_frame = FrameOptionChats(self, fg_color = 'black', border_color = 'black')
        self.option_chats_frame.grid(row=0, column=0)

        self.chatbot_frame = FrameChatbot(self, fg_color = "#878787", border_color = '#878787')
        self.chatbot_frame.grid(row=0, column=1)


if __name__ == '__main__':
    window = ChatBotMainInterface()
    window.mainloop()