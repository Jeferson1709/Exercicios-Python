# Faça um programa que peça o raio de um círculo, calcule e mostre sua área:
import math

raio = float(input('Entre com o raio: '))
area = math.pi * (raio ** 2)
print(f'A área de círculo com raio {raio} é: {area:.2f}')