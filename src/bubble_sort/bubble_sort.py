def bubble_sort(lista):
    check_type = lambda x: not isinstance(x,(int,float))
    if not isinstance(lista, list):
        raise TypeError("Provied list contains corrupted values!")
    if any( [check_type(x) for x in lista] ):
        raise TypeError("Provied list contains corrupted values!")
    n = len(lista)
    i = 0
    while n > 1:
        zamien = False
        for l in range(0, n-1):
            if lista[l] > lista[l+1]:
                lista[l], lista[l+1] = lista[l+1], lista[l]
                i += 1
                zamien = True
        n -= 1
        if zamien == False: break
        
    return lista, i