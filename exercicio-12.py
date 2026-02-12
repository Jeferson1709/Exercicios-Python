# Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes, usando a seguinte fórmula:

tamanho_gb = float(input('Digite o tamanho do arquivo em GBs: '))
tamanho_mb = tamanho_gb * 1_024
print(f'O arquivo tem {tamanho_mb} MBs')