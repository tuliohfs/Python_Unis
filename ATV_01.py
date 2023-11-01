
Qtd_Dias = int(input("Por favor digite quantos dias de vida tem: "))

Const_Ano = 365
Const_Mes = 30


anos = Qtd_Dias // Const_Ano
meses = (Qtd_Dias % Const_Ano) // Const_Mes
dias = (Qtd_Dias % Const_Ano) % Const_Mes


print(f"Voce tem {anos}, {meses} Meses e {dias} dias de Vida")
