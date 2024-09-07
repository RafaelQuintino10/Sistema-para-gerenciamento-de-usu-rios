import customtkinter as custk
import csv
import os
from tkinter import messagebox as pop_up

# Define o caminho do arquivo CSV
arquivo_dados_usuarios = 'usuarios.csv'
arquivo_dados_alimentos = 'alimentos.csv'


def cadastrar_usuario():
    """Solicita informações do usuário e as salva no arquivo CSV."""
    nome = usuario.get()
    id = idade.get()
    if not nome or not id:
        pop_up.showerror('ERRO!', "DIGITE O NOME E A IDADE CORRETAMENTE!")
        return
    dados = carregar_dados_usuario()
    dados.append({'Nome': nome, 'Idade': id})
    salvar_dados_usuario(dados)
    pop_up.showinfo('SUCESSO', "USUÁRIO CADASTRADO COM SUCESSO!")
    usuario.delete(0, 'end')  # Limpa o campo de entrada
    idade.delete(0, 'end')    # Limpa o campo de entrada
    atualizar_lista_usuarios()  # Atualiza a lista após cadastrar


def salvar_dados_usuario(dados):
    """Salva os dados no arquivo CSV."""
    with open(arquivo_dados_usuarios, mode='w', newline='', encoding='utf-8') as arquivo:
        campo_nomes = ['Nome', 'Idade']
        escritor = csv.DictWriter(arquivo, fieldnames=campo_nomes)
        escritor.writeheader()
        escritor.writerows(dados)

def carregar_dados_usuario():
    """Carrega os dados do arquivo CSV, se existir."""
    if os.path.exists(arquivo_dados_usuarios):
        with open(arquivo_dados_usuarios, mode='r', newline='', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            return list(leitor)
    return []


def cadastrar_alimentos():
    """Solicita informações do usuário e as salva no arquivo CSV."""
    alimen = alimento.get()
    quant = qntd.get()
    if not alimen or not quant:
        pop_up.showerror('ERRO!', "DIGITE O ALIMENTO E A QUANTIDADE CORRETAMENTE!")
        return
    dados = carregar_dados_alimentos()
    dados.append({'Alimento': alimen, 'Quantidade': quant})
    salvar_dados_alimentos(dados)
    pop_up.showinfo('SUCESSO', "ALIMENTO CADASTRADO COM SUCESSO!")
    usuario.delete(0, 'end')  # Limpa o campo de entrada
    idade.delete(0, 'end')    # Limpa o campo de entrada
    atualizar_lista_alimentos()  # Atualiza a lista após cadastrar


def salvar_dados_alimentos(dados):
    """Salva os dados no arquivo CSV."""
    with open(arquivo_dados_alimentos, mode='w', newline='', encoding='utf-8') as arquivo:
        campo_nomes = ['Alimento', 'Quantidade']
        escritor = csv.DictWriter(arquivo, fieldnames=campo_nomes)
        escritor.writeheader()
        escritor.writerows(dados)

def carregar_dados_alimentos():
    """Carrega os dados do arquivo CSV, se existir."""
    if os.path.exists(arquivo_dados_alimentos):
        with open(arquivo_dados_alimentos, mode='r', newline='', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            return list(leitor)
    return []

def calcular_quantidade_total_alimentos():
    dados = carregar_dados_alimentos()
    quantidade_total= 0
    for item in dados:
        quantidade_total += float(item['Quantidade'])
    return quantidade_total

def divisao_alimentos_por_usuarios():
    try:
        quantidade_total = calcular_quantidade_total_alimentos()
        dados_usuarios = carregar_dados_usuario()
        num_usuarios = len(dados_usuarios)
        if num_usuarios == 0:
            pop_up.showerror('ERRO!', 'NÃO HÁ USUÁRIOS CADASTRADOS PARA FAZER A DIVISÃO!')
        
        divisao = quantidade_total / num_usuarios
        resultado = f'CADA USUÁRIO RECEBERÁ {divisao:.2f} UNIDADES DE ALIMENTO!'
        resultado_label.configure(text=resultado)
    except ValueError:
        pop_up.showerror('ERRO!', 'OCORREU UM ERRO AO REALIZAR A DIVISÃO DE ALIMENTOS! TENTE NOVAMENTE!')
    
def mostrar_tela_principal():
    tela_cadastro_usuario.grid_forget()
    tela_listagem_usuarios.grid_forget()
    tela_cadastro_alimentos.grid_forget()
    tela_listagem_alimentos.grid_forget()
    tela_calculo.grid_forget()
    tela_principal.grid(row=0, column=0, sticky='nsew')

def mostrar_tela_cadastro_usuarios():
    tela_principal.grid_forget()
    tela_listagem_usuarios.grid_forget()
    tela_cadastro_usuario.grid(row=0, column=0, sticky="nsew")

def mostrar_listagem_usuarios():
    tela_principal.grid_forget()
    tela_cadastro_usuario.grid_forget()
    tela_listagem_usuarios.grid(row=0, column=0, sticky='nsew')
    atualizar_lista_usuarios()

def mostrar_tela_cadastro_alimentos():
    tela_principal.grid_forget()
    tela_cadastro_usuario.grid_forget()
    tela_listagem_usuarios.grid_forget()
    tela_cadastro_alimentos.grid(row=0, column=0, sticky='nsew')

def mostrar_listagem_alimentos():
    tela_principal.grid_forget()
    tela_cadastro_usuario.grid_forget()
    tela_cadastro_alimentos.grid_forget()
    tela_listagem_usuarios.grid_forget()
    tela_listagem_alimentos.grid(row=0, column=0, sticky='nsew')
    atualizar_lista_alimentos()

def mostrar_tela_calculo():
    tela_principal.grid_forget()
    tela_cadastro_usuario.grid_forget()
    tela_cadastro_alimentos.grid_forget()
    tela_listagem_usuarios.grid_forget()
    tela_listagem_alimentos.grid_forget()
    tela_calculo.grid(row=0, column=0, sticky='nsew')




def criar_tabela_usuarios(frame, dados):
    """Cria uma tabela no frame fornecido com os dados fornecidos, mantendo os cabeçalhos."""
    # Primeiro, destrua todos os widgets, exceto o cabeçalho
    for widget in frame.winfo_children():
        widget.destroy()

    headers = ['Nome', 'Idade']
    # Cria cabeçalhos se ainda não existirem
    if not frame.grid_slaves(row=0):
        for j, header in enumerate(headers):
            label = custk.CTkLabel(frame, text=header, font=('Helvetica', 17, 'bold'), anchor='w', fg_color='black')
            label.grid(row=0, column=j, padx=20, pady=5, columnspan=6, sticky='nsew')

        # Adiciona dados a partir da linha 1 (abaixo dos cabeçalhos)
        start_row = 1
        for i, linha in enumerate(dados):
            for j, valor in enumerate([linha['Nome'], linha['Idade']]):
                label = custk.CTkLabel(frame, text=valor, font=('Helvetica', 15), anchor='w')
                label.grid(row=start_row + i, column=j, padx=25, pady=5, sticky='nsew')

        # Configure a expansão das colunas e linhas
        for j in range(2):  # Duas colunas: Nome e Idade
            frame.grid_columnconfigure(j, weight=1)
        for i in range(start_row, start_row + len(dados)):
            frame.grid_rowconfigure(i, weight=1)


def criar_tabela_alimentos(frame, dados):
    """Cria uma tabela no frame fornecido com os dados fornecidos, mantendo os cabeçalhos."""
    # Primeiro, destrua todos os widgets, exceto o cabeçalho
    for widget in frame.winfo_children():
        widget.destroy()

    headers = ['Alimentos', 'Quantidade']
    # Cria cabeçalhos se ainda não existirem
    if not frame.grid_slaves(row=0):
        for j, header in enumerate(headers):
            label = custk.CTkLabel(frame, text=header, font=('Helvetica', 17, 'bold'), anchor='w', fg_color='black')
            label.grid(row=0, column=j, padx=20, pady=5, columnspan=6, sticky='nsew')

        # Adiciona dados a partir da linha 1 (abaixo dos cabeçalhos)
        start_row = 1
        for i, linha in enumerate(dados):
            for j, valor in enumerate([linha['Alimento'], linha['Quantidade']]):
                label = custk.CTkLabel(frame, text=valor, font=('Helvetica', 15), anchor='w')
                label.grid(row=start_row + i, column=j, padx=25, pady=5, sticky='nsew')

        # Configure a expansão das colunas e linhas
        for j in range(2):  # Duas colunas: Nome e Idade
            frame.grid_columnconfigure(j, weight=1)
        for i in range(start_row, start_row + len(dados)):
            frame.grid_rowconfigure(i, weight=1)


def atualizar_lista_alimentos():
    dados = carregar_dados_alimentos()
    criar_tabela_alimentos(scrollable_frame_alimentos,dados)

def atualizar_lista_usuarios():
    """Atualiza a lista de usuários na tela de listagem."""
    dados = carregar_dados_usuario()
    criar_tabela_usuarios(scrollable_frame_usuarios, dados)

# Inicializa a janela principal
janela = custk.CTk()
janela.geometry('400x400')
janela.title('Trabalho RAD Python')

# Configuração das proporções das linhas e colunas
janela.grid_columnconfigure(0, weight=1)
janela.grid_rowconfigure(0, weight=1)

# Criação dos Frames
tela_principal = custk.CTkFrame(janela)
tela_cadastro_usuario = custk.CTkFrame(janela)
tela_listagem_usuarios = custk.CTkFrame(janela)
tela_cadastro_alimentos = custk.CTkFrame(janela)
tela_listagem_alimentos = custk.CTkFrame(janela)
tela_calculo = custk.CTkFrame(janela)


# Configuração dos Frames
tela_principal.grid(row=0, column=0, sticky="nsew")
tela_cadastro_usuario.grid(row=0, column=0, sticky="nsew")
tela_listagem_usuarios.grid(row=0, column=0, sticky="nsew")
tela_cadastro_alimentos.grid(row=0, column=0, sticky="nsew")
tela_listagem_alimentos.grid(row=0, column=0, sticky="nsew")
tela_calculo.grid(row=0, column=0, sticky="nsew")


# Configuração das proporções dos Frames
tela_principal.grid_columnconfigure(0, weight=1)
tela_principal.grid_columnconfigure(1, weight=1)
tela_principal.grid_columnconfigure(2, weight=1)
tela_principal.grid_rowconfigure(0, weight=1)
tela_principal.grid_rowconfigure(1, weight=0)
tela_principal.grid_rowconfigure(2, weight=0)
tela_principal.grid_rowconfigure(3, weight=0)
tela_principal.grid_rowconfigure(4, weight=0)
tela_principal.grid_rowconfigure(5, weight=1)

tela_cadastro_usuario.grid_columnconfigure(0, weight=1)
tela_cadastro_usuario.grid_columnconfigure(1, weight=1)
tela_cadastro_usuario.grid_columnconfigure(2, weight=1)
tela_cadastro_usuario.grid_rowconfigure(0, weight=1)
tela_cadastro_usuario.grid_rowconfigure(1, weight=0)
tela_cadastro_usuario.grid_rowconfigure(2, weight=0)
tela_cadastro_usuario.grid_rowconfigure(3, weight=0)
tela_cadastro_usuario.grid_rowconfigure(4, weight=0)
tela_cadastro_usuario.grid_rowconfigure(5, weight=1)

tela_cadastro_alimentos.grid_columnconfigure(0, weight=1)
tela_cadastro_alimentos.grid_columnconfigure(1, weight=1)
tela_cadastro_alimentos.grid_columnconfigure(2, weight=1)
tela_cadastro_alimentos.grid_rowconfigure(0, weight=1)
tela_cadastro_alimentos.grid_rowconfigure(1, weight=0)
tela_cadastro_alimentos.grid_rowconfigure(2, weight=0)
tela_cadastro_alimentos.grid_rowconfigure(3, weight=0)
tela_cadastro_alimentos.grid_rowconfigure(4, weight=0)
tela_cadastro_alimentos.grid_rowconfigure(5, weight=1)

tela_listagem_usuarios.grid_columnconfigure(0, weight=1)
tela_listagem_usuarios.grid_columnconfigure(1, weight=1)
tela_listagem_usuarios.grid_columnconfigure(2, weight=1)
tela_listagem_usuarios.grid_rowconfigure(0, weight=0)
tela_listagem_usuarios.grid_rowconfigure(1, weight=1)
tela_listagem_usuarios.grid_rowconfigure(2, weight=0)
tela_listagem_usuarios.grid_rowconfigure(3, weight=0)
tela_listagem_usuarios.grid_rowconfigure(4, weight=1)

tela_listagem_alimentos.grid_columnconfigure(0, weight=1)
tela_listagem_alimentos.grid_columnconfigure(1, weight=1)
tela_listagem_alimentos.grid_columnconfigure(2, weight=1)
tela_listagem_alimentos.grid_rowconfigure(0, weight=0)
tela_listagem_alimentos.grid_rowconfigure(1, weight=1)
tela_listagem_alimentos.grid_rowconfigure(2, weight=0)
tela_listagem_alimentos.grid_rowconfigure(3, weight=0)
tela_listagem_alimentos.grid_rowconfigure(4, weight=1)

tela_calculo.grid_columnconfigure(0, weight=1)
tela_calculo.grid_columnconfigure(1, weight=1)
tela_calculo.grid_columnconfigure(2, weight=1)
tela_calculo.grid_rowconfigure(0, weight=1)
tela_calculo.grid_rowconfigure(1, weight=0)
tela_calculo.grid_rowconfigure(2, weight=0)
tela_calculo.grid_rowconfigure(3, weight=0)
tela_calculo.grid_rowconfigure(4, weight=1)
tela_calculo.grid_rowconfigure(5, weight=1)

# Inicializa a tela_principal
texto = custk.CTkLabel(tela_principal, text='Cadastro de usuários e gerenciamento de alimentos',
                       font=('Helvetica', 24, 'bold'), text_color='#E0FFFF', wraplength=350)
texto.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

botao_cadastro = custk.CTkButton(tela_principal, text='Cadastrar usuário',
                                font=('Helvetica', 14, 'bold'), fg_color='#1E90FF', command=mostrar_tela_cadastro_usuarios)
botao_cadastro.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

botao_listar_usuarios = custk.CTkButton(tela_principal, text='Listar usuários',
                                        font=('Helvetica', 14, 'bold'), fg_color='#1E90FF', command=mostrar_listagem_usuarios)
botao_listar_usuarios.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

botao_cadastro_alimentos = custk.CTkButton(tela_principal, text='Cadastrar alimentos',
                                          font=('Helvetica', 14, 'bold'), fg_color='#1E90FF', command=mostrar_tela_cadastro_alimentos)
botao_cadastro_alimentos.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

botao_listar_alimentos = custk.CTkButton(tela_principal, text='Listar alimentos',
                                        font=('Helvetica', 14, 'bold'), fg_color='#1E90FF', command=mostrar_listagem_alimentos)
botao_listar_alimentos.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

botao_calcular_divisao = custk.CTkButton(tela_principal, text='Calcular divisão', font=('Helvetica', 14, 'bold'),
                        fg_color='#1E90FF', command=mostrar_tela_calculo)
botao_calcular_divisao.grid(row=5, column=0, columnspan=4, padx=10, pady=10)


# Inicializa a tela_cadastro_usuario
texto = custk.CTkLabel(tela_cadastro_usuario, text='Cadastro de usuários',
                       font=('Helvetica', 24, 'bold'), text_color='#E0FFFF', wraplength=350)
texto.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

usuario_label = custk.CTkLabel(tela_cadastro_usuario, text='Usuário:', font=('Helvetica', 14, 'bold'), text_color='#E0FFFF')
usuario_label.grid(row=1, column=0, padx=1, pady=10, sticky='e')

usuario = custk.CTkEntry(tela_cadastro_usuario, placeholder_text='Digite o nome do usuário...')
usuario.grid(row=1, column=1, padx=10, pady=10, sticky='we')

idade_label = custk.CTkLabel(tela_cadastro_usuario, text='Idade:', font=('Helvetica', 14, 'bold'), text_color='#E0FFFF')
idade_label.grid(row=2, column=0, padx=1, pady=10, sticky='e')

idade = custk.CTkEntry(tela_cadastro_usuario, placeholder_text='Digite a idade do usuário...')
idade.grid(row=2, column=1, padx=10, pady=10, sticky='we')

botao = custk.CTkButton(tela_cadastro_usuario, text='Cadastrar usuário', font=('Helvetica', 14, 'bold'),
                        fg_color='#1E90FF', command=cadastrar_usuario)
botao.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

botao_voltar = custk.CTkButton(tela_cadastro_usuario, text='Voltar', font=('Helvetica', 14, 'bold'),
                        fg_color='#1E90FF', command=mostrar_tela_principal)
botao_voltar.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

# Inicializa a tela de listagem de usuários
texto = custk.CTkLabel(tela_listagem_usuarios, text='Lista de Usuários', font=('Helvetica', 24, 'bold'), text_color='#E0FFFF', wraplength=550)
texto.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='we')

botao_voltar = custk.CTkButton(tela_listagem_usuarios, text='Voltar', font=('Helvetica', 14, 'bold'),
                        fg_color='#1E90FF', command=mostrar_tela_principal)
botao_voltar.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

# Criar um frame rolável para a tabela
scrollable_frame_usuarios = custk.CTkScrollableFrame(tela_listagem_usuarios)
scrollable_frame_usuarios.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

# Configurar a expansão do frame rolável
tela_listagem_usuarios.grid_rowconfigure(1, weight=1)
tela_listagem_usuarios.grid_columnconfigure(0, weight=1)
tela_listagem_usuarios.grid_columnconfigure(1, weight=1)
tela_listagem_usuarios.grid_columnconfigure(2, weight=1)

# Inicializa a tela de cadastro de alimentos

texto = custk.CTkLabel(tela_cadastro_alimentos, text='Cadastro de alimentos',
                       font=('Helvetica', 24, 'bold'), text_color='#E0FFFF', wraplength=350)
texto.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

alimentos_label = custk.CTkLabel(tela_cadastro_alimentos, text='Alimento:', font=('Helvetica', 14, 'bold'), text_color='#E0FFFF')
alimentos_label.grid(row=1, column=0, padx=1, pady=10, sticky='e')

alimento = custk.CTkEntry(tela_cadastro_alimentos, placeholder_text='Digite o alimento...')
alimento.grid(row=1, column=1, padx=10, pady=10, sticky='we')

qntd_label = custk.CTkLabel(tela_cadastro_alimentos, text='Quantidade:', font=('Helvetica', 14, 'bold'), text_color='#E0FFFF')
qntd_label.grid(row=2, column=0, padx=1, pady=10, sticky='e')

qntd = custk.CTkEntry(tela_cadastro_alimentos, placeholder_text='Digite a quantidade...')
qntd.grid(row=2, column=1, padx=10, pady=10, sticky='we')

botao = custk.CTkButton(tela_cadastro_alimentos, text='Cadastrar alimento', font=('Helvetica', 14, 'bold'),
                        fg_color='#1E90FF', command=cadastrar_alimentos)
botao.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

botao_voltar = custk.CTkButton(tela_cadastro_alimentos, text='Voltar', font=('Helvetica', 14, 'bold'),
                        fg_color='#1E90FF', command=mostrar_tela_principal)
botao_voltar.grid(row=4, column=0, columnspan=4, padx=10, pady=10)


# Inicializa a tela de listagem de alimentos
texto = custk.CTkLabel(tela_listagem_alimentos, text='Lista de Alimentos', font=('Helvetica', 24, 'bold'), text_color='#E0FFFF', wraplength=550)
texto.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='we')

botao_voltar = custk.CTkButton(tela_listagem_alimentos, text='Voltar', font=('Helvetica', 14, 'bold'),
                        fg_color='#1E90FF', command=mostrar_tela_principal)
botao_voltar.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

# Criar um frame rolável para a tabela
scrollable_frame_alimentos = custk.CTkScrollableFrame(tela_listagem_alimentos)
scrollable_frame_alimentos.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

# Configurar a expansão do frame rolável
tela_listagem_usuarios.grid_rowconfigure(1, weight=1)
tela_listagem_usuarios.grid_columnconfigure(0, weight=1)
tela_listagem_usuarios.grid_columnconfigure(1, weight=1)
tela_listagem_usuarios.grid_columnconfigure(2, weight=1)

# Inicializa a tela de cálculo
texto = custk.CTkLabel(tela_calculo, text='Divisão de alimentos',
                       font=('Helvetica', 24, 'bold'), text_color='#E0FFFF', wraplength=350)
texto.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

botao = custk.CTkButton(tela_calculo, text='Calcular divisão', font=('Helvetica', 14, 'bold'),
                        fg_color='#1E90FF', command=divisao_alimentos_por_usuarios)
botao.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

resultado_label = custk.CTkLabel(tela_calculo, text='', font=('Arial', 15), text_color='#E0FFFF', bg_color='black',wraplength=350)
resultado_label.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

botao_voltar = custk.CTkButton(tela_calculo, text='Voltar', font=('Helvetica', 14, 'bold'),
                        fg_color='#1E90FF', command=mostrar_tela_principal)
botao_voltar.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

tela_cadastro_usuario.grid_forget()  # Inicialmente esconder a tela_cadastro_usuario
tela_listagem_usuarios.grid_forget()  # Inicialmente esconde a tela_listagem_usuarios
tela_cadastro_alimentos.grid_forget()  # Inicialmente esconder a tela_cadastro_alimentos
tela_listagem_alimentos.grid_forget()   # # Inicialmente esconde a tela_listagem_alimentos
tela_calculo.grid_forget() # Inicialmente esconde a tela_calculo



janela.mainloop()
