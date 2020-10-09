def good_pairs(arr):
    visitado = {}
    contagem = 0
    for elemento in arr:
        if elemento in visitado:
            contagem += visitado[elemento]
            visitado[elemento] += 1
        else:
            visitado[elemento] = 1
    return contagem

arr = [2, 5, 1, 2, 3, 2, 5, 1, 2, 1]

print(good_pairs(arr))