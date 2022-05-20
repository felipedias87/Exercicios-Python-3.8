#Exemplo de lógica
contador = int(input("Digite o numero"))
array = []
while contador > 0:
    contador = contador - 1
    array.append(contador)
teste = ' '
lista_unica = list(set(array))
for lista in lista_unica:
    if lista > 0:
        cont = 0
        for a in range(lista):
            cont = cont + 1
            teste = teste +" "+ str(lista)
            if(cont == lista):
                print(teste)
                teste=' '

