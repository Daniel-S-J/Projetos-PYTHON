#solicite ao usuário a quantidade de peças e o preço da peça
qntd_peças = int(input("Digite a quantidade de peças compradas: "))
preço = float(input("Digite o valor unitário da peça: "))
if qntd_peças <5:
    desconto = 0
elif 6  <= qntd_peças <= 10:
    desconto = 10
else:
    desconto = 20

valor_total = preço * qntd_peças 
valor_final = valor_total * (1 - desconto/100)

print (f"O valor final é: {valor_final}")




