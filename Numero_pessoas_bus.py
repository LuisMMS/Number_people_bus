'''Number of People in the Bus
Há um ônibus circulando na cidade, que leva e solta algumas pessoas em cada parada.

Você recebe uma lista (ou matriz) de pares inteiros. Os elementos de cada par representam o número de pessoas que entram no ônibus (o primeiro item) e o número de pessoas que saem do ônibus (o segundo item) em um ponto de ônibus.

Sua tarefa é retornar o número de pessoas que ainda estão no ônibus após a última estação de ônibus (após a última matriz). Apesar de ser o último ponto de ônibus, o ônibus não está vazio e algumas pessoas ainda estão dentro do ônibus, e provavelmente estão dormindo lá: D

Dê uma olhada nos casos de teste.

Lembre-se de que os casos de teste garantem que o número de pessoas no ônibus seja sempre> = 0. Portanto, o número inteiro de retorno não pode ser negativo.

O segundo valor na primeira matriz de inteiros é 0, uma vez que o ônibus está vazio na primeira parada..
'''
def number(bus_stops):
    lista1=[]
    sum1=0
    sum2=0
    sum=0
    
    for movement in bus_stops:
        for i in movement:
            lista1.append(i)
    
    k=0
    while k<len(lista1):
        sum1+=lista1[k]
        k=k+2
    
    z=1
    while z<=len(lista1):
        sum2+=lista1[z]
        z=z+2
        
    sum=sum1-sum2
    return sum
