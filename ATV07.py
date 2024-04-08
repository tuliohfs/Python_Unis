def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

# Exemplo de uso
if __name__ == "__main__":
    num = 5
    print(f'O fatorial de {num} é {fatorial(num)}')
