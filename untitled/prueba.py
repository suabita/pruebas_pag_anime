karen = [0,"gato",1,False,4]
lista =[]
perro = 'zorro, gripa, 2'
for valor in karen:
    if isinstance(valor,str):
        lista.append(valor)
print(lista)
for valor in perro:
    try:
        a=int(valor)
    except ValueError:
        pass
    else:
        print(valor)

def universidad(materias):
    for materia,profesor in materias.items():
        if isinstance(profesor,str):
            print(profesor)
universidad({'control':'andres','dsp':4})