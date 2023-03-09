import csv

# define o nome do arquivo CSV onde os dados serão armazenados
FILE_NAME = "catalogo_equipamentos.csv"

def cadastrar_equipamento():
    # solicita ao usuário as informações do equipamento
    nome = input("Digite o nome do equipamento: ")
    tipo = input("Digite o tipo do equipamento: ")
    marca = input("Digite a marca do equipamento: ")
    modelo = input("Digite o modelo do equipamento: ")
    numero_serie = input("Digite o número de série do equipamento: ")
    descricao = input("Digite uma breve descrição do equipamento: ")

    # abre o arquivo CSV em modo de escrita
    with open(FILE_NAME, mode='a', newline='') as csv_file:
        # cria um objeto para escrever os dados no arquivo CSV
        writer = csv.writer(csv_file)

        # escreve as informações do equipamento no arquivo CSV
        writer.writerow([nome, tipo, marca, modelo, numero_serie, descricao])

    print("Equipamento cadastrado com sucesso!")

def listar_equipamentos():
    # abre o arquivo CSV em modo de leitura
    with open(FILE_NAME, mode='r') as csv_file:
        # cria um objeto para ler os dados do arquivo CSV
        reader = csv.reader(csv_file)

        # percorre as linhas do arquivo CSV e imprime as informações dos equipamentos
        for row in reader:
            print(f"Nome: {row[0]}, Tipo: {row[1]}, Marca: {row[2]}, Modelo: {row[3]}, Número de Série: {row[4]}, Descrição: {row[5]}")

# menu principal do programa
while True:
    print("Selecione uma opção:")
    print("1 - Cadastrar equipamento")
    print("2 - Listar equipamentos")
    print("3 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        cadastrar_equipamento()
    elif opcao == "2":
        listar_equipamentos()
    elif opcao == "3":
        break
    else:
        print("Opção inválida. Tente novamente.")
