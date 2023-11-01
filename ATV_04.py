Num = int(input("Digite um Número Inteiro entre 0 e 100: "))

if Num < 100 and Num > 0:
    Num_primo = True
    
    if Num <= 1:
        Num_primo = False
    else:
        for i in range(2, int(Num ** 0.5) + 1):
            if Num % i == 0:
                Num_primo = False
                break
    
    if Num_primo:
        print(f"{Num} é um número primo.")
    else:
        print(f"{Num} não é um número primo.")
else:
    print("O número digitado náo eestá no intervalo de (0 a 100).")
