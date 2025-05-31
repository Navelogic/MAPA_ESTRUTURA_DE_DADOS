'''

1 - Ao retirar a senha sempre é atribuída a senha 1 para todos os clientes. - FEITO
2 - Não estão sendo atribuídas novas senhas a lista. - FEITO
3 - Ao chamar uma senha, a fila não é alterada. - FEITO
4 - Ao pedir para ver a fila completa, esta não aparece. - FEITO

'''


from collections import deque

fila = deque()
contador_senha = 0

def menu():
    print("\n--- Sistema de Controle de Fila - Açougue Bom Preço ---")
    print("1 - Retirar Senha")
    print("2 - Chamar Próxima Senha")
    print("3 - Mostrar Fila Atual")
    print("4 - Sair")
    return input("Escolha uma opção:")


while True:
    opcao = menu()
    if opcao == '1':
        contador_senha +=1
        fila.append(contador_senha)
        print(f"\nSenha {contador_senha} retirada com sucesso!")
    elif opcao == '2':
        if fila:
            senha_chamada = fila.popleft()
            print(f"\nAtenção! Senha chamada: {senha_chamada}")
        else:
            print("Fila vazia. Nenhuma senha para chamar.")
    elif opcao == '3':
        if fila:
            print("Fila atual de senhas:")
            print(''.join(str(list(fila))))
        else:
            print("Fila vazia.")
    elif opcao == '4':
        print("Sistema encerrado. Obrigado por utilizar!")
        break
    else:
        print("Opção inválida. Tente novamente.")