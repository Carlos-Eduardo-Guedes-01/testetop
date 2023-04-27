num=[3,13,4,11,9]
soma=sum(num)
print(num[0],end='')
cont=1
while(cont<len(num)):
    print(' +',num[cont],end='')
    cont+=1
print(' =',soma)