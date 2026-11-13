def area_triangulo(base, altura):
    return (base * altura) / 2

def area_retangulo(base, altura):
    return base * altura

print("1 - Triângulo")
print("2 - Retângulo")
opcao = input("Escolha: ")

base = float(input("Base: "))
altura = float(input("Altura: "))

if opcao == "1":
    print("Área do triângulo:", area_triangulo(base, altura))
elif opcao == "2":
    print("Área do retângulo:", area_retangulo(base, altura))
else:
    print("Opção inválida")