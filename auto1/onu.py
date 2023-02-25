import xtelnet
import pexpect
import time

print("="*52)
print("="*15, "Sistema Automatizado", "="*15)
print("="*52, "\n")

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

    opcao_de_versap = int(input("Digite a opção: (1 ou 2): "))


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
def nokia():

    ip = '192.168.1.1'
    p = 23

    tn = pexpect.spawn('telnet ' + ip)

    #Comando que apaga tudo e retorna padrão de fábrica
    tn.expect('/sbin # ')
    tn.sendline('cfgcli -r')
    tn.expect('/sbin # ')

    print(tn.before.decode())#Imprime o comando que foi lançado anteriormente

    # Reinicia o produto
    tn.sendline('reboot')
    tn.expect('/sbin # ')

    print(tn.before.decode())
    tn.close()

boll = True

while (boll):

    option = str(input("Digite Sim (S) para inicializar o sistema e Não (N) para finalizar (s ou n): ")).lower()

    if (option == "s"):

        onuType = int(input("Enter your type ont: "))

        if (onuType == 1):
            onu_huawei()

        elif (onuType == 2):
            gm620()

        elif (onuType == 3):
            nokia()

        boll = True
    elif(option == "n"):
        boll = False
        print("Sistema finalizado com sucesso...")