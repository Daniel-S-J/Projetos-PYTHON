# Solicita dados ao usuário

quantidade = int(input("Informe a quantidade de peças compradas: "))

preco_unitario = float(input("Informe o preço unitário: R$ "))
 
# Define o desconto

if quantidade <= 5:

    desconto = 0

elif 6 <= quantidade <= 10:

    desconto = 0.10

else:

    desconto = 0.20
 
# Calcula valores

total_sem_desconto = quantidade * preco_unitario

valor_desconto = total_sem_desconto * desconto

total_final = total_sem_desconto - valor_desconto


print(f"Preço total sem desconto: R$ {total_sem_desconto:.2f}")

print(f"Desconto aplicado: {desconto * 100:.0f}%")

print(f"Valor do desconto: R$ {valor_desconto:.2f}")

print(f"Preço final: R$ {total_final:.2f}")
 