# Faça um programa que peça as 4 notas bimestrais e mostre a média.

somaDasNotas = 0
media = 0
for i in range(4):
    nota = float(input(f"Digite a nota do {i+1}º bimestre: "))
    somaDasNotas += nota

    
media = somaDasNotas / 4;

print(f"Sua nota bimestral é: {media}")

    
    