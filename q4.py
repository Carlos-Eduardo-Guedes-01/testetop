pang=["pack my box with five dozen liquor jugs's is a pangram, because it contains all the letters 'a' though 'z'",'this is not a pangram']
alfa=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
quant=0
for i in pang:
    for j in alfa:
        if(j in i):
            quant+=1
    if(quant==26):
        print(1,end='')
    else:
        print(0,end='')
