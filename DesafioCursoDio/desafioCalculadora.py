num1 = input("Digite um número; ")

operacao = input("Digite a operação desejada: ")
num2 = input("Digite outro número: ")
if operacao == "+":
    resultado = int(num1) + int(num2)
elif operacao == "-":
    resultado = int(num1) - int(num2)
elif operacao == "*":
    resultado = int(num1) * int(num2)
elif operacao == "/":
    resultado = int(num1) / int(num2)
else:
    print("Operação inválida")
print("Resultado: ", resultado)
# Desafio: Criar uma calculadora simples que aceite dois números e uma operação (adição, subtração, multiplicação ou divisão) e retorne o resultado.
# Exemplo de uso:
# Digite um número: 10
# Digite outro número: 5
# Digite a operação desejada: +
# Resultado: 15