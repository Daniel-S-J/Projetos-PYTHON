
 
# Salas

sala_XD = [[0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0]]
 
sala_HD = [[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]]
 

 
# Todas as salas 

salas = [sala_XD, sala_HD]
 
while True:

    print("1 - Escolher sala")
    print("2 - Sair")
 
    opcao = input("Digite sua opção: ")
 
    if opcao == "1":

        print("""Salas disponíveis:""")

        print("2 - Sala XD (4x4)")

        print("3 - Sala HD (3x3)")

        num_sala = int(input("Escolha a sala: "))
 
        if num_sala >= 1 and num_sala <= 2:

            sala = salas[num_sala - 1]
 
            # Mostrar assentos

            print("\nMapa de assentos (0 = livre, X = ocupado):")

            for linha in sala:

                for assento in linha:

                    if assento == 0:

                        print("0", end=" ")

                    else:

                        print("X", end=" ")

                print()
 
            # Reservar assento

            l = int(input("Escolha a linha: ")) - 1

            c = int(input("Escolha a coluna: ")) - 1
 
            if sala[l][c] == 0:

                sala[l][c] = 1

                print("Assento reservado com sucesso!")

            else:

                print("Esse assento já está ocupado!")

        else:

            print("Sala inválida!")
 
    elif opcao == "2":

        print("Saindo...")

        break
 
    else:

        print("Opção inválida, tente de novo!")
 