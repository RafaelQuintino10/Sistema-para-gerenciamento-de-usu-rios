
import customtkinter as custk
from main2 import *
from tkinter import messagebox 

def cadastrar_usuario():
    """Solicita informações do usuário e as salva no arquivo CSV."""
    nome = usuario.get()
    id = idade.get()
    if not nome or not id:
        pop_up.showerror('ERRO!',"DIGITE O NOME E A IDADE CORRETAMENTE!")
        return
    dados = carregar_dados()
    dados.append({'Nome': nome, 'Idade': id})
    salvar_dados(dados)
    if dados:
        pop_up.showinfo('SUCESSO',"USUÁRIO CADASTRADO COM SUCESSO!")

def salvar_dados(dados):
    """Salva os dados no arquivo CSV."""
    with open(arquivo_dados, mode='w', newline='', encoding='utf-8') as arquivo:
        campo_nomes = ['Nome', 'Idade']
        escritor = csv.DictWriter(arquivo, fieldnames=campo_nomes)
        escritor.writeheader()
        escritor.writerows(dados)

def carregar_dados():
    """Carrega os dados do arquivo CSV, se existir."""
    if os.path.exists(arquivo_dados):
        with open(arquivo_dados, mode='r', newline='', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            return list(leitor)
    return []

def listar_usuarios():
    """Lista todos os usuários cadastrados."""
    dados = carregar_dados()
    if dados:
        print("Usuários cadastrados:")
        for usuario in dados:
            print(f"Nome: {usuario['Nome']}, Idade: {usuario['Idade']}")
    else:
        print("Nenhum usuário cadastrado.")



def mostar_tela_principal():
    tela_cadastro_usuario.grid_forget()
    tela_listagem_usuarios.grid_forget()
    tela_principal.grid(row=0, column=0, sticky='nsew')

def mostar_tela_cadastro():
    tela_principal.grid_forget()  # Oculta a tela_principal
    tela_cadastro_usuario.grid(row=0, column=0, sticky="nsew")  # Exibe a tela_cadastro_usuario

def mostrar_listagem_usuarios():
    tela_principal.grid_forget()
    tela_cadastro_usuario.grid_forget()
    tela_listagem_usuarios.grid(row=0, column=0, sticky='nsew')

    dados = carregar_dados()
    criar_tabela(scrollable_frame, dados)

def criar_tabela(frame, dados):
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

# Configuração dos Frames
tela_principal.grid(row=0, column=0, sticky="nsew")
tela_cadastro_usuario.grid(row=0, column=0, sticky="nsew")
tela_listagem_usuarios.grid(row=0, column=0, sticky="nsew")


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
tela_cadastro_usuario.grid_rowconfigure(2, weight=1)
tela_cadastro_usuario.grid_rowconfigure(3, weight=0)
tela_cadastro_usuario.grid_rowconfigure(4, weight=0)
tela_cadastro_usuario.grid_rowconfigure(5, weight=1)

tela_listagem_usuarios.grid_columnconfigure(0, weight=1)
tela_listagem_usuarios.grid_columnconfigure(1, weight=1)
tela_listagem_usuarios.grid_columnconfigure(2, weight=1)
tela_listagem_usuarios.grid_rowconfigure(0, weight=0)
tela_listagem_usuarios.grid_rowconfigure(1, weight=1)
tela_listagem_usuarios.grid_rowconfigure(2, weight=0)
tela_listagem_usuarios.grid_rowconfigure(3, weight=0)
tela_listagem_usuarios.grid_rowconfigure(4, weight=1)

# Inicializa a tela_principal
texto = custk.CTkLabel(tela_principal, text='Cadastro de usuários e gerenciamento de alimentos',
                       font=('Helvetica', 24, 'bold'), text_color='#E0FFFF', wraplength=350)
texto.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

botao_cadastro = custk.CTkButton(tela_principal, text='Cadastrar usuário',
                                font=('Helvetica', 14, 'bold'), fg_color='#1E90FF', command=mostar_tela_cadastro)
botao_cadastro.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

botao_listar_usuarios = custk.CTkButton(tela_principal, text='Listar usuários',
                                        font=('Helvetica', 14, 'bold'), fg_color='#1E90FF', command=mostrar_listagem_usuarios)
botao_listar_usuarios.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

botao_cadastro_alimentos = custk.CTkButton(tela_principal, text='Cadastrar alimentos',
                                          font=('Helvetica', 14, 'bold'), fg_color='#1E90FF', command=None)
botao_cadastro_alimentos.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

botao_listar_alimentos = custk.CTkButton(tela_principal, text='Listar alimentos',
                                        font=('Helvetica', 14, 'bold'), fg_color='#1E90FF', command=None)
botao_listar_alimentos.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

# Inicializa a tela_cadastro_usuario
texto = custk.CTkLabel(tela_cadastro_usuario, text='Cadastro de usuários e gerenciamento de alimentos',
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
                        fg_color='#1E90FF', command=mostar_tela_principal)
botao_voltar.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

# Inicializa a tela de listagem de usuários
# Adicionar o título
texto = custk.CTkLabel(tela_listagem_usuarios, text='Lista de Usuários', font=('Helvetica', 24, 'bold'), text_color='#E0FFFF', wraplength=550)
texto.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='ew')

botao_voltar = custk.CTkButton(tela_listagem_usuarios, text='Voltar', font=('Helvetica', 14, 'bold'),
                        fg_color='#1E90FF', command=mostar_tela_principal)
botao_voltar.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

# Criar um frame rolável para a tabela
scrollable_frame = custk.CTkScrollableFrame(tela_listagem_usuarios)
scrollable_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

# Adicionar a tabela ao frame rolável
criar_tabela(scrollable_frame)

# Configurar a expansão do frame rolável
tela_listagem_usuarios.grid_rowconfigure(1, weight=1)
tela_listagem_usuarios.grid_columnconfigure(0, weight=1)
tela_listagem_usuarios.grid_columnconfigure(1, weight=1)
tela_listagem_usuarios.grid_columnconfigure(2, weight=1)

tela_cadastro_usuario.grid_forget()  # Inicialmente esconder a tela_cadastro_usuario
tela_listagem_usuarios.grid_forget()


janela.mainloop()
