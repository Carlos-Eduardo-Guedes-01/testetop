string='caranguejo'
cont=0
resposta=''
invert=''
for i in string:
    if(cont>=(len(string)-2)):
        invert=invert+i
    cont+=1
resposta=invert[::-1]
print(resposta)