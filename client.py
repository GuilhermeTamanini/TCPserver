from socket import *

destination = ('localhost', 12000)

while True:
    print("-------------------------")
    print("Menu de controle de produto")
    print("-------------------------")
    print("1 - Cadastro")
    print("2 - Deletar")
    print("3 - Atualizar")
    print("4 - Visualizar um")
    print("5 - Visualizar todos")
    print("0 - Sair")
    op = input("Opção: ")

    if op == "0":
        print("Encerrando cliente...")
        break

    try:
        if op == "1":
            name = input("Nome: ")
            desc = input("Descrição: ")
            price = input("Preço: ")
            msg = f"1//{name}//{desc}//{price}"

        if op == "2":
            code = input("Código: ")
            msg = f"2//{code}"

        if op == "3":
            code = input("Código: ")
            name = input("Nome: ")
            desc = input("Descrição: ")
            price = input("Preço: ")
            msg = f"3//{code}//{name}//{desc}//{price}"

        if op == "4":
            code = input("Código: ")
            msg = f"4//{code}"

        if op == "5":
            msg = "5"

        if "5" < op < "0":
            print("Opção inválida!")
            continue

        with socket(AF_INET, SOCK_STREAM) as socCli:
            socCli.connect(destination)
            socCli.send(msg.encode())

            resp = socCli.recv(1024).decode()
            print("Resposta do servidor:", resp)

    except Exception as e:
        print(f"Erro ao comunicar com o servidor: {e}")
