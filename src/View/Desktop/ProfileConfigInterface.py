import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))


from Controller.ChatbotController import ChatbotController
from Controller.UserController import UserController

import customtkinter as CTk

WIDTH_ENTRY = 190
WIDTH_BUTTOM = 100
FG_COLOR = 'White'
BORDER_COLOR = 'White'
TEXT_COLOR = 'Black'
IA_MODELS = ChatbotController.get_ia_models()

class ProfileConfigInterface(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("350x320")
        self.title("Configurações de Usuário")
        self.configure(fg_color=FG_COLOR)
        #self.resizable(False, False)

        #self.lbl_username = CTk.CTkLabel(self, text='Novo nome:', font=('Arial', 12, 'bold'), text_color = TEXT_COLOR)
        #self.lbl_username.grid(row=1, column=0, padx=5, pady=5)
        #self.ent_username = CTk.CTkEntry(self, placeholder_text = 'Insira seu novo nome', width = WIDTH_ENTRY, fg_color = FG_COLOR, placeholder_text_color = TEXT_COLOR, text_color=TEXT_COLOR)
        #self.ent_username.grid(row=1, column=1, padx=5, pady=5)

        self.lbl_dropdown = CTk.CTkLabel(self, text = 'Modelo de texto:', font=('Arial', 12, 'bold'), text_color = TEXT_COLOR)
        self.lbl_dropdown.grid(row=3, column=0, padx=5, pady=5)
        self.model_name = CTk.StringVar(value=ProfileConfigInterface.get_main_text_model())
        self.opt_modelsIA = CTk.CTkOptionMenu(self, values=IA_MODELS['message'], width = WIDTH_ENTRY, variable = self.model_name, font=('Arial', 12, 'bold'), text_color = TEXT_COLOR, dropdown_text_color = TEXT_COLOR, \
                                              button_color = 'light gray', button_hover_color='light gray', dropdown_fg_color='white', dropdown_hover_color='light gray', fg_color='white', command=self.get_model)
        self.opt_modelsIA.grid(row=3, column=1, padx=5, pady=5)

        self.btn_confirm = CTk.CTkButton(self, text='Confirm', command=self.confirm_alterations)
        self.btn_confirm.grid(row=4, column=0, padx=5, pady=5)


    def get_model(self, choice):
        self.model_name = CTk.StringVar(value=choice)

    def get_main_text_model():
        text_model = ChatbotController.get_main_models()
        if text_model['text_model']:
            return text_model['text_model']
        return 'Sem modelo definido'

    def confirm_alterations(self):
        model = self.model_name.get()
        UserController.edit_model(model)

if __name__ == '__main__':
    window = ProfileConfigInterface()
    window.mainloop()