idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso:KG "))
altura = float(input("Digite sua altura: "))

if((idade > 18) and (peso >= 60.0) and (altura >= 1.70)):
    print("Apto a entrar no exercito!")
else:
    print("Você não está apto a entrar no exercito!")