# Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado =float (input("Digite o lado do quadrado: "))
area  = lado ** 2
dobroArea = area * 2
print(f"O dobro da área de {area:.1f}m² é: {dobroArea:.1f}m²")