"""Algortitimo com a classe e as funções de execução para o game"""

# ------------------------- Bibliotecas Utilizadas: -------------------------
from random import randint
import math


# ------------------------- Implementação da Classe: ------------------------
class Calcular:

    def __init__(self: object, dificuldade: int, /) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self._gerar_valor  # Variavel 1 que irá gerar um valor randomico.
        self.__valor2: int = self._gerar_valor  # Variavel 1 que irá gerar um valor randomico.
        self.__operacao: int = randint(1, 6)  # Valor Randomico sendo: 1 - Somar, 2 - subtrair, 3 - multiplicar,
                                              # 4 - Dividir, 5 - Potencializar e 6 - Raiz Quadrada.
        self.__resultado: float = self._gerar_resultado

    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade

    @property
    def valor1(self: object) -> int:
        return self.__valor1

    @property
    def valor2(self: object) -> int:
        return self.__valor2

    @property
    def operacao(self: object) -> int:
        return self.__operacao

    @property
    def resultado(self: object) -> float:
        return self.__resultado

    # ------------------------- Metodo utilizado com o Nome da Operação: -------------------------
    def __str__(self: object) -> str:
        op: str = ''
        if self.operacao == 1:
            op = 'Somar'
            return op
        elif self.operacao == 2:
            op = 'Subtrair'
            return op
        elif self.operacao == 3:
            op = 'Multiplicar'
            return op
        elif self.operacao == 4:
            op = 'Dividir'
        elif self.operacao == 5:
            op = 'Potencia'
        elif self.operacao == 6:
            op = 'Raiz quadrada'
        else:
            op = 'Operação Desconhecida'
        return f' Valor 1: {self.valor1}\n Valor 2: {self.valor2}\n Dificuldade: {self.dificuldade}\n Operação: {op}'

    # ------------------------- Método que gera valor aleatorio conforme a dificuldade escolida para as variaveis: 
    # (__valor1 e __valor2). 
    @property
    def _gerar_valor(self: object) -> int:
        if self.dificuldade == 1:
            return randint(0, 10)
        elif self.dificuldade == 2:
            return randint(11, 100)
        elif self.dificuldade == 3:
            return randint(101, 1000)
        elif self.dificuldade == 4:
            return randint(1001, 10000)
        else:
            return randint(10001, 100000)

    # ------------------------- Calculo de Resultados do algoritmo: -------------------------
    @property
    def _gerar_resultado(self: object) -> float:
        if self.operacao == 1:  # Somar
            resultado: float = self.valor1 + self.valor2
            return float(resultado)
        elif self.operacao == 2:  # Subtração
            resultado: float = self.valor1 - self.valor2
            return float(resultado)
        elif self.operacao == 3:  # Multiplicar
            resultado: float = self.valor1 * self.valor2
            return float(resultado)
        elif self.operacao == 4:  # Dividir
            val2 = self.valor2 + 1
            resultadoDiv: float = self.valor1 / val2
            resultado: float = f"{resultadoDiv:.2f}"
            return float(resultado)
        elif self.operacao == 5:  # Potencializar
            resultado: float = self.valor1 ** self.valor2
            return float(resultado)
        elif self.operacao == 6:  # Raiz Quardada
            resultadoRaiz: float = (math.sqrt(self.valor1))
            resultado: float = f"{resultadoRaiz:.2f}"
            return float(resultado)

    # ------------- Metodo que retorna o sinal da equação , para visualização da equação e resultado -----------------
    @property
    def _op_simbolo(self: object) -> str:
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        elif self.operacao == 3:
            return '*'
        elif self.operacao == 4:
            return '/'
        elif self.operacao == 5:
            return '^'
        elif self.operacao == 6:
            return '√'

    # ------------------------- Verifica se a reposta é igual ao resultado Certo/Errado -------------------------
    def checar_resultado(self: object, resposta: float) -> bool:
        certo: bool = False

        if self.resultado == resposta:
            print('Resposta Correta!')
            certo = True
            return certo

        else:
            print('Resposta Errada!')
            print(f'A resposta correta é = {self.resultado}.')
            return certo

    # ------------------------- Mostra o resultado feito pela maquina: -------------------------
    def mostrar_operacao(self: object) -> None:
        if self.operacao == 6: # Raiz quadrada.
            print(f'Qual a raiz quadrada de {self.valor1} = ?')
        elif self.operacao == 4: # Divisão
            if self.valor2 == 0: # Ajustando o valor de self.valor2 caso seja 0:
                self.valor2 = 1
                print(f'{self.valor1} {self._op_simbolo} {self.valor2} = ?')
            print(f'{self.valor1} {self._op_simbolo} {self.valor2} = ?')
        else:
            print(f'{self.valor1} {self._op_simbolo} {self.valor2} = ?')
