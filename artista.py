Agenda = ["Banda a", "Banda b", "Cantor"]
print ("Agenda original", Agenda)
artista_cancelado = input ("Digite o nome do artista: ")
if artista_cancelado in Agenda:
    indice = Agenda.index (artista_cancelado)
    novo_artista = input ("Digite um novo artista: ")
    Agenda.pop (indice)
    Agenda.insert (indice, novo_artista)
    print ("""Agenda atualizada""", Agenda)
else:
    print(f" O artista '{artista_cancelado}' não foi encontrado")