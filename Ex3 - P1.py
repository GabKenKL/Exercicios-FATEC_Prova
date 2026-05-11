#Declarar
N: int = 0
contador_de_formulas: int = 0

def Dados():
    global contador_de_formulas
    vl1: int = 0
    vl2: int = 0
    vl3: int = 0
    soma: int = 0

    while (vl1 < 6):
        vl1 = vl1 + 1
        vl2 = 0
        while (vl2 < 6):
            vl2 = vl2 + 1
            vl3 = 0
            while (vl3 < 6):
                vl3 = vl3 + 1
                soma = vl1 + vl2 + vl3
                if (soma == N):
                    print(vl1 , "+" , vl2 , "+" , vl3 , "=" , N)
                    contador_de_formulas += 1
    

def Busca():
    global N
    while (N < 3 or N > 18):
        N = int(input("Valor inválido. Digite um valor entre 3 e 18: "))

def main():
    global N
    global contador_de_formulas

    N = int(input("Digite um número entre 3 e 18:"))
    if (N < 3 or N > 18):
        Busca()
    Dados()
    print("O número de modos possíveis de fazer são " , contador_de_formulas)

if (__name__ == '__main__'):
    main()
