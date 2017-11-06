from torneio import Torneio

champ = Torneio()
champ.nome = "Torneio Hello World"
champ.add_jogador("Leonardo")
champ.add_jogador("Anderson")
champ.add_jogador("Julio")
champ.add_jogador("Danilo")
champ.add_jogador("Joaquim")
champ.add_jogador("Abelardo")
champ.add_jogador("João")
champ.add_jogador("Emerson")
champ.add_jogador("Gleydson")
champ.add_jogador("André")
champ.add_jogador("Rafael")

print(champ.numero_rodadas_sugeridas())
print()

champ.primeira_rodada()
champ.proxima_rodada()

for i in range(len(champ.rodadas)):
    print("Rodada %d" % (i+1))
    for j in range(len(champ.rodadas[i].partidas)):
        p = champ.rodadas[i].partidas[j]
        print(p.jogador1.nome)
        print("x")
        print(p.jogador2.nome)
        print()
        print()

for i in range(len(champ.jogadores)):
    if champ.jogadores[i].byes > 0:
        print(champ.jogadores[i].nome)
        print("BYE")
        print()
        print()