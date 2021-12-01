nmrs = list(map(int,input().split()))
insert = []
b = int(input())

def buscabinaria(lista, item):
    inicio = 0
    final = len(lista)-1
    here = 0
    found = 0

    while final >= inicio and acheikrl == 0:
        meio = (inicio + final)//2
        if (item == lista[meio]):
            here = 1
            found = index.lista[meio]
        else:
            if (item < lista[meio]):
                final = meio-1

            else:
                inicio = meio+1

    return(found)

print(buscabinaria(nmrs,b))
