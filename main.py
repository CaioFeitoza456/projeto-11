import json
from os import listdir

CAMINHO_PRODUTOS = "produtos.json"

class Estoque:
    arquivos_pasta = listdir()


    def __init__(self):
        if not CAMINHO_PRODUTOS in Estoque.arquivos_pasta:
            with open(CAMINHO_PRODUTOS, "x") as arquivo:
                json.dump([], arquivo)

    def subir_produtos(self, lista_de_produtos):
        with open(CAMINHO_PRODUTOS, "w", encoding="utf8") as arquivo:
            json.dump(lista_de_produtos, arquivo, indent=2)

    def carregar_produtos(self):
        with open(CAMINHO_PRODUTOS, "r", encoding="utf8") as arquivo:
            produtos = json.load(arquivo)
        return produtos


armazem = Estoque()
produtos_a_subir = []

while True:
    print(">>>OPÇÕES<<<")
    print()
    print("[0] Encerrar o programa")
    print("[1] Adicionar produto")
    print("[2] Salvar produtos")
    print("[3] Carregar produtos")
    print()

    opcao = input("Digite aqui: ")

    if opcao == "0":
        # FECHAR PROGRAMA
        print("Fechando programa...")
        break

    elif opcao == "1":
        # ADICIONAR PRODUTO
        produto = {"nome": "", "id": ""}

        nome_produto = input("Nome produto: ").strip().capitalize()
        id_produto = input("Id produto: ").strip()

        produto["nome"] = nome_produto
        produto["id"] = id_produto
    
        produtos_a_subir.append(produto)

    elif opcao == "2":
        # SALVAR PRODUTOS
        if not len(produtos_a_subir) == 0:
            armazem.subir_produtos(produtos_a_subir)
            produtos_a_subir.clear()
            print("Produtos salvos com sucesso!")
            continue
        
        print("Não há nenhum produto para salvar.")

    elif opcao == "3":
        # CARREGAR PRODUTOS
        produtos_armazem = armazem.carregar_produtos()
        
        if not len(produtos_armazem) == 0:
            print()
            for produto in produtos_armazem:
                print(f"Nome: {produto["nome"]}")
                print(f"Id: {produto["id"]}")
                print("~" * 30)
            print()
            continue

        print("Não há nada para carregar, adicione algo primeiro.")

    else:
        # SE ALGO DIFERENTE DE "0, 1, 2, 3" FOR DIGITADO
        print("Digite uma opção válida.")
