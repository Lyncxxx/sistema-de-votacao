from random import randint
from time import sleep


class Candidato:
    def __init__(self, nome, partido, numero):
        self.nome = nome
        self.partido = partido
        self.numero = numero
        self.votos_recebidos = 0


    def __str__(self):
        return f'''Nome: {self.nome} 
N°{self.numero} 
Partido: {self.partido}
Votos recebidos: {self.votos_recebidos}
'''

    def adicionar_voto(self):
        self.votos_recebidos += 1


class Eleitor:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.vezes_votadas = 0
        self.n_candidato_votado = 0

    def pode_votar(self):
        if self.vezes_votadas <= 1:
            return True
        else:
            return False

class Urna:
    def __init__(self):
        self.lista_de_candidatos = []
        self.lista_de_eleitores = []

    def adicionar_eleitor(self, eleitor):
        self.lista_de_eleitores.append(eleitor)

    def adicionar_candidato(self, candidato):
        self.lista_de_candidatos.append(candidato)

    def votar(self, eleitor, numero):
        if eleitor.pode_votar():
            # numero = int(input('Informe o número do candidato: '))
            for candidato in self.lista_de_candidatos:
                if candidato.numero == numero:
                    # candidato.adicionar_voto()
                    eleitor.n_candidato_votado = numero
                    eleitor.vezes_votadas += 1
                    print('Voto efetuado com sucesso!')
        else:
            print('ERRO! Eleitor já votou!')

    def apurar_votos(self):
        urnas_apuradas = 0
        for candidato in self.lista_de_candidatos:
            print('-' * 20)
            print(f'{urnas_apuradas}% das urnas apuradas')
            print(candidato)

        for eleitor in self.lista_de_eleitores:
            print('-' * 20)
            for candidato in self.lista_de_candidatos:
                if eleitor.n_candidato_votado == candidato.numero:
                    candidato.adicionar_voto()
                urnas_apuradas = randint(urnas_apuradas,100)
                print(f'{urnas_apuradas}% das urnas apuradas')
                print(candidato)
            sleep(2)
        print('-' * 50)


    def exibir_vencedor(self):
        vencedor = ''
        total_de_votos = len(self.lista_de_eleitores)
        num_votos_ganhador = 0
        for candidato in self.lista_de_candidatos:
            print(f'O candidato {candidato.nome} obteve {candidato.votos_recebidos} votos')
            if candidato.votos_recebidos > num_votos_ganhador:
                vencedor = candidato.nome
                num_votos_ganhador = candidato.votos_recebidos

        porcentagem_de_votos = round((num_votos_ganhador/total_de_votos)*100, 2)
        print(f'O vencerdor foi {vencedor} com {porcentagem_de_votos}% dos votos')

chave_de_encerramento = 1001

urna = Urna()
# # CADASTRO DOS CANDIDATOS
# while True:
#     print('CADASTRO DE CANDIDATO')
#     nome_candidato = str(input('NOME: '))
#     partido = str(input('PARTIDO: '))
#     numero = int(input('NÚMERO: '))
#     candidato = Candidato(nome_candidato, partido, numero, 'sp')
#     urna.adicionar_candidato(candidato)
#     res = input('Deseja adicionar mais algum candidato?[s/n] ').strip().lower()[0]
#     if res == 'n':
#         break
#
# # PERIODO DE ELEIÇÕES
# print('ELEIÇÕES 2024')
# while True:
#     nome_eleitor = str(input('NOME: '))
#     if nome_eleitor.isnumeric():
#         if int(nome_eleitor) == chave_de_encerramento:
#             break
#     cpf = int(input('CPF: '))
#     eleitor = Eleitor(nome_eleitor, cpf)
#     urna.adicionar_eleitor(eleitor)
#     urna.votar(eleitor)

candidato1 = Candidato('Candidato 1', 'P1', 1)
candidato2 = Candidato('Candidato 2', 'P2', 2)
urna.adicionar_candidato(candidato1)
urna.adicionar_candidato(candidato2)


eleitor1 = Eleitor('Maria', 123)
urna.adicionar_eleitor(eleitor1)
urna.votar(eleitor1, 1)
eleitor2 = Eleitor('Joao', 111)
urna.adicionar_eleitor(eleitor2)
urna.votar(eleitor2, 2)
eleitor3 = Eleitor('Jorge', 1111)
urna.adicionar_eleitor(eleitor3)
urna.votar(eleitor3, 1)


print("\n" * 130)
urna.apurar_votos()
urna.exibir_vencedor()


