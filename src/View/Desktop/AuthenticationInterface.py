import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Controller.UserController import UserController
from View.Desktop.ViewUtils.InformationMessage import InformationMessage

import customtkinter as CTk

WIDTH_ENTRY = 190
WIDTH_BUTTOM = 100
FG_COLOR = 'White'
BORDER_COLOR = 'White'
TEXT_COLOR = 'Black'

class FrameDataSignin(CTk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.lbl_cod_profile = CTk.CTkLabel(self, text = 'Identificador:', font=('Arial', 12, 'bold'), text_color = TEXT_COLOR)
        self.lbl_cod_profile.grid(row=0, column=0, padx=5)
        self.ent_cod_profile = CTk.CTkEntry(self, placeholder_text = 'Insira seu código de usuário', width = WIDTH_ENTRY, fg_color = FG_COLOR, placeholder_text_color = TEXT_COLOR, text_color=TEXT_COLOR)
        self.ent_cod_profile.grid(row=0, column=1, padx=10)

        self.lbl_password = CTk.CTkLabel(self, text = 'Senha', font=('Arial', 12, 'bold'), text_color = TEXT_COLOR)
        self.lbl_password.grid(row=1, column=0, padx=5)
        self.ent_password = CTk.CTkEntry(self, placeholder_text = 'Insira sua senha', width = WIDTH_ENTRY, show = '*', fg_color = FG_COLOR, placeholder_text_color = TEXT_COLOR, text_color=TEXT_COLOR)
        self.ent_password.grid(row=1, column=1, padx=10)


class FrameButton(CTk.CTkFrame):
    def __init__(self, master, signin_frame, **kwargs):
        super().__init__(master, **kwargs)
        self.signin_frame = signin_frame
        self.btn_signin = CTk.CTkButton(self, text='Não tenho uma conta', command = lambda: self.open_RegisterInterface(signin_frame), text_color = TEXT_COLOR, font=('Arial', 12, 'underline'), fg_color = 'White', width=WIDTH_BUTTOM)
        self.btn_signin.grid(row=0, column=0, padx=(0, 10))

        self.btn_signup = CTk.CTkButton(self, text='Entrar', command = lambda: self.signin_frame.button_signin(), text_color = TEXT_COLOR, fg_color = 'Light Gray', width=WIDTH_BUTTOM)
        self.btn_signup.grid(row=0, column=1, padx=(10, 0))


    def open_RegisterInterface(self, signin_frame):
        from View.Desktop.RegisterInterface import RegisterInterface
        signin_frame.withdraw()
        register_window = RegisterInterface()
        register_window.mainloop()
    

class AuthenticationInterface(CTk.CTk):
    def __init__(self):
        super().__init__() # Pega o construtor da classe Pai
        self.geometry("350x320")
        self.title("Login de Usuário")
        self.configure(fg_color=FG_COLOR)
        self.resizable(False, False)

        self.lbl_main_title = CTk.CTkLabel(self, text = 'Seja bem vindo!', text_color = TEXT_COLOR, font=('Arial', 18, 'bold'))
        self.lbl_main_title.pack(padx=20, pady=(20, 0))
        self.lbl_desc = CTk.CTkLabel(self, text='Insira seus dados de acesso', text_color = TEXT_COLOR, font=('Arial', 14))
        self.lbl_desc.pack(padx=5, pady=10)

        self.frm_signin = FrameDataSignin(self, fg_color=FG_COLOR, border_color=BORDER_COLOR)
        self.frm_signin.pack(padx=5, pady=10)

        self.frm_button = FrameButton(self, signin_frame=self, fg_color=FG_COLOR, border_color=BORDER_COLOR)
        self.frm_button.pack(padx=5, pady=10, side='bottom')

    
    def button_signin(self):
        cod_profile = self.frm_signin.ent_cod_profile.get()
        password = self.frm_signin.ent_password.get()
        message = UserController.signin(cod_profile, password)
        InformationMessage(self, 'Sucesso', message['message'])


if __name__ == '__main__':
    ...