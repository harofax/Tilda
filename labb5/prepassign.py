def utskrift(lista):
    if len(lista) > 0:
        print(lista[0])
        utskrift(lista[1:])

