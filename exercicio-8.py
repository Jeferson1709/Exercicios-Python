# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.


salarioPorHora = float(input("Digite o seu salário por hora: "))
horasTrabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
salarioTotal = salarioPorHora * horasTrabalhadas
print(f'O salário deste mês será: {salarioTotal:.2f}')