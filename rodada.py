from partida import Partida
class Rodada:
    def __init__(self):
        self.partidas = []

    def add_partida(self,jogador1,jogador2):
        partida = Partida(jogador1,jogador2)
        self.partidas.append(partida)

    def jah_pegou(self,jogador1,jogador2):
        for i in range(len(self.partidas)):
            if (self.partidas[i].jogador1.nome == jogador1.nome and self.partidas[i].jogador2.nome == jogador2.nome) or (self.partidas[i].jogador1.nome == jogador2.nome and self.partidas[i].jogador2.nome == jogador1.nome):
                    return True
        return False