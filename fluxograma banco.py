import os
import time

# função para limpar a tela
def limpar_tela():
    os.system("cls") #windows 

print ('Banco Do Brasil')
nome = (input('CLIENTE: insira seu nome'))
print('Olá' + nome +', seja bem vindo(a)')
print('SELECIONE UMA OPÇÃO:')
import questionary

# Defina as opções
choices = [
    'Saldo',
    'Extrato (últimos 5 dias)',
    'Empréstimos',
    'Sair',
]

def menu_principal():
    while True:
        # O menu será exibido repetidamente
        answer = questionary.select(
            "Escolha uma opção (use as setas e Enter):",
            choices=choices
        ).ask()

        # Se o usuário apertar Esc ou interromper o programa, answer será None
        if answer is None or answer == 'Sair':
            print('Saindo do sistema... Até logo!')
            break  # Encerra o loop while

        # Processa as outras respostas
        if answer == 'Saldo':
            print('\n--- Seu Saldo: R$ 1.250,00 ---\n')
            
        elif answer == 'Extrato (últimos 5 dias)':
            print('\n--- Gerando Extrato... ---\n')
            # Aqui você poderia colocar a lógica do extrato
            
        elif answer == 'Empréstimos':
            print('\n--- Analisando crédito disponível... ---\n')

        # Dica: Adicione um input vazio para o usuário ler a informação antes do menu voltar
        input("Pressione Enter para voltar ao menu...")

# Executa o programa
if __name__ == "__main__":
    menu_principal()