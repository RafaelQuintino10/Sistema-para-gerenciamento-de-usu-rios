import csv
import os
import tkinter.messagebox as pop_up
# Define o caminho do arquivo onde os dados serão armazenados
arquivo_dados = "usuarios.csv"

def carregar_dados():
    """Carrega os dados do arquivo CSV, se existir."""
    if os.path.exists(arquivo_dados):
        with open(arquivo_dados, mode='r', newline='', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            return list(leitor)
    return []

def salvar_dados(dados):
    """Salva os dados no arquivo CSV."""
    with open(arquivo_dados, mode='w', newline='', encoding='utf-8') as arquivo:
        campo_nomes = ['Nome', 'Idade']
        escritor = csv.DictWriter(arquivo, fieldnames=campo_nomes)
        escritor.writeheader()
        escritor.writerows(dados)

def cadastrar_usuario():
    """Solicita informações do usuário e as salva no arquivo CSV."""
    nome = input("Digite o nome do usuário: ")
    id = input("Digite o e-mail do usuário: ")
    
    dados = carregar_dados()
    dados.append({'Nome': nome, 'Idade': id})
    salvar_dados(dados)
    if dados:
        pop_up.showinfo('Usuário castrado com sucesso!')

def listar_usuarios():
    """Lista todos os usuários cadastrados."""
    dados = carregar_dados()
    if dados:
        print("Usuários cadastrados:")
        for usuario in dados:
            print(f"Nome: {usuario['Nome']}, Idade: {usuario['Idade']}")
    else:
        print("Nenhum usuário cadastrado.")

def menu():
    """Exibe o menu principal e processa a escolha do usuário."""
    while True:
        print("\nMenu:")
        print("1. Cadastrar usuário")
        print("2. Listar usuários")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            cadastrar_usuario()
        elif escolha == '2':
            listar_usuarios()
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
