import customtkinter as CTk

#class InformationMessage(CTk.CTkTopLevel):
class InformationMessage(CTk.CTkToplevel):
    def __init__(self, master, title: str, message: str, *args, **kwargs):
        super().__init__(master)

        self.geometry('450x150')
        self.title(title)
        self.configure(fg_color='white')

        self.information = CTk.CTkLabel(self, text=message, text_color='black', font=('Arial', 14, 'bold'))
        self.information.place(relx=0.5, rely=0.5, anchor='center', y=-20)

        self.button = CTk.CTkButton(self, command=self.button_click, text= 'Confirmar', fg_color='green', text_color='white')
        self.button.place(relx=0.5, rely=1.0, anchor='s', y=-10)

    def button_click(self):
        self.destroy()

if __name__ == '__main__':
    ...
    