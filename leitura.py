# CRUD
BANCO_DE_DADOS = "usuarios.txt" # Arquivo de dados com as entradas dos usuários

def criar_usuario(): # Função para criar um novo usuário e salvar no banco de dados
    print("\n=== Menu do Cadastro de Usuário ===")
    nome = input("Nome: ")
    idade = input("Idade: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    with open(BANCO_DE_DADOS, "a", encoding="utf-8") as arq:
        arq.write(f"{nome},{idade},{cidade},{estado}\n")
    print("Usuário cadastrado com sucesso!")
    return nome, int(idade), cidade, estado

def estimar_livros_futuros(livros_digitais, livros_fisicos):
    total_atual = livros_digitais + livros_fisicos
    total_5_anos = total_atual * 5
    print(f"\nEstimativa: Se você continuar nesse ritmo, lerá aproximadamente {total_5_anos} livros nos próximos 5 anos.") 
    
    if total_atual >= 20:
        print("Incrível! Você é um leitor assíduo!")
    elif total_atual >= 10:
        print("Muito bom! Sua média de leitura está acima da média nacional.")
    elif total_atual >= 5:
        print("Legal! Mas você pode aumentar esse ritmo com pequenas mudanças.")
    else:
        print("Vamos lá! Que tal estabelecer uma meta de leitura esse ano?")

def media_livros_por_mes(livros_digitais, livros_fisicos): # Função para calcular a média de livros lidos por mês
    total = livros_digitais + livros_fisicos
    media = total / 12
    print(f"\nMédia mensal de leitura: Aproximadamente {media:.2f} livros por mês.")

def habitos_leitura(nome, idade, cidade, estado): # Função para analisar hábitos de leitura
    print("\n=== Análise de Hábitos de Leitura ===")
    livros_digitais = int(input("Quantos livros digitais você leu no último ano? "))
    livros_fisicos = int(input("Quantos livros físicos você leu no último ano? "))
    preferencia = input("Prefere leitura digital ou física? ").strip().lower()
    horas_estudo = float(input("Horas semanais de leitura para estudo: "))
    horas_entretenimento = float(input("Horas semanais de leitura por entretenimento: "))
    genero = input("Gênero literário favorito: ")

    print(f"\nOlá, {nome} de {idade} anos de {cidade}, {estado}.")
    print(f"Você gosta de {genero} e prefere leitura {preferencia}.")

    estimar_livros_futuros(livros_digitais, livros_fisicos) 
    print(f"\nHoras de estudo por ano: {horas_estudo * 52:.2f} h")
    print(f"Horas de entretenimento por ano: {horas_entretenimento * 52:.2f} h")
    media_livros_por_mes(livros_digitais, livros_fisicos)

    if horas_estudo > horas_entretenimento: # Análise de horas de estudo vs entretenimento
        print("Você estuda mais do que se diverte com leitura. Parabéns pelo foco!")
    elif horas_estudo < horas_entretenimento:
        print("Você lê mais por diversão. Um leitor apaixonado!")
    else:
        print("Equilíbrio perfeito entre estudo e prazer. Continue assim!")

# Início do programa
print("\n==== Sistema de Leitura com Cadastro ====") 

while True:
    print("\n1 - Cadastrar novo usuário e iniciar análise de leitura")
    print("2 - Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome, idade, cidade, estado = criar_usuario()
        habitos_leitura(nome, idade, cidade, estado)
    elif escolha == "2":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
