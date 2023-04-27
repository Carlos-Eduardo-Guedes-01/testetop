numero=32
valor=''
base=2
while(numero>=base):
    valor=valor+str(numero%base)
    numero=int(numero/base)
print(valor)