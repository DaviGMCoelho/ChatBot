import customtkinter as CTk

class BaseBubble(CTk.CTkFrame): # text_color, anchor
    def __init__(self, master, content, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(corner_radius=15)
        self.grid_columnconfigure(0, weight=1)

        self.content = CTk.CTkLabel(self, text=content, font=('Arial', 16, 'bold'), text_color='black')
        self.content.pack(fill='none', expand=False, padx=10, pady=2)

        self.after(100, self._set_wrap)

    def _set_wrap(self):
        largura_disponivel = int(self.master.winfo_width() * 0.7)
        largura_disponivel = max(200, min(largura_disponivel, 800))
        self.content.configure(wraplength=largura_disponivel)
        self.update_idletasks()


class UserBubble(BaseBubble):
    def __init__(self, master, content, **kwargs):
        super().__init__(master, content, **kwargs)
        self.configure(fg_color='green')
        self.content.configure(anchor='e')


class BotBubble(BaseBubble):
    def __init__(self, master, content, **kwargs):
        super().__init__(master, content, **kwargs)
        self.configure(fg_color='light gray')
        self.content.configure(anchor='w')
    

