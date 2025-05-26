import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", '..')))

from src.model.Entities.User import User

import customtkinter as CTk

WIDTH_ENTRY = 190
WIDTH_BUTTOM = 100
FG_COLOR = 'White'
BORDER_COLOR = 'White'
TEXT_COLOR = 'Black'


class FrameDatas(CTk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.lbl_username = CTk.CTkLabel(self, text = 'Apelido:', font=('Arial', 12, 'bold'), text_color = TEXT_COLOR)
        self.lbl_username.grid(row=0, column=0, padx=5)
        self.ent_username = CTk.CTkEntry(self, placeholder_text = 'Insira seu nome de usuário', width = WIDTH_ENTRY, fg_color = FG_COLOR, placeholder_text_color = TEXT_COLOR, text_color=TEXT_COLOR)
        self.ent_username.grid(row=0, column=1, padx=10)

        self.lbl_password = CTk.CTkLabel(self, text = 'Senha', font=('Arial', 12, 'bold'), text_color = TEXT_COLOR)
        self.lbl_password.grid(row=1, column=0, padx=5)
        self.ent_password = CTk.CTkEntry(self, placeholder_text = 'Insira sua senha', width = WIDTH_ENTRY, show = '*', fg_color = FG_COLOR, placeholder_text_color = TEXT_COLOR, text_color=TEXT_COLOR)
        self.ent_password.grid(row=1, column=1, padx=10)

        self.lbl_conf_password = CTk.CTkLabel(self, text = 'Confirmar senha', font=('Arial', 12, 'bold'), text_color = TEXT_COLOR)
        self.lbl_conf_password.grid(row=2, column=0, padx=5)
        self.ent_conf_password = CTk.CTkEntry(self, placeholder_text = 'Digite novamente sua senha', width = WIDTH_ENTRY, show = '*', fg_color = FG_COLOR, placeholder_text_color = TEXT_COLOR, text_color=TEXT_COLOR)
        self.ent_conf_password.grid(row=2, column=1, padx=10)




class FrameButton(CTk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.btn_signin = CTk.CTkButton(self, text='Cadastrar dados', command = SignupInterface.button_signup, text_color = TEXT_COLOR, fg_color = 'Light Gray', width=WIDTH_BUTTOM)
        self.btn_signin.grid(row=0, column=0, padx=(0, 10))

        self.btn_signup = CTk.CTkButton(self, text='Entrar', command = SignupInterface.button_signin, text_color = TEXT_COLOR, fg_color = 'Light Gray', width=WIDTH_BUTTOM)
        self.btn_signup.grid(row=0, column=1, padx=(10, 0))
    

class SignupInterface(CTk.CTk):
    def __init__(self):
        super().__init__() # Pega o construtor da classe Pai
        self.geometry("350x320")
        self.title("Cadastro de Usuário")
        self.configure(fg_color=FG_COLOR)
        self.resizable(False, False)

        self.lbl_main_title = CTk.CTkLabel(self, text = 'Seja bem vindo!', font = ('Arial', 18, 'bold'), text_color = TEXT_COLOR)
        self.lbl_main_title.pack(padx=20, pady=(20, 0))
        self.lbl_desc = CTk.CTkLabel(self, text='''Insira seus dados e em seguida
        aperte no botão correspondente''', text_color = TEXT_COLOR)
        self.lbl_desc.pack(padx=5, pady=10)
        self.frm_datas = FrameDatas(self, fg_color=FG_COLOR, border_color=BORDER_COLOR)
        self.frm_datas.pack(padx=5, pady=10)
        self.frm_button = FrameButton(self, fg_color=FG_COLOR, border_color=BORDER_COLOR)
        self.frm_button.pack(padx=5, pady=10, side='bottom')

    def button_signin(self):
        print(vars(User))
        
    def button_signup(self):
        User(self.frm_datas.ent_password.get(), self.frm_datas.ent_conf_password.get())
        print(vars(User))


window = SignupInterface()
window.mainloop()