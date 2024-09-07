# import customtkinter as custk


# janela = custk.CTk()
# janela.geometry('400x400')
# janela.title('Trabalho RAD Python')
# # Configuraraçãp das proporções das linhas e colunas
# janela.grid_columnconfigure(0, weight=1)  # A coluna 0 deve se expandir
# janela.grid_columnconfigure(1, weight=1)  # A coluna 1 deve se expandir
# janela.grid_columnconfigure(2, weight=1)  # A coluna 2 deve se expandir
# janela.grid_rowconfigure(0, weight=1)     # A linha 0 deve se expandir
# janela.grid_rowconfigure(1, weight=0)     # A linha 1 não deve se expandir
# janela.grid_rowconfigure(2, weight=0)     # A linha 2 não deve se expandir
# janela.grid_rowconfigure(3, weight=1)     # A linha 3 deve se expandir
# janela.grid_rowconfigure(4, weight=1)     # A linha 4 deve se expandir

# texto = custk.CTkLabel(janela, text='Lista de Usuários',font=('Helvetica', 24, 'bold'), text_color='#E0FFFF', wraplength=350)
# texto.grid(row=0, column=0, columnspan=3, padx=10, pady=10)




# janela.mainloop()
# import tkinter as tk
# from tkinter import ttk
# import customtkinter as custk

# # Função para configurar a aparência do Treeview
# def estilizar_treeview(treeview):
#     treeview.tag_configure('headings', background='#B0C4DE', font=('Helvetica', 12, 'bold'))
#     treeview.heading('#0', text='', anchor='w')
#     treeview.heading('#1', text='ID', anchor='w')
#     treeview.heading('#2', text='Nome', anchor='w')
#     treeview.heading('#3', text='Email', anchor='w')
#     treeview.column('#0', width=0, stretch=tk.NO)
#     treeview.column('#1', width=100, anchor='w')
#     treeview.column('#2', width=200, anchor='w')
#     treeview.column('#3', width=300, anchor='w')

# # Criar a janela principal
# janela = custk.CTk()
# janela.geometry('600x400')
# janela.title('Trabalho RAD Python')

# # Configuração das proporções das linhas e colunas
# janela.grid_columnconfigure(0, weight=1)  # A coluna 0 deve se expandir
# janela.grid_columnconfigure(1, weight=1)  # A coluna 1 deve se expandir
# janela.grid_columnconfigure(2, weight=1)  # A coluna 2 deve se expandir
# janela.grid_rowconfigure(0, weight=1)     # A linha 0 deve se expandir
# janela.grid_rowconfigure(1, weight=1)     # A linha 1 deve se expandir

# # Título
# texto = custk.CTkLabel(janela, text='Lista de Usuários', font=('Helvetica', 24, 'bold'), text_color='#E0FFFF', wraplength=350)
# texto.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# # Criar um Frame para a tabela
# frame_tabela = custk.CTkFrame(janela)
# frame_tabela.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

# # Adicionar Treeview ao Frame
# treeview = ttk.Treeview(frame_tabela, columns=('ID', 'Nome', 'Email'), show='headings')
# treeview.pack(fill=tk.BOTH, expand=True)

# # Estilizar Treeview
# estilizar_treeview(treeview)

# # Dados para a tabela
# dados = [
#     (1, 'João Silva', 'joao.silva@email.com'),
#     (2, 'Maria Oliveira', 'maria.oliveira@email.com'),
#     (3, 'Carlos Souza', 'carlos.souza@email.com')
# ]

# # Adicionar dados ao Treeview
# for dado in dados:
#     treeview.insert('', tk.END, values=dado)

# janela.mainloop()

# import customtkinter as custk

# # Função para criar a tabela
# def criar_tabela(frame):
#     # Exemplo de dados para a tabela
#     dados = [
#         ["Nome", "Idade", "Cidade"],
#         ["Ana", "28", "São Paulo"],
#         ["Carlos", "35", "Rio de Janeiro"],
#         ["Maria", "42", "Belo Horizonte"],
#         ["João", "31", "Salvador"],
#         ["Lucas", "22", "Curitiba"],
#         ["Juliana", "29", "Fortaleza"],
#     ]

#     for i, linha in enumerate(dados):
#         for j, valor in enumerate(linha):
#             label = custk.CTkLabel(frame, text=valor, font=('Helvetica', 12))
#             label.grid(row=i, column=j, padx=5, pady=5)

# # Criar a janela principal
# janela = custk.CTk()
# janela.geometry('600x400')
# janela.title('Trabalho RAD Python')

# # Configurar as proporções das linhas e colunas
# janela.grid_columnconfigure(0, weight=1)
# janela.grid_columnconfigure(1, weight=1)
# janela.grid_columnconfigure(2, weight=1)
# janela.grid_rowconfigure(0, weight=1)
# janela.grid_rowconfigure(1, weight=0)
# janela.grid_rowconfigure(2, weight=0)
# janela.grid_rowconfigure(3, weight=1)
# janela.grid_rowconfigure(4, weight=1)

# # Adicionar o título
# texto = custk.CTkLabel(janela, text='Lista de Usuários', font=('Helvetica', 24, 'bold'), text_color='#E0FFFF', wraplength=550)
# texto.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# # Criar um frame rolável para a tabela
# scrollable_frame = custk.CTkScrollableFrame(janela)
# scrollable_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

# # Adicionar a tabela ao frame rolável
# criar_tabela(scrollable_frame)

# # Configurar a expansão do frame rolável
# janela.grid_rowconfigure(1, weight=1)
# janela.grid_columnconfigure(0, weight=1)

# # Iniciar o loop da interface
# janela.mainloop()

import customtkinter as custk

# Função para criar a tabela
def criar_tabela(frame):
    # Exemplo de dados para a tabela
    dados = [
        ["Nome", "Idade", "Cidade"],
        ["Ana", "28", "São Paulo"],
        ["Carlos", "35", "Rio de Janeiro"],
        ["Maria", "42", "Belo Horizonte"],
        ["João", "31", "Salvador"],
        ["Lucas", "22", "Curitiba"],
        ["Juliana", "29", "Fortaleza"],
    ]
    

    for i, linha in enumerate(dados):
        for j, valor in enumerate(linha):
            label = custk.CTkLabel(frame, text=valor, font=('Helvetica', 12), anchor='w')
            label.grid(row=i, column=j, padx=5, pady=5, sticky='nsew')

    # Configure a expansão das colunas e linhas
    for j in range(len(dados[0])):
        frame.grid_columnconfigure(j, weight=1)
    for i in range(len(dados)):
        frame.grid_rowconfigure(i, weight=1)

# Criar a janela principal
janela = custk.CTk()
janela.geometry('600x400')
janela.title('Trabalho RAD Python')

# Configurar as proporções das linhas e colunas da janela
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)
janela.grid_rowconfigure(0, weight=0)
janela.grid_rowconfigure(1, weight=1)
janela.grid_rowconfigure(2, weight=0)
janela.grid_rowconfigure(3, weight=0)
janela.grid_rowconfigure(4, weight=1)

# Adicionar o título
texto = custk.CTkLabel(janela, text='Lista de Usuários', font=('Helvetica', 24, 'bold'), text_color='#E0FFFF', wraplength=550)
texto.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='ew')

# Criar um frame rolável para a tabela
scrollable_frame = custk.CTkScrollableFrame(janela)
scrollable_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

# Adicionar a tabela ao frame rolável
criar_tabela(scrollable_frame)

# Configurar a expansão do frame rolável
janela.grid_rowconfigure(1, weight=1)
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)

# Iniciar o loop da interface
janela.mainloop()
