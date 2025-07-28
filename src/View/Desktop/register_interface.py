import customtkinter as CTk

from src.controller.user_controller import UserController
from src.view.desktop.ViewUtils.InformationMessage import InformationMessage
from src.view.desktop.chatbot_interface import ChatBotMainInterface

WIDTH_ENTRY = 190
WIDTH_BUTTOM = 100
FG_COLOR = 'White'
BORDER_COLOR = 'White'
TEXT_COLOR = 'Black'

class FrameDataSignup(CTk.CTkFrame):
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

        self.lbl_conf_password = CTk.CTkLabel(self, text = 'Confirmação de Senha', font=('Arial', 12, 'bold'), text_color = TEXT_COLOR)
        self.lbl_conf_password.grid(row=2, column=0, padx=5)
        self.ent_conf_password = CTk.CTkEntry(self, placeholder_text = 'Insira sua senha novamente', width = WIDTH_ENTRY, show = '*', fg_color = FG_COLOR, placeholder_text_color = TEXT_COLOR, text_color=TEXT_COLOR)
        self.ent_conf_password.grid(row=2, column=1, padx=10)


class FrameButton(CTk.CTkFrame):
    def __init__(self, master, signup_frame, **kwargs):
        super().__init__(master, **kwargs)
        self.signup_frame = signup_frame
        self.btn_signin = CTk.CTkButton(self, text='Já tenho uma conta', command = lambda: self.open_AuthenticationInterface(signup_frame), 
                                        text_color = TEXT_COLOR, font=('Arial', 12, 'underline'), fg_color = 'White', width=WIDTH_BUTTOM)
        self.btn_signin.grid(row=0, column=0, padx=(0, 10))

        self.btn_signup = CTk.CTkButton(self, text='Cadastrar', command = lambda: self.signup_frame.button_signup(), text_color = TEXT_COLOR, fg_color = 'Light Gray', width=WIDTH_BUTTOM)
        self.btn_signup.grid(row=0, column=1, padx=(10, 0))


    def open_AuthenticationInterface(self, signup_frame):
        from src.view.desktop.authentication_interface import AuthenticationInterface
        signup_frame.withdraw()
        register_window = AuthenticationInterface()
        register_window.mainloop()


class RegisterInterface(CTk.CTk):
    def __init__(self):
        super().__init__() # Pega o construtor da classe Pai
        self.geometry("350x320")
        self.title("Cadastro de Usuário")
        self.configure(fg_color=FG_COLOR)
        self.resizable(False, False)

        self.lbl_main_title = CTk.CTkLabel(self, text = 'Seja bem vindo!', text_color = TEXT_COLOR, font=('Arial', 18, 'bold'))
        self.lbl_main_title.pack(padx=20, pady=(20, 0))
        self.lbl_desc = CTk.CTkLabel(self, text='Insira seus dados para se cadastrar!', text_color = TEXT_COLOR, font=('Arial', 14))
        self.lbl_desc.pack(padx=5, pady=10)

        self.frm_signup = FrameDataSignup(self, fg_color=FG_COLOR, border_color=BORDER_COLOR)
        self.frm_signup.pack(padx=5, pady=10)

        self.frm_button = FrameButton(self, signup_frame=self, fg_color=FG_COLOR, border_color=BORDER_COLOR)
        self.frm_button.pack(padx=5, pady=10, side='bottom')


    def button_signup(self):
        user = UserController()
        username = self.frm_signup.ent_username.get()
        password = self.frm_signup.ent_password.get()
        conf_password = self.frm_signup.ent_conf_password.get()
        message, cod_profile = user.signup(username, password, conf_password)
        if message['status']:
            title = 'Cadastro realizado com sucesso!'
            warning = f'Seu código de identificação: {cod_profile}, anote!'
            main_interface = ChatBotMainInterface()
            main_interface.mainloop()
        else:
            title = 'Ocorreu um erro!'
            warning = f'Erro: {message['message']}'
        InformationMessage(self, title, warning)
