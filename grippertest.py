from gripper.gripper import Gripper
gripper = Gripper('10.224.1.253') # Replace with YOUR IP adress
while(1):
    i = int(input("1 para fechar\n0 para abrir\n"))
    if (i == 1) : 
        gripper.grip()
    elif (i == 0) : 
        gripper.set_position(40)
    else : break
    

