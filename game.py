from models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)

# ---------------------------- Método para execução do jogo: ----------------------------
def jogar(pontos: int) -> None:
    print()

    """
    Try e Except feito para caso o usuario entrei com um valor sem ser int.
    """
    try:
        dificuldade: int = int(input('Informe o nível de dificuldade desejado (1, 2, 3 ou 4): '))
        calc: Calcular = Calcular(dificuldade)
    except:
        print('Valor incorreto. Tente um numero inteiro.\n')
        jogar(pontos)


    print('Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao() # Mostra a operação que o usuario terá q responder.

    resultado: float = float(input()) # Busca o resultado da equação para verificação a seguir:

    if calc.checar_resultado(resultado): # Verifica o resultado se estiver igual a resposta acrescenta o ponto conforme a dificuldade
        pontos += dificuldade
        print(f'Você tem {pontos} pts.')


    # Opção para continuar jogando ou não:
    continuar: int = 1

    while continuar == 1:
        try:
            continuar: int = int(input('\n\nDeseja continuar [1 - Sim ou 0 - Sair]: '))
            print('\n')
        except:
            print(f'Opção invalida, tente novamente.\n\n')
            jogar(pontos)

        if continuar == 1:
            jogar(pontos)

        elif continuar == 0:
            print(f'Você finalizou o jogo com {pontos} pts.')
            print('Até a próxima!')
            exit(-1)


if __name__ == '__main__':
    main()
