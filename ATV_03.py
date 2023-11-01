Num_01 = int(input("Digite um Número Inteiro: "))
Num_02 = int(input("Digite outro Número Inteiro: "))
Num_03 = int(input("Digite outro Número Inteiro: "))

Num_menor = Num_01

if Num_02 < Num_menor:
    Num_menor = Num_02

if Num_03 < Num_menor:
    Num_menor = Num_03

print(f'O menor Número e {Num_menor}')