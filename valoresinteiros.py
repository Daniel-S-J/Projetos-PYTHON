pares = 0
impares = 0
positivo = 0
negativo = 0
valor = []
for i in range (5):
    #Informe ao usuário que ele precisa digitar 5 números inteiros
    valores = int(input(f"Digite o {i+1} valor: "))
    valor.append(valores)
for v in valor:
    if v % 2 == 0:
        pares += 1
    else:
        impares += 1

    if v > 0:
        positivo += 1
    elif v < 0:
        negativo += 1

print (f"{pares} valor par(es)")
print (f" {impares} valor impar(es)")
print (f"{negativo} valor negativo(s)")
print (f"{positivo} valor positivo(s)")


