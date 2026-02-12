

## Escreva um programa que soma dois números inteiros inseridos pelo usuário.
## Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
##Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

###
# numero_01 = int(input("inserir um numero inteiro:"))
# numero_02 = int(input("inserir outro numero inteiro:"))

# resultado = numero_01 // numero_02

# print(resultado)


#Números de Ponto Flutuante (float)
#Escreva um programa que receba dois números flutuantes e realize sua adição.
#Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
#Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
#Faça um programa que converta a temperatura de Celsius para Fahrenheit.
#Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada

import math
raio_do_circulo= float(input("digite o raio: "))
area_do_circulo = math.pi * raio_do_circulo ** 2
print(f"{area_do_circulo:.2f}")