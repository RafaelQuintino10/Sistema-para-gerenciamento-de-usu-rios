import customtkinter as custk


janela = custk.CTk()
janela.geometry('400x400')
janela.title('Trabalho RAD Python')
# Configuraraçãp das proporções das linhas e colunas
janela.grid_columnconfigure(0, weight=1)  # A coluna 0 deve se expandir
janela.grid_columnconfigure(1, weight=1)  # A coluna 1 deve se expandir
janela.grid_columnconfigure(2, weight=1)  # A coluna 2 deve se expandir
janela.grid_rowconfigure(0, weight=1)     # A linha 0 deve se expandir
janela.grid_rowconfigure(1, weight=0)     # A linha 1 não deve se expandir
janela.grid_rowconfigure(2, weight=0)     # A linha 2 não deve se expandir
janela.grid_rowconfigure(3, weight=1)     # A linha 3 deve se expandir
janela.grid_rowconfigure(4, weight=1)     # A linha 4 deve se expandir

texto = custk.CTkLabel(janela, text='Cadastro de usuários e gerenciamento de alimentos',font=('Helvetica', 24, 'bold'), text_color='#E0FFFF', wraplength=350)
texto.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

usuario_label = custk.CTkLabel(janela, text='Usuário:',font=('Helvetica', 14, 'bold'), text_color='#E0FFFF')
usuario_label.grid(row=1, column=0, padx=1, pady=10, sticky='e')

usuario = custk.CTkEntry(janela, placeholder_text='Digite o nome do usuário...')
usuario.grid(row=1, column=1,padx = 10, pady = 10, sticky='we')

idade_label = custk.CTkLabel(janela, text='Idade:',font=('Helvetica', 14, 'bold'), text_color='#E0FFFF')
idade_label.grid(row=2, column=0, padx=1, pady=10, sticky='e')

idade = custk.CTkEntry(janela, placeholder_text='Digite a idade do usuário...')
idade.grid(row=2, column=1,padx = 10, pady = 10, sticky='we')

botao = custk.CTkButton(janela, text='Cadastrar usuário',font=('Helvetica', 14, 'bold'),  fg_color='#1E90FF', command=0)
botao.grid(row=3, column=0, columnspan=4,padx=10, pady=10)


janela.mainloop()
