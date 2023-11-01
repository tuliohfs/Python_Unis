# Ler os valores de entrada
lado1 = int(input("Digite o valor de a: "))
lado2 = int(input("Digite o valor de b: "))
lado3 = int(input("Digite o valor de c: "))

# Função para calcular a área de um triângulo usando a fórmula de Heron
def calcula_area(lado1, lado2, lado3):
    s = (lado1 + lado2 + lado3) / 2
    area = (s * (s - lado1) * (s - lado2) * (s - lado3)) ** 0.5
    return area

# Função para verificar se os valores formam um triângulo
def verificacao(a, b, c):
    if a > b + c or b > a + c or c > a + b:
        return False
    else:
        return True

# Verificar se os valores formam um triângulo
if verificacao(lado1, lado2, lado3):
    # Se formam um triângulo, calcular a área
    area = calcula_area(lado1, lado2, lado3)
    print(f"Os valores {lado1}, {lado2} e {lado3} formam um triângulo com área {area:.2f}")
else:
    # Se não formam um triângulo, mostrar os valores lidos
    print(f"Os valores {lado1}, {lado2} e {lado3} não formam um triângulo.")
