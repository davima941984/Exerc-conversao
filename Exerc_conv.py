print("Olá, este programa converte kilômetros em milhas.")

while True:
    x = int(input("Quantos kilômetros você deseja converter em milhas? "))  # inf_usuário
    y = float(0.62)
    print(x * y)  # Conversão km para milhas
    perg = input("Você deseja fazer mais alguma conversão? (s/n) ")
    if perg == "n":
        print("Até a póxima!")
        break
