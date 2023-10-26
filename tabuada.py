'''
	Elaborar um programa em Python que efetue o cálculo de uma tabuada de um número qualquer e armazene os resultados em uma lista A para 11 elementos. Apresentar os valores armazenados na lista.
'''

listaA = []
resp = 1

while resp != 0:
    num = int(input("Digite um número para exibir a tabuada : "))
    for i in range(1,11):
        listaA.append(i * num)

    print("\n==== Tabuada ====\n")
    for i in range(10):
        print(f"{num} x {i + 1} = {listaA[i]}")

    resp = int(input("\nRepetir (1-SIM / 0-NÃO) : "))
