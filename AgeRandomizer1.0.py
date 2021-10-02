import random

#abre o arquivo, somente para leitura
arq = open("povos.txt","r")
linhas = arq.readlines()

#função random coop
def randeqp(eqp1,eqp2):
    print("Iniciando Sorteio de Equipes...")
    eqps = set()
    i=0
    i2=0
    print("Equipe 1: ")
    #laço com tamanho da equipe
    while i < eqp1:
        x = random.randrange(0,len(linhas))
        #comando que garante que não haja repetição de civilizações
        if x not in eqps:
            i += 1
            eqps.add(x)
            #conserto de bug com a ultima linha
            if x==0:
                print(linhas[x-1],"\n")
            else:
                print(linhas[x-1])
    print("Equipe 2: ")
    #laço com tamanho da equipe
    while i2 < eqp2:
        x = random.randrange(0,len(linhas))
        #comando que garante que não haja repetição de civilizações
        if x not in eqps:
            i2 += 1
            eqps.add(x)
            #conserto de bug com a ultima linha
            if x==0:
                print(linhas[x-1],"\n")
            else:
                print(linhas[x-1])
                
#função random ffa
def randffa(nump):
    print("Iniciando sorteio de Civilizações...")
    civ = set()
    i=0
    ip=0
    #laço com quantidade de players
    while i < nump:
        x = random.randrange(0,len(linhas))
        #comando que garante que não haja repetição de civilizações
        if x not in civ:
             i += 1
             ip += 1
             civ.add(x)
             if x==0:
                print("Player",ip,":")
                print(linhas[x-1],"\n")
             else:
                print("Player",ip,":")
                print(linhas[x-1])


#entrada das variáveis
#Laço de repetição para escolha correta de modo de jogo
while True:
    modo = str(input("Qual vai ser o modo de jogo? Coop ou FFA?"))
    modo = modo.lower()
    if (modo=="coop") or (modo=="ffa"):
        break
if (modo=="coop"):
    eqp1 = int(input("Informe quantos jogadores na Equipe 1: "))
    eqp2 = int(input("Informe quantos jogadores na Equipe 2: "))
    randeqp(eqp1,eqp2)
else:
    nump = int(input("Informe o número de players: "))
    randffa(nump)
    

