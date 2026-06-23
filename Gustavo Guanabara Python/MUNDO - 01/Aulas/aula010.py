from datetime import datetime

print("\n==== VERIFICAR SE CARRO PODE RODAR TVDE - PT ====")

data_limite = datetime.strptime("11/06/2019", "%d/%m/%Y")

while True:
    try:
        data_fab = input("\nDATA (DD/MM/AAAA): ")

        data_carro = datetime.strptime(data_fab, "%d/%m/%Y")

        if data_carro >= data_limite:
            print(f"\nDATA: {data_fab} = SIM, PODE RODAR NO TVDE")
        else:
            print(f"\nDATA: {data_fab} = NÃO PODE RODAR NO TVDE")

        break  # sai do laço quando a data é válida

    except ValueError:
        print("\nErro: informe a data no formato DD/MM/AAAA")
        print("Exemplo: 15/08/2020")
        # volta automaticamente para pedir a data novamente

print("\n####################....100% PROGRAMA FINALIZADO....")