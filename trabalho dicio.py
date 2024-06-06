import pprint
import time

livros = {"Percy Jackson, O Ladrão de Raios": {"Autor": "Rick Riordan", "Ano": "2005", "Disponível": True}, 
              "O Guia do Mochileiro das Galáxias": {"Autor": "Douglas Adams", "Ano": "1979", "Disponível": True},
              "O Pequeno Príncipe": {"Autor": "Antoine de Saint-Exupéry", "Ano": "1943", "Disponível": True}}


def adicionar_livro(titulo, livros):
    if titulo in livros:
        print("")
        print(f"O livro {titulo} já está na biblioteca.")
    else:
        autor = input("Qual o autor do livro?")
        ano = input("Qual o ano do livro?")
        livros[titulo] = {"Autor": autor, "Ano": ano, "Disponível": True}
        print("Livro adicionado com sucesso!")

def buscar_livro(titulo, livros):
    if titulo in livros:
        print("")
        print(f"O livro {titulo} já está na biblioteca.")
    else: 
        print("")
        print(f"Não foi possível encontrar o título {titulo} =(")

def pegar_livro(titulo, livros):
    if titulo in livros:
        livros[titulo]["Disponível:"] = False
        print("Livro pego com sucesso!")
    else: 
        print("Livro não encontrado ou não consta na biblioteca, verifique a ortografia! =)")

def devolver_livro(titulo, livros):
    if titulo in livros:
        livros[titulo]["Disponível:"] = True
        print("Livro devolvido com sucesso!")
    else: 
        print("Livro não encontrado ou já consta na biblioteca, verifique a ortografia! =)")


while True: 
    print("")
    print("Biblioteca")
    print("1. Adicionar livro")
    print("2. Buscar livro.")
    print("3. Pegar livro")
    print("4. Devolver livro")
    print("5. Biblioteca completa.")
    print("0. Fechar biblioteca.")
    print("")
    choice = input("Escolha uma opção: ")
    
    if choice == "1":
        print("")
        titulo = input("Qual livro você gostaria de guardar?")
        adicionar_livro(titulo, livros)


    elif choice == "2":
        titulo = input("Qual livro você quer procurar?")
        buscar_livro(titulo, livros)

    elif choice == "3":
        titulo = input("Qual livro você gostaria de pegar?")
        pegar_livro(titulo, livros)

    elif choice == "4":
        titulo = input("Qual o livro você gostaria de devolver?")
        devolver_livro(titulo, livros)

    elif choice == "5":
        print(f"A biblioteca tem os seguintes livros: ")
        pprint.pp(livros)

    elif choice == "0":
        break