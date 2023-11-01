def inverter(frase):
    # Dividi a frase em palavras usando o espaço
    palavrasInv = [palavra[::-1] for palavra in frase.split()]

    # Junta as palavras invertidas em uma nova frase
    nova_frase = ' '.join(palavrasInv)

    return nova_frase

fraseOrg = input('Digite a sua frase: ')
fraseInv = inverter(fraseOrg)
print(fraseInv)
