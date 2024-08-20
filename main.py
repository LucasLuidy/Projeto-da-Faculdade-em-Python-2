def calcular_PGCF(CT, DCP):
    return (((CT / 0.7067) - DCP) / 0.9156) - DCP

while True:

    num_gatos = int(input("Digite o número de gatos (deve ser maior que zero): "))

    abaixo_do_peso = 0
    peso_ideal = 0
    acima_do_peso = 0
    soma_PGCF_abaixo_do_peso = 0
    soma_PGCF_peso_ideal = 0
    soma_PGCF_acima_do_peso = 0

    for i in range(1, num_gatos + 1):
        while True:
            try:
                CT = float(input(f"\nGato {i}:\nDigite a Circunferência Torácica em (cm): "))
                DCP = float(input(f"Digite a Distância entre o Calcâneo e a Patela em (cm): "))
                if CT <= 0 or DCP <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Entrada inválida. Digite novamente.")

        PGCF = calcular_PGCF(CT, DCP)

        if PGCF < 20:
            abaixo_do_peso += 1
            soma_PGCF_abaixo_do_peso += PGCF
        elif 20 <= PGCF < 27:
            peso_ideal += 1
            soma_PGCF_peso_ideal += PGCF
        else:
            acima_do_peso += 1
            soma_PGCF_acima_do_peso += PGCF

        print(f"PGCF: {PGCF:.2f}")
        if PGCF < 20:
            print("O gato está abaixo do peso")
        elif 20 <= PGCF < 27:
            print("O gato está no peso ideal")
        else:
            print("O gato está acima do peso")

    print("\nResultados:")
    if abaixo_do_peso > 0:
        media_PGCF_abaixo_do_peso = soma_PGCF_abaixo_do_peso / abaixo_do_peso
        print(f"Abaixo do Peso: {abaixo_do_peso} animais, PGCF médio: {media_PGCF_abaixo_do_peso:.2f}")
    if peso_ideal > 0:
        media_PGCF_peso_ideal = soma_PGCF_peso_ideal / peso_ideal
        print(f"Peso Ideal: {peso_ideal} animais, PGCF médio: {media_PGCF_peso_ideal:.2f}")
    if acima_do_peso > 0:
        media_PGCF_acima_do_peso = soma_PGCF_acima_do_peso / acima_do_peso
        print(f"Acima do Peso: {acima_do_peso} animais, PGCF médio: {media_PGCF_acima_do_peso:.2f}")
        
    opcaoCh = input("Pressione a tecla ENTER para repetir o programa ou qualquer outra tecla para sair: ")

    if opcaoCh != "":
        break

