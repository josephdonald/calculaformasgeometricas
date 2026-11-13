#  Arquivo principal do sistema que calcula área geométricas que virão de outros arquivos

def calcular_area_retangulo():
    base = float(input("Digite a base do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    area = base * altura
    return area

def calcular_area_circulo():
    raio = float(input("Digite o raio do círculo: "))
    area = 3.14 * raio ** 2
    return area

def calcular_area_triangulo():
    base = float(input("Digite a base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))
    area = (base * altura) / 2
    return area

def main():
    print("Escolha a forma geométrica para calcular a área:")
    print("1. Retângulo")
    print("2. Círculo")
    print("3. Triângulo")

    escolha = input("Digite o número correspondente à forma geométrica: ")

    if escolha == "1":
        area = calcular_area_retangulo()
        print(f"A área do retângulo é: {area}")
    elif escolha == "2":
        area = calcular_area_circulo()
        print(f"A área do círculo é: {area}")
    elif escolha == "3":
        area = calcular_area_triangulo()
        print(f"A área do triângulo é: {area}")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

main()