#Algoritmo Ex1 - P1 (entendimento)
#declarar
Altura: float = 0.0
Idade: int = 0
Sexo: int = 0
cta: int = 1
Altura_maior = 0
Altura_menor = 10
Idade_maior: int = 0
Idade_menor: int = 0
ctah: int = 0
ctam: int = 0
MDh: float = 0
MDm: float = 0

def medias (Soma_alturah, Soma_alturam, contah, contam):
    Media_homens: float = 0.0
    Media_mulheres: float = 0.0

    Media_homens = (Soma_alturah / contah)
    Media_mulheres = (Soma_alturam / contam)

    print("A média da altura dos homens entre 18 e 35 anos é de" , Media_homens, ", enquanto a média da altura das mulheres é de" , Media_mulheres)

def soma_alturas():
    global MDh
    global MDm
    global ctah
    global ctam
    
    if Sexo == 1:
        if (Idade >= 18 and Idade <= 35):
            MDh = MDh + Altura
            ctah += 1
    elif Sexo == 2:
        MDm = MDm + Altura
        ctam += 1

    

def busca_cta(conta):
    global Altura_maior
    global Altura_menor
    global Idade_menor
    global Idade_maior

    if (Altura > Altura_maior):
        Altura_maior = Altura
        Idade_maior = Idade
    elif(Altura < Altura_menor):
        Altura_menor = Altura
        Idade_menor = Idade
    
    conta += 1
    return conta


def main():
    global Altura
    global Idade
    global Sexo
    global cta
    while (cta <= 5):
        print("Dados da" , cta , '° pessoa: ')
        Altura = float(input('Digite a altura da pessoa: '))
        Idade = int(input("Digite a idade da pessoa: "))
        Sexo = int(input("Digite o sexo da pessoa, sendo 1 para homem e 2 para mulher: "))

        cta = busca_cta(cta)
        soma_alturas()

    medias(MDh, MDm, ctah, ctam)
    print("A maior altura é de " , Altura_maior , "e sua idade é de ", Idade_maior, "anos.")
    print("A menor altura é de " , Altura_menor , "e sua idade é de " , Idade_menor, "anos.")

if (__name__ == '__main__'):
    main()



        