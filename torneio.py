from jogador import Jogador
from partida import Partida
from rodada import Rodada
from random import shuffle
class Torneio:
    def __init__(self):
        self.nome = ""
        self.rodadas = []
        self.jogadores = []

    def add_jogador(self,nome):
        jogador = Jogador()
        jogador.nome = nome
        self.jogadores.append(jogador)

    def numero_rodadas_sugeridas(self):
        if len(self.jogadores) < 4:
            return 0
        if len(self.jogadores) < 9:
            return 3
        if len(self.jogadores) < 25:
            return 4
        if len(self.jogadores) < 45:
            return 5
        if len(self.jogadores) < 149:
            return 6
        return 7

    def qual_rodada(self):
        return len(self.rodadas) + 1

    def primeira_rodada(self):
        jogadores_temp = self.jogadores_temp()
        shuffle(jogadores_temp)

        rodada1 = Rodada()
        i = 0
        while i < len(jogadores_temp):
            rodada1.add_partida(jogadores_temp[i], jogadores_temp[i+1])
            i += 2
            if i == len(jogadores_temp) - 1:
                jogadores_temp[i].byes += 1
                break
        
        self.rodadas.append(rodada1)

    def jah_pegou(self,jogador1,jogador2):
        for i in range(len(self.rodadas)):
            if self.rodadas[i].jah_pegou(jogador1,jogador2):
                return True
        return False

    def jogador_menos_byes_menos_pontos(self,jogadores_temp):
        indice = 0
        for i in range(1,len(jogadores_temp)):
            if jogadores_temp[indice].byes > jogadores_temp[i].byes:
                indice = i
        for i in range(1,len(jogadores_temp)):
            if jogadores_temp[indice].byes == jogadores_temp[i].byes and jogadores_temp[indice].pontos > jogadores_temp[i].pontos:
                indice = i
        return i

    def jogadores_temp(self):
        jogadores_temp = []
        for i in range(len(self.jogadores)):
            jogadores_temp.append(self.jogadores[i])
        return jogadores_temp

    def jogador_aleatorio_com_mais_pontos(self,jogadores_temp):
        maior_pontuacao = self.maior_pontuacao(jogadores_temp)
        jogadores_maior_pontuacao = []
        for i in range(len(jogadores_temp)):
            if jogadores_temp[i].pontos == maior_pontuacao:
                jogadores_maior_pontuacao.append(jogadores_temp[i])
        shuffle(jogadores_maior_pontuacao)
        return jogadores_maior_pontuacao[0]
    
    def maior_pontuacao(self,jogadores_temp):
        pontos = 0
        for i in range(len(jogadores_temp)):
            if jogadores_temp[i].pontos > pontos:
                pontos = jogadores_temp[i].pontos
        return pontos

    def remove_jogador(self,jogadores_temp,jogador):
        indice = -1
        for i in range(len(jogadores_temp)):
            if jogadores_temp[i].nome == jogador.nome:
                indice = i
                break
        del jogadores_temp[indice]

    def proxima_rodada(self):
        jogadores_temp = self.jogadores_temp()
        if len(jogadores_temp) % 2 != 0:
            indice_bye = self.jogador_menos_byes_menos_pontos(jogadores_temp)
            jogadores_temp[indice_bye].byes += 1
            del jogadores_temp[indice_bye]
        
        rodada = Rodada()
        while len(jogadores_temp) > 0:
            jogador1 = self.jogador_aleatorio_com_mais_pontos(jogadores_temp)
            self.remove_jogador(jogadores_temp,jogador1)

            achou = False
            jogadores_removidos = []

            while not achou:
                jogador2 = self.jogador_aleatorio_com_mais_pontos(jogadores_temp)
                self.remove_jogador(jogadores_temp,jogador2)

                if not self.jah_pegou(jogador1,jogador2):
                    achou = True
                    rodada.add_partida(jogador1,jogador2)
                else:
                    jogadores_removidos.append(jogador2)
            
            for i in range(len(jogadores_removidos)):
                jogadores_temp.append(jogadores_removidos[i])
        
        self.rodadas.append(rodada)



