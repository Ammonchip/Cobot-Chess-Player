import URBasic 
import time
from gripper import Gripper

gripper = Gripper('10.224.1.253', 0) # Replace with YOUR IP adress
host = "10.224.1.115"   #E.g. a Universal Robot offline simulator, please adjust to match your IP
acc = 3
vel = 3
robotModle = URBasic.robotModel.RobotModel()
robot = URBasic.urScriptExt.UrScriptExt(host=host,robotModel=robotModle)

alto = 0.1821
baixo = -0.0450
distX = 0.0370
distY = 0.0370
pontoInicial = [-0.1965,  0.4425, alto, 2.8915, 1.2285, 0.0000]
pontoFinal = [-0.3090,  0.3268, alto, 2.8915, 1.2285, 0.0000]

def pick(gripper = gripper, ponto = pontoInicial, baixo = baixo, alto = alto):
    aux = ponto
    aux[2] = baixo
    robot.movel(aux)
    #time.sleep(1)
    gripper.grip()
    #time.sleep(1)
    aux[2] = alto
    robot.movel(aux)
    #time.sleep(1)
    return aux

def move(gripper = gripper, ponto = pontoInicial, distX = distX, distY = distY):
    aux = ponto
    robot.movel(aux)
    #time.sleep(1)
    return aux
    
def place(gripper = gripper, ponto = pontoInicial, baixo = baixo, alto = alto):
    aux = ponto
    aux[2] = -0.0400
    robot.movel(aux)
    #time.sleep(1)
    gripper.set_position(40)
    #time.sleep(1)
    aux[2] = alto
    robot.movel(aux)
    #time.sleep(1)
    return aux

def troca(pontoInicial, pontoFinal):
    aux = pontoFinal
    pontoFinal = pontoInicial
    pontoInicial = aux
    return pontoInicial, pontoFinal

pontoInicial[0] = pontoInicial[0] + (2*distX)
pontoInicial[1] = pontoInicial[1] + (2*distY)
pontoFinal[0] = pontoFinal[0] - (7*distX)
pontoFinal[1] = pontoFinal[1] - (7*distY)


j = 2

#robot.movel(pontoInicial)
#time.sleep(5)

while(j):
    pontoInicial = [-0.1965,  0.4425, alto, 2.8915, 1.2285, 0.0000]
    pontoFinal = [-0.3090,  0.3268, alto, 2.8915, 1.2285, 0.0000]
    if(j%2==0):
        pontoInicial, pontoFinal = troca(pontoInicial, pontoFinal)
    robot.movel(pontoInicial)
    time.sleep(5)
    gripper.set_position(45)
    time.sleep(3)
    
    #começa as brancas
    for i in range(8):
        pick(ponto=pontoInicial)
        move(ponto = pontoFinal)
        place(ponto=pontoFinal)

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
            pontoInicial[0] = pontoInicial[0] + distX
            pontoInicial[1] = pontoInicial[1] - distY
            pontoFinal[0] = pontoFinal[0] + distX
            pontoFinal[1] = pontoFinal[1] - distY
            move(ponto=pontoInicial)

    #começa as pretas
    for i in range(8):
        pick(ponto=pontoInicial)
        move(ponto = pontoFinal)
        place(ponto=pontoFinal)

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
    j = j + 1 


#gripper.set_position(40)
#robot.movel(pose=pontoInicial, a=1.2, v=vel)

"""
pose = robot.get_actual_tcp_pose()
time.sleep(1)
print("Posicao atual do robo" + str(pose))
gripper.grip()
time.sleep(1)
robot.movel(pose=[-0.2293,  0.4411, alto,    2.8914,  1.2285,  0.0000], a=1.2, v=vel)
time.sleep(1)
robot.movel(pose=[-0.5909,  0.3811,  alto,    2.8914,  1.2285,  0.0000], a=1.2, v=vel)
time.sleep(1)
robot.movel(pose=[-0.5909,  0.3811, baixo,    2.8914,  1.2285,  0.0000], a=1.2, v=vel)
time.sleep(1)
gripper.set_position(40)
time.sleep(1)
"""
