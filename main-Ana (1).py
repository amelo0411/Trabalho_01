opcao = 1
while opcao != '4': # condição é aqui
    opcao = input('Escolha a viagem: [1] - RJ para SP, [2] - SP para MG, [3] - \
    MG para RS [4] - Sair')

    if opcao == '1':
        distancia_RJSP = 433
        tempo_RJSP = 5
        print("Você está viajando do Rio de Janeiro para São Paulo")
        print("Distância: " + str(distancia_RJSP) + " km")
        print("Tempo de viagem: " + str(tempo_RJSP) + " horas")

    elif opcao == '2':
        distancia_SPMG = 584
        tempo_SPMG = 6
        print("Você está viajando de São Paulo para Minas Gerais")
        print("Distância: " + str(distancia_SPMG) + " km")
        print("Tempo de viagem: " + str(tempo_SPMG) + " horas")

    elif opcao == '3':
        distancia_MGRS = 1608
        tempo_MGRS = 21
        print("Você está viajando de Minas Gerais para Rio Grande do Sul")
        print("Distância: " + str(distancia_MGRS) + " km")
        print("Tempo de viagem: " + str(tempo_MGRS) + " horas")

    elif opcao == '4':
        print("Encerrando o programa...")
    else:
        print("Opção inválida, insira outro valor")
