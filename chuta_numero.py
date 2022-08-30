# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#essa é minha branch
print("bem vindo ao chuta numero, se acertar receberá um premio!")
tentativa=3
resposta="SIM"
while tentativa>0:
    numero = int(input("digite um numero:"))

    # print("digite outro numero"+str(numero))
    #numero=numero+1
    if numero==50:
        print("parebens seu premio é uma mamada")
        break

    elif numero>50:
        print("esta quase o numero é menor")
    else:
        print("esta quase o numero é maior")

    if tentativa==1: #numero != 50 :
        print("agora vc me deve uma mamada")

    tentativa=tentativa-1