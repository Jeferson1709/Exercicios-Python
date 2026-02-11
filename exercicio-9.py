# Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

f = float(input("Informe a temperatura em graus Fahrenheit: "))

c = (f - 32) * 5/9

print(f"{f}°F equivalem a {c:.2f}°C")
