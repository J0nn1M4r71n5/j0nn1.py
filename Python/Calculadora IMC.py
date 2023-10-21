
def calcular_imc(peso, altura):
    try:
        altura_metros = altura / 100  # Converter altura de centímetros para metros
        imc = peso / (altura_metros ** 2)
        return imc
    except ZeroDivisionError:
        return "Erro: Altura não pode ser zero."

def classificar_imc(imc):
    if imc < 16:
        return "Magreza grave"
    elif 16 <= imc < 17:
        return "Magreza moderada"
    elif 17 <= imc < 18.5:
        return "Magreza leve"
    elif 18.5 <= imc < 25:
        return "Peso saudável"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade Grau I"
    elif 35 <= imc < 40:
        return "Obesidade Grau II (severa)"
    else:
        return "Obesidade Grau III (mórbida)"

try:
    peso = float(input("Digite seu peso em quilogramas: "))
    altura = float(input("Digite sua altura em centímetros: "))
    imc = calcular_imc(peso, altura)

    if type(imc) == float:
        print(f"Seu IMC é: {imc:.2f}")
        classificacao = classificar_imc(imc)
        print(f"Classificação: {classificacao}")
    else:
        print(imc)

except ValueError:
    print("Erro: Certifique-se de inserir números válidos para peso e altura.")
