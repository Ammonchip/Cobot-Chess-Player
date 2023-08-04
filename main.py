import rtde_control
import time
from gripper import Gripper

HOST = "10.224.1.252"   #ARM ip address
GRIPPER = "10.224.1.253" #CLP gripper control 
rtde_c = rtde_control.RTDEControlInterface(HOST)
gripper = Gripper(GRIPPER) # Replace with YOUR IP adress
gripper.grip()
#altura em que a garra levanta 
alto = 0.1821
#altura que a garra abaixa
baixo = -0.0450
#distância de uma célula para outra
distX = 0.0370
distY = 0.0370
#ponto inicial, é o ponto em que o robô começa a pegar as peças para arrumar
pontoInicial = [-0.1965,  0.4425, alto, 2.8915, 1.2285, 0.0000]
#ponto final, é o ponto em que o robô começa a pegar as peças do tabuleiro para "desarrumar"
pontoFinal = [-0.3090,  0.3268, alto, 2.8915, 1.2285, 0.0000]
#função pick para pegar as peças em um dado ponto variando o eixo z(subindo)
def pick(gripper = gripper, ponto = pontoInicial, baixo = baixo, alto = alto):
    aux = ponto
    aux[2] = baixo
    rtde_c.moveL(aux)
    #time.sleep(3)
    gripper.grip()
    #time.sleep(3)
    aux[2] = alto
    rtde_c.moveL(aux)
    #time.sleep(3)
    return aux
#função move, move a TCP para um determinado ponto no plano variando o eixo x, y
def move(gripper = gripper, ponto = pontoInicial, distX = distX, distY = distY):
    aux = ponto
    rtde_c.moveL(aux)
    #time.sleep(3)
    return aux
#função place para soltar a peça em um determinado ponto variando o eixo z(descendo)
def place(gripper = gripper, ponto = pontoInicial, baixo = baixo, alto = alto):
    aux = ponto
    aux[2] = -0.0400
    rtde_c.moveL(aux)
    #time.sleep(3)
    gripper.set_position(40)
    time.sleep(1)
    aux[2] = alto
    rtde_c.moveL(aux)
    #time.sleep(3)
    return aux
#troca os pontos finais e iniciais 
def troca(pontoInicial, pontoFinal):
    aux = pontoFinal
    pontoFinal = pontoInicial
    pontoInicial = aux
    return pontoInicial, pontoFinal
'''
#j = 1 o cobot começa a arrumar as peças de xadrez de fora para dentro do tabuleiro
#j = 2 o cobot começa a arrumar as peças de xadrez de dentro para fora do tabuleiro
j = 2
#move o braço para o ponto inicial
rtde_c.moveL(pontoInicial)
#inicia a posição dos dedos da garra
gripper.set_position(40)
time.sleep(1)

while(j):
    pontoInicial = [-0.1965,  0.4425, alto, 2.8915, 1.2285, 0.0000]
    pontoFinal = [-0.3090,  0.3268, alto, 2.8915, 1.2285, 0.0000]
    #decide se arruma ou desarruma
    if(j%2==0):
        pontoInicial, pontoFinal = troca(pontoInicial, pontoFinal)
    rtde_c.moveL(pontoInicial)
    gripper.set_position(40)
    time.sleep(1)
    
    #começa as brancas
    for i in range(8):
        pick(ponto=pontoInicial)
        move(ponto = pontoFinal)
        place(ponto=pontoFinal)
        #condição para iniciar segunda fileira de peças brancas
        if(i==7):
            #move direita
            pontoInicial[0] = pontoInicial[0] - distX
            pontoInicial[1] = pontoInicial[1] - distY
            #move direita
            pontoFinal[0] = pontoFinal[0] - distX
            pontoFinal[1] = pontoFinal[1] - distY
            move(ponto=pontoInicial)
        else:
            #move baixo
            pontoInicial[0] = pontoInicial[0] - distX
            pontoInicial[1] = pontoInicial[1] + distY
            #move baixo
            pontoFinal[0] = pontoFinal[0] - distX
            pontoFinal[1] = pontoFinal[1] + distY
            move(ponto=pontoInicial)
        
    #2º linha das brancas
    for i in range(8):
        pick(ponto=pontoInicial)
        move(ponto = pontoFinal)
        place(ponto=pontoFinal)
        #condição para iniciar primeira fileira de peças pretas
        if(i==7):
            if (j%2==0):
                #move direita 6 casas
                pontoInicial[0] = pontoInicial[0] - (6*distX)
                pontoInicial[1] = pontoInicial[1] - (6*distY)
                #move esquerda 3 casas
                pontoFinal[0] = pontoFinal[0] + (3*distX)
                pontoFinal[1] = pontoFinal[1] + (3*distY)
            else:
                #move esquerda 3 casas
                pontoInicial[0] = pontoInicial[0] + (3*distX)
                pontoInicial[1] = pontoInicial[1] + (3*distY)
                #move direita 6 casas
                pontoFinal[0] = pontoFinal[0] - (6*distX)
                pontoFinal[1] = pontoFinal[1] - (6*distY)
            move(ponto=pontoInicial)
        else:
            #move cima 
            pontoInicial[0] = pontoInicial[0] + distX
            pontoInicial[1] = pontoInicial[1] - distY
            #move cima
            pontoFinal[0] = pontoFinal[0] + distX
            pontoFinal[1] = pontoFinal[1] - distY
            move(ponto=pontoInicial)

    #começa as pretas
    for i in range(8):
        pick(ponto=pontoInicial)
        move(ponto = pontoFinal)
        place(ponto=pontoFinal)
        #condição para iniciar segunda fileira de peças pretas
        if(i==7):
            if(j%2==0):
                #move esquerda
                pontoInicial[0] = pontoInicial[0] + distX
                pontoInicial[1] = pontoInicial[1] + distY
                #move direita
                pontoFinal[0] = pontoFinal[0] - distX
                pontoFinal[1] = pontoFinal[1] - distY
            else:
                #move direita
                pontoInicial[0] = pontoInicial[0] - distX
                pontoInicial[1] = pontoInicial[1] - distY
                #move esquerda
                pontoFinal[0] = pontoFinal[0] + distX
                pontoFinal[1] = pontoFinal[1] + distY
            move(ponto=pontoInicial)
        else:
            #move baixo
            pontoInicial[0] = pontoInicial[0] - distX
            pontoInicial[1] = pontoInicial[1] + distY
            #move baixo
            pontoFinal[0] = pontoFinal[0] - distX
            pontoFinal[1] = pontoFinal[1] + distY
            move(ponto=pontoInicial)

    #segunda linha das pretas
    for i in range(8):
        pick(ponto=pontoInicial)
        move(ponto = pontoFinal)
        place(ponto=pontoFinal)
    
        if(i==7):
            #move cima
            pontoInicial[0] = pontoInicial[0] + distX
            pontoInicial[1] = pontoInicial[1] - distY
            #move cima
            pontoFinal[0] = pontoFinal[0] + distX
            pontoFinal[1] = pontoFinal[1] - distY
            move(ponto=pontoInicial)
        else:
            #move cima
            pontoInicial[0] = pontoInicial[0] + distX
            pontoInicial[1] = pontoInicial[1] - distY
            #move cima
            pontoFinal[0] = pontoFinal[0] + distX
            pontoFinal[1] = pontoFinal[1] - distY
            move(ponto=pontoInicial)
    #incrementa contador j
    j = j + 1 
'''