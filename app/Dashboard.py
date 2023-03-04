import os 
def MENU():                                                                                             # INTERFACE
    os.system('cls')
    print("\t"*3+"█"*58)
    print("\t"*3+"██"+"\t"*7+"██")
    print("\t"*3+"██"+"\t"*2+"CERTIFICATE POINT CALCULATOR"+"\t"*2+"██")
    print("\t"*3+"██"+"\t"*7+"██")
    print("\t"*3+"█"*58)


def PROGBAR(nue,den,filename):                                                                                   # PROGRESS BAR
    os.system('cls')
    prog=(nue/den)*10
    print("Progress: [","█"*int(prog)," "*(10-int(prog)),"\b] ~",int(prog*10),"%")
    print("\nNO =",nue,", File =",filename)