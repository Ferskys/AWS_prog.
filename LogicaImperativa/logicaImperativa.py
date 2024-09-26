def coletar_dados_pessoais():
    # Solicitar dados ao usuário
    nome = input("Informe seu nome: ")
    endereco = input("Informe seu endereço: ")
    cidade = input("Informe sua cidade: ")
    cpf = input("Informe seu CPF: ")
    rg = input("Informe seu RG: ")

    # Exibir os dados informados
    print("\nDados Pessoais:")
    print(f"Nome: {nome}")
    print(f"Endereço: {endereco}")
    print(f"Cidade: {cidade}")
    print(f"CPF: {cpf}")
    print(f"RG: {rg}")

# Executar a função
coletar_dados_pessoais()