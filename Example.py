import URBasic 
import time
from gripper import Gripper

gripper = Gripper('10.224.1.253', 0) # Replace with YOUR IP adress
host = "10.224.1.115"   #E.g. a Universal Robot offline simulator, please adjust to match your IP
acc = 0.9
vel = 0.9
robotModle = URBasic.robotModel.RobotModel()
robot = URBasic.urScriptExt.UrScriptExt(host=host,robotModel=robotModle)

alto = 0.1821
baixo = -0.0392
distX = 0.0370
distY = 0.0370
pontoInicial = [-0.1965,  0.4425, alto, 2.8915, 1.2285, 0.0000]
pontoFinal = [-0.3090,  0.3268, alto, 2.8915, 1.2285, 0.0000]

def pick(gripper = gripper, ponto = pontoInicial, baixo = baixo, alto = alto):
    aux = ponto
    aux[2] = baixo
    robot.movel(aux)
    time.sleep(1)
    gripper.grip()
    time.sleep(1)
    aux[2] = alto
    robot.movel(aux)
    time.sleep(1)
    return aux

def move(gripper = gripper, ponto = pontoInicial, distX = distX, distY = distY):
    aux = ponto
    robot.movel(aux)
    time.sleep(1)
    return aux
    
def place(gripper = gripper, ponto = pontoInicial, baixo = baixo, alto = alto):
    aux = ponto
    aux[2] = baixo
    robot.movel(aux)
    time.sleep(1)
    gripper.set_position(40)
    time.sleep(1)
    aux[2] = alto
    robot.movel(aux)
    time.sleep(1)
    return aux

pontoInicial[0] = pontoInicial[0] + (2*distX)
pontoInicial[1] = pontoInicial[1] + (2*distY)
pontoFinal[0] = pontoFinal[0] - (7*distX)
pontoFinal[1] = pontoFinal[1] - (7*distY)
robot.movel(pontoInicial)
gripper.set_position(40)
input()
sumX = 0
sumY = 0
baixo = -0.0252
"""
#começa as brancas
for i in range(8):
    pick(ponto=pontoInicial)
    move(ponto = pontoFinal)
    place(ponto=pontoFinal)
    #sumX = sumX - distX
    #sumY = sumY + distY
    if(i==7):
        pontoInicial[0] = pontoInicial[0] - distX
        pontoInicial[1] = pontoInicial[1] - distY
        pontoFinal[0] = pontoFinal[0] - distX
        pontoFinal[1] = pontoFinal[1] - distY
        ponto = move(ponto=pontoInicial)
    else:
        pontoInicial[0] = pontoInicial[0] - distX
        pontoInicial[1] = pontoInicial[1] + distY
        pontoFinal[0] = pontoFinal[0] - distX
        pontoFinal[1] = pontoFinal[1] + distY
        ponto = move(ponto=pontoInicial)
    input()
#2º linha das brancas
for i in range(8):
    pick(ponto=pontoInicial)
    move(ponto = pontoFinal)
    place(ponto=pontoFinal)
    #sumX = sumX - distX
    #sumY = sumY + distY
    if(i==7):
        pontoInicial[0] = pontoInicial[0] + (3*distX)
        pontoInicial[1] = pontoInicial[1] + (3*distY)
        pontoFinal[0] = pontoFinal[0] - (6*distX)
        pontoFinal[1] = pontoFinal[1] - (6*distY)
        ponto = move(ponto=pontoInicial)
    else:
        pontoInicial[0] = pontoInicial[0] + distX
        pontoInicial[1] = pontoInicial[1] - distY
        pontoFinal[0] = pontoFinal[0] + distX
        pontoFinal[1] = pontoFinal[1] - distY
        ponto = move(ponto=pontoInicial)
    input()
"""
#começa as pretas

for i in range(8):
    pick(ponto=pontoInicial)
    move(ponto = pontoFinal)
    place(ponto=pontoFinal)
    #sumX = sumX - distX
    #sumY = sumY + distY
    if(i==7):
        pontoInicial[0] = pontoInicial[0] - distX
        pontoInicial[1] = pontoInicial[1] - distY
        pontoFinal[0] = pontoFinal[0] + distX
        pontoFinal[1] = pontoFinal[1] + distY
        ponto = move(ponto=pontoInicial)
    else:
        pontoInicial[0] = pontoInicial[0] - distX
        pontoInicial[1] = pontoInicial[1] + distY
        pontoFinal[0] = pontoFinal[0] - distX
        pontoFinal[1] = pontoFinal[1] + distY
        ponto = move(ponto=pontoInicial)
    input()
#segunda linha das pretas
for i in range(8):
    pick(ponto=pontoInicial)
    move(ponto = pontoFinal)
    place(ponto=pontoFinal)
    #sumX = sumX - distX
    #sumY = sumY + distY
    if(i==7):
        pontoInicial[0] = pontoInicial[0] + distX
        pontoInicial[1] = pontoInicial[1] - distY
        pontoFinal[0] = pontoFinal[0] + distX
        pontoFinal[1] = pontoFinal[1] - distY
        ponto = move(ponto=pontoInicial)
    else:
        pontoInicial[0] = pontoInicial[0] + distX
        pontoInicial[1] = pontoInicial[1] - distY
        pontoFinal[0] = pontoFinal[0] + distX
        pontoFinal[1] = pontoFinal[1] - distY
        ponto = move(ponto=pontoInicial)
    input()

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
