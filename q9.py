
nome=['bola','morcego','luva','luva','luva']
preco=[2,3,1,2,1]
peso=[2,5,1,1,1]
nomes=[]
rep=[]
cont=0
quant3=1
for n in nome:
    if(n not in nomes):
        nomes.append(n)
    else:
        rep.append(cont)
        quant3+=1
    cont+=1
v2=0
v3=0
v4=0
quant=0
quant2=0
quant_f=0
for i in rep:
    v2=preco[i]
    for j in preco:
        if v2 in preco:
            quant+=1
#se a quantidade de numeros repetidos passar de 1
    v3=peso[i]
    for k in preco:
        if v2 in preco:
            quant2+=1
    quant_f+=1
if(quant>0 and quant2>0 and quant3>1):
    print(quant_f)