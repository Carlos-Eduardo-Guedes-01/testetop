n=5
peso=[1.01,1.99,2.5,1.5,3.01]
p_total=sum(peso)
cont=0
if(p_total>3):
    while p_total>=0:
        cont+=1
        p_total-=3
print(cont)