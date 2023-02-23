import xtelnet
import time


t = xtelnet.session()

def connectTelnet(ip, user, passw, port, tm):
    t.connect(ip, username=user, password=passw, p=port, timeout=tm)

# 1
def onu_huawei():

    connectTelnet('192.168.100.1', 'root', 'admin', 23, 5)
    #Entra no modo admin
    su = t.execute("su\r\n")
    print(su)
    #Reseta o produto
    print("Processing...")
    time.sleep(0.5)
    comand = t.execute("reset")
    print(comand)
    print("successfully reset...")


# 2
def gm620():

    opcao_de_versap = int(input("Digite a opção: (1 ou 2)"))


    if (opcao_de_versap == 1):

        t.connect('192.168.1.1', 'root', 'Pon620', 23, 5)
        time.sleep(0.5)
        print("Processing...")
        #Reseta o produto
        comand = t.execute("sidbg 1 DB reset")
        print(comand)

    elif(opcao_de_versap == 2):

        t.connect('192.168.1.1', 'root', 'Zte521', 23, 5)
        time.sleep(0.5)
        print("Processing...")
        #Reseta o produto
        comand = t.execute("sidbg 1 DB reset")
        print(comand)
    
        print("successfully reset...")

# 3
# def nokia():

#     connectTelnet('192.168.1.1', '', '', 23, 5)
#     time.sleep(0.5)
#     print("Processing...")
#     nokiaComnad = t.execute("cfgcli -r")
#     print(nokiaComnad)

#     reboot = t.execute("reboot")
#     print(reboot)
#     print("successfully reset...")

# if (onuType == 1):
#     onu_huawei()
# elif (onuType == 2):
#     gm620()

boll = True

while (boll):

    option = str(input("Digite Sim para inicializar o sistema e Não para finalizar (s ou n): ")).lower()

    if (option == "s"):

        onuType = int(input("Enter your type ont: "))

        if (onuType == 1):
            onu_huawei()
        elif (onuType == 2):
            gm620()

        boll = True
    elif(option == "n"):
        boll = False
        print("Sistema finalizado com sucesso...")