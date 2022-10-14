# 2 - Escreva um programa que mostre os números de 1 até um numero
# digitado pelo usuário, mas apenas os números impares.
n = int(input("Digite um número: "))
x = 1
while x <= n:
    while x % 2 != 0:
        print(x)
        x = x + 1
    x = x + 1
