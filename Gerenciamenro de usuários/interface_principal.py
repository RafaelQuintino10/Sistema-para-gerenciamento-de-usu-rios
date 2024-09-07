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
janela.grid_rowconfigure(3, weight=0)     # A linha 3 não deve se expandir
janela.grid_rowconfigure(4, weight=0)     # A linha 4 não deve se expandir
janela.grid_rowconfigure(5, weight=1)     # A linha 5 deve se expandir

texto = custk.CTkLabel(janela, text='Cadastro de usuários e gerenciamento de alimentos',font=('Helvetica', 24, 'bold'), text_color='#E0FFFF', wraplength=350)
texto.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


botao_cadastro = custk.CTkButton(janela, text='Cadastrar usuário',font=('Helvetica', 14, 'bold'),  fg_color='#1E90FF', command=0)
botao_cadastro.grid(row=1, column=0, columnspan=4,padx=10, pady=10)

botao_listar_usuarios = custk.CTkButton(janela, text='Listar usuários',font=('Helvetica', 14, 'bold'),  fg_color='#1E90FF', command=0)
botao_listar_usuarios.grid(row=2, column=0, columnspan=4,padx=10, pady=10)

botao_cadastro_alimentos = custk.CTkButton(janela, text='Cadastrar alimentos',font=('Helvetica', 14, 'bold'),  fg_color='#1E90FF', command=0)
botao_cadastro_alimentos.grid(row=3, column=0, columnspan=4,padx=10, pady=10)

botao_listar_alimentos = custk.CTkButton(janela, text='Listar alimentos',font=('Helvetica', 14, 'bold'),  fg_color='#1E90FF', command=0)
botao_listar_alimentos.grid(row=4, column=0, columnspan=4,padx=10, pady=10)

janela.mainloop()
