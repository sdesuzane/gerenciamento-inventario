# Arquivo: gerenciamento_inventario.py

# Variável global para armazenar o estoque de produtos
estoque = {}

# Função para cadastrar produtos no sistema
def cadastrar_produtos():
    print("Acessando funcionalidade de cadastro de produtos...")
    # Aqui você pode adicionar o código para cadastrar produtos
    nome_produto = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade inicial: "))
    estoque[nome_produto] = quantidade
    print(f"{quantidade} unidades de {nome_produto} cadastradas com sucesso!")

# Função para realizar uma venda de produtos
def realizar_venda():
    print("Acessando funcionalidade de venda...")
    # Aqui você pode adicionar o código para realizar uma venda
    produto = input("Digite o nome do produto a ser vendido: ")
    if produto in estoque:
        quantidade_vendida = int(input(f"Digite a quantidade de {produto} a ser vendida: "))
        if quantidade_vendida <= estoque[produto]:
            estoque[produto] -= quantidade_vendida
            print(f"{quantidade_vendida} unidades de {produto} vendidas com sucesso!")
        else:
            print("Quantidade insuficiente em estoque.")
    else:
        print("Produto não encontrado no estoque.")

# Função para realizar uma encomenda de produtos
def realizar_encomenda():
    print("Acessando funcionalidade de encomenda...")
    # Aqui você pode adicionar o código para realizar uma encomenda
    produto = input("Digite o nome do produto a ser encomendado: ")
    quantidade_encomendada = int(input(f"Digite a quantidade de {produto} a ser encomendada: "))
    if produto in estoque:
        estoque[produto] += quantidade_encomendada
    else:
        estoque[produto] = quantidade_encomendada
    print(f"{quantidade_encomendada} unidades de {produto} encomendadas com sucesso!")

# Função para exibir o estoque atual de produtos
def exibir_estoque():
    print("Acessando funcionalidade de exibição de estoque...")
    print("Estoque atual:")
    for produto, quantidade in estoque.items():
        print(f"{produto}: {quantidade} unidades")

# Função para iniciar sessão no sistema
def iniciar_sessao():
    print("Iniciando sessão...")
    # Aqui você pode adicionar o código para iniciar a sessão
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    # Lógica para verificar o usuário e senha e permitir o acesso ao sistema

# Função para atualizar o estoque de produtos no sistema
def atualizar_estoque():
    print("Acessando funcionalidade de atualização de estoque...")
    # Aqui você pode adicionar o código para atualizar o estoque
    nome_produto = input("Digite o nome do produto a ser atualizado: ")
    quantidade = int(input("Digite a quantidade a ser adicionada/subtraída: "))
    # Lógica para atualizar o estoque do produto no banco de dados

# Função para monitorar a validade dos produtos no sistema
# Função para monitorar a validade dos produtos no sistema
def monitorar_validade():
    print("Acessando funcionalidade de monitoramento de validade...")
    # Aqui você pode adicionar o código para monitorar a validade dos produtos
    # Exemplo: verificar a data de validade dos produtos no banco de dados e gerar alertas se necessário
    produtos = {
        "Arroz": {"validade": "10/10/2024", "quantidade": 100},
        "Feijão": {"validade": "15/10/2024", "quantidade": 50},
        "Óleo": {"validade": "30/09/2024", "quantidade": 20}
    }
    for produto, info in produtos.items():
        if info["quantidade"] < 10:
            print(f"Atenção! A quantidade de {produto} está baixa. Verifique o estoque!")
        if info["validade"] == "10/10/2024":
            print(f"Atenção! O produto {produto} está próximo da data de validade.")

# Função para gerar relatórios do estoque no sistema
def gerar_relatorios():
    print("Acessando funcionalidade de geração de relatórios...")
    # Aqui você pode adicionar o código para gerar relatórios
    # Exemplo: consultar o banco de dados para obter informações sobre o estoque e criar um relatório em formato PDF ou Excel
    relatorio = {
        "Arroz": 100,
        "Feijão": 50,
        "Óleo": 20
    }
    print("Relatório de Estoque:")
    for produto, quantidade in relatorio.items():
        print(f"{produto}: {quantidade} unidades")

# Função para fornecer informações sobre o treinamento dos colaboradores
def treinamento_colaboradores():
    print("Acessando informações sobre o treinamento dos colaboradores...")
    # Aqui você pode adicionar o código para fornecer informações sobre o treinamento
    # Exemplo: listar os materiais de treinamento disponíveis e as datas das próximas sessões de treinamento
    materiais = ["Manual do Sistema", "Vídeo Tutorial"]
    datas_treinamento = ["10/10/2024", "15/10/2024"]
    print("Materiais de Treinamento Disponíveis:")
    for material in materiais:
        print(material)
    print("\nDatas das Próximas Sessões de Treinamento:")
    for data in datas_treinamento:
        print(data)

# Função para fornecer suporte adicional aos usuários
def obter_suporte():
    print("Acessando informações de suporte...")
    # Aqui você pode adicionar o código para fornecer suporte
    # Exemplo: fornecer informações de contato para o suporte técnico e instruções para abrir um chamado de suporte
    print("Para obter suporte técnico, entre em contato conosco pelo telefone (32) 12345-6789 ou envie um email para system.gerenciamento_inventario@gmail.com")
    print("Se preferir, você pode abrir um chamado de suporte diretamente pelo sistema, na seção 'Suporte'.")

def main():
    print("Bem-vindo ao Sistema de Gerenciamento de Inventário!")
    # Aqui você pode criar um menu simples para o usuário escolher as opções
    while True:
        print("\nOpções:")
        print("1. Iniciar Sessão")
        print("2. Cadastrar Produtos")
        print("3. Realizar Venda")
        print("4. Realizar Encomenda")
        print("5. Exibir Estoque")
        print("6. Atualizar Estoque")
        print("7. Monitorar Validade")
        print("8. Gerar Relatórios")
        print("9. Treinamento dos Colaboradores")
        print("10. Obter Suporte")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            iniciar_sessao()
        elif opcao == "2":
            cadastrar_produtos()
        elif opcao == "3":
            realizar_venda()
        elif opcao == "4":
            realizar_encomenda()
        elif opcao == "5":
            exibir_estoque()
        elif opcao == "6":
            atualizar_estoque()
        elif opcao == "7":
            monitorar_validade()
        elif opcao == "8":
            gerar_relatorios()
        elif opcao == "9":
            treinamento_colaboradores()
        elif opcao == "10":
            obter_suporte()
        elif opcao == "0":
            print("Saindo do Sistema de Gerenciamento de Inventário. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()




